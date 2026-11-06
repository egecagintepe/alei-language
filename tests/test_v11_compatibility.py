import hashlib,json,os,subprocess,sys,unittest
from pathlib import Path
from alei_language.lexicon import ROOT,lookup,records,resolve_version
from alei_language.morphology import analyze
from alei_language.grammar import parse_sentence,parse_clause
from alei_language.examples_translation import translate_help_example

class VersionCompatibility(unittest.TestCase):
 def test_original_hash_and_reproduction(self):
    original=(ROOT/'adsiz_dil_acik_anlam_standardi_v1_0.md').read_bytes()
    archived=(ROOT/'standard/adsiz_dil_acik_anlam_standardi_v1_0.md').read_bytes()
    self.assertEqual(original,archived)
    self.assertEqual(hashlib.sha256(archived).hexdigest(),'265fcc0dd0fcaf4bd23a062d631855463201be4ac12e42bf2501f30628ee8504')
    for script in ('derive_data.py','derive_v11.py'):
        subprocess.run([sys.executable,str(ROOT/'scripts'/script),'--check'],check=True)
 def test_current_name_and_greeting(self):
    overlay=json.loads((ROOT/'standard/versions/1.1.0.json').read_text(encoding='utf-8-sig'))
    self.assertEqual(overlay['language_name'],'Alei'); self.assertEqual(resolve_version('current'),'1.1.0')
    self.assertEqual(lookup('Alei','1.0'),lookup('Alei','1.1.0'))
    self.assertEqual(lookup('Alei','1.1.0')[0]['gloss_tr'],'merhaba')
 def test_default_v1_unchanged(self):
    self.assertEqual(lookup('Mivav'),lookup('Mivav','1.0'))
    self.assertEqual(lookup('Mivav')[0]['status'],'owner_accepted_working')
    self.assertFalse(lookup('Mirav'));self.assertFalse(lookup('Miraven'))
    self.assertEqual(analyze('Mivaven')['status'],'attested')
 def test_owner_preferred_and_legacy(self):
    for new,old in [('Mirav','Mivav'),('Miraven','Mivaven')]:
        preferred=lookup(new,'1.1.0')[0];legacy=lookup(old,'1.1.0')[0]
        self.assertEqual(preferred['status'],'owner_adopted');self.assertEqual(preferred['decision_id'],'AD-2026-002')
        self.assertEqual(legacy['status'],'legacy_alias');self.assertEqual(legacy['preferred_form'],new)
        self.assertIn('Legacy',legacy['warning']);self.assertEqual(legacy['id'],lookup(old,'1.0')[0]['id'])
        self.assertEqual(preferred['historical_reference']['id'],legacy['id'])
        self.assertEqual(preferred['historical_reference']['provenance'],legacy['provenance'])
        self.assertEqual(analyze(old,'current')['status'],'legacy_alias')
 def test_agent_noun_is_unresolved(self):
    self.assertEqual(lookup('Mivavar','1.1.0')[0]['status'],'historical_v1_pending')
    self.assertFalse(lookup('Miravar','1.1.0'))
    self.assertNotEqual(analyze('Miravar','1.1.0')['status'],'attested')
 def test_counts_and_other_roots(self):
    old=list(records('1.0')); new=list(records('1.1.0'))
    self.assertEqual(sum(r['part_of_speech']=='root' for r in new),270)
    self.assertEqual(len([r for r in new if r['id'].startswith('lexemes:') or r['id'].startswith('ad:1.1.0:lexeme:')]),273)
    self.assertEqual(len(list(records('1.1.0',True)))-len(new),3)
    for term in ('Sael','Arem','Norel','Añel','Haur','Belem','Mir','Mürav'):
        self.assertEqual(lookup(term,'1.0'),lookup(term,'1.1.0'))
    old_untouched={r['id']:r for r in old if r['canonical_spelling'] not in ('Mivav','Mivaven','Mivavar')}
    new_by_id={r['id']:r for r in new}
    for key,value in old_untouched.items(): self.assertEqual(new_by_id[key],value)
 def test_morphology_and_current_resolution(self):
    for word,operation in [('Miravna','plural'),('Miravan','object')]:
        result=analyze(word,'1.1.0');self.assertEqual(result['status'],'candidate')
        self.assertTrue(any(x.get('base')=='Mirav' and x.get('operation')==operation for x in result['candidates']))
    legacy=analyze('Mivavan','1.1.0')
    self.assertTrue(any(c.get('status')=='legacy_candidate' and c.get('preferred_base')=='Mirav' for c in legacy['candidates']))
    self.assertTrue(parse_sentence('Mei naelen mivavan.','1.1.0').get('warnings'))
    self.assertEqual(lookup('Miraven','current'),lookup('Miraven','1.1.0'))
    with self.assertRaises(ValueError): lookup('Mirav','2.0')
 def test_examples_structure_translation_and_legacy_warning(self):
    for text,version in [('Mei mivaven sain.','1.0'),('Mei mivaven sain.','1.1.0'),('Mei miraven sain.','1.1.0')]:
        result=translate_help_example(text,version);self.assertEqual(result['tr'],'Sana yardım ediyorum.')
        self.assertEqual(result['en'],'I help you.')
        self.assertEqual(bool(result['warnings']),text.startswith('Mei mivaven') and version=='1.1.0')
    for text,version in [('Eli va mivaven sain.','1.0'),('Eli va mivaven sain.','1.1.0'),('Eli va miraven sain.','1.1.0')]:
        self.assertEqual(translate_help_example(text,version)['tr'],'O sana yardım edecek.')
    self.assertTrue(parse_clause('Mei mivaven sain.','1.1.0').get('warnings'))
    self.assertEqual(translate_help_example('Mei miraven sain.','1.0')['status'],'unsupported')
    self.assertEqual(translate_help_example('Mei ne miraven sain.','1.1.0')['status'],'unsupported')
 def test_cli_default_and_explicit(self):
    env={**os.environ,'PYTHONPATH':str(ROOT/'src'),'PYTHONIOENCODING':'utf-8'}
    def run(*args):
        result=subprocess.run([sys.executable,'-m','alei_language.cli',*args],cwd=ROOT,env=env,check=True,capture_output=True,text=True,encoding='utf-8')
        return json.loads(result.stdout)
    self.assertEqual(run('lookup','Mirav'),[])
    self.assertEqual(run('lookup','Mirav','--version','current')[0]['status'],'owner_adopted')
    self.assertEqual(run('lookup','Mivav','--version','1.1.0')[0]['status'],'legacy_alias')
 def test_current_docs_and_decisions(self):
    decisions=json.loads((ROOT/'governance/decisions/2026-11-05.json').read_text(encoding='utf-8-sig'))
    self.assertEqual({d['id'] for d in decisions},{'AD-2026-001','AD-2026-002'})
    self.assertTrue(all(d['authority']=='language owner' for d in decisions))
    for name in ('README.md','README.tr.md','GOVERNANCE.md','standard/README.md'):
        text=(ROOT/name).read_text(encoding='utf-8')
        self.assertNotIn('the language has no official name',text.lower())
        self.assertNotIn('resmî adı henüz seçilmedi',text.lower())
if __name__=='__main__':unittest.main()
