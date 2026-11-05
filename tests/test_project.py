import unittest, sys, subprocess, json, hashlib
from pathlib import Path
from alei_language.lexicon import lookup, normalize, ROOT
from alei_language.orthography import validate, syllables, stress_index
from alei_language.morphology import analyze, plural, object_form, analyze_simple_sentence
from alei_language.transparent_semantics import parse
class LanguageTests(unittest.TestCase):
    def test_roots_status_and_count(self):
        rows=[json.loads(x) for x in (ROOT/'data/roots.jsonl').read_text(encoding='utf-8').splitlines()]
        self.assertEqual(len(rows),270)
        for status,count in [('owner_locked',34),('owner_accepted_working',56),('delegated_v1',180)]:
            with self.subTest(status=status): self.assertEqual(sum(r['status']==status for r in rows),count)
    def test_attested_words(self):
        for word in ['Mei','Sai','Eli','Elar','Meina','Saina','Elina','sen','rin','mel','ael','Sael','Haur','Belem','Mivav','Saelen','Belemlen','Oren','Firen']:
            with self.subTest(word=word): self.assertTrue(lookup(word))
        for word in ['ser','seri','Jajaya']:
            with self.subTest(word=word): self.assertFalse(lookup(word))
    def test_orthography(self):
        for word in ['Sael','Añel','Miŋ','Ünar','Firen']:
            with self.subTest(word=word): self.assertEqual(validate(word),[])
        for word in ['xen','çel','aaai','strra']:
            with self.subTest(word=word): self.assertTrue(validate(word))
        self.assertEqual(syllables('Saelen'),['ae','e']); self.assertEqual(stress_index('Saelen'),0)
        self.assertEqual(syllables('Velia'),['e','i','a']); self.assertEqual(normalize('Iİ'),'ıi')
    def test_morphology(self):
        self.assertEqual(plural('Lera'),'Lerana'); self.assertEqual(object_form('Sai'),'Sain')
        self.assertEqual(object_form('Tüvan'),'Tüvanan'); self.assertEqual(object_form(plural('Lera')),'Leranan')
        self.assertEqual(analyze('Oren')['status'],'attested'); self.assertEqual(analyze('Firen')['status'],'attested')
        self.assertEqual(analyze('Jajaya')['status'],'unknown')
        self.assertTrue(any(c['operation']=='plural_object' for c in analyze('Leranan')['candidates']))
    def test_basic_sentence_orders(self):
        a=analyze_simple_sentence('Mei saelen sain.')
        b=analyze_simple_sentence('Mei sain saelen.')
        self.assertEqual((a['subject'],a['verb'],a['object']),('mei','saelen','sai'))
        self.assertEqual((b['subject'],b['verb'],b['object']),('mei','saelen','sai'))
        self.assertEqual((a['order'],b['order']),('SVO','SOV'))
        self.assertFalse(a['object_focus']); self.assertTrue(b['object_focus'])
        self.assertEqual(analyze_simple_sentence('Mei saelen sai.')['status'],'unsupported')
    def test_semantics(self):
        result=parse('meyar-ro-yenar-li-reş-ze-selim-mu-molir')
        self.assertFalse(result['exact_identity_known']); self.assertEqual([r['strength'] for r in result['relations']],['asserted','typical','typical','typical'])
        for bad in ['Jajaya','meyar-no-vürel','meyar-li-hokar','meyar-li','meyar-xx-reş']:
            with self.subTest(bad=bad), self.assertRaises(ValueError): parse(bad)
        self.assertEqual(parse('meyar-su-lavar')['relations'][0]['strength'],'typical')
    def test_source_and_derived(self):
        manifest=json.loads((ROOT/'standard/manifest.json').read_text(encoding='utf-8'))
        original=(ROOT/'adsiz_dil_acik_anlam_standardi_v1_0.md').read_bytes()
        archived=(ROOT/'standard'/manifest['standard']['file']).read_bytes()
        self.assertEqual(original,archived); self.assertEqual(hashlib.sha256(archived).hexdigest(),manifest['standard']['sha256'])
        subprocess.run([sys.executable,str(ROOT/'scripts/derive_data.py'),'--check'],check=True)
    def test_examples_attested(self):
        rows=[json.loads(x) for x in (ROOT/'data/example-sentences.jsonl').read_text(encoding='utf-8').splitlines()]
        self.assertEqual(len(rows),101)
        self.assertEqual(rows[10]['canonical_spelling'],'Mei saelen sain.')
        self.assertEqual(rows[11]['canonical_spelling'],'Mei sain saelen.')
        self.assertIn('seni',rows[10]['gloss_tr'].lower()); self.assertIn('seni',rows[11]['gloss_tr'].lower())
    def test_skills(self): subprocess.run([sys.executable,str(ROOT/'scripts/validate_skills.py')],check=True)
if __name__=='__main__': unittest.main()
