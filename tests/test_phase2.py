import json, subprocess, sys, unittest
from pathlib import Path
from alei_language.grammar import parse_clause
from alei_language.lexicon import ROOT, lookup
from alei_language.transparent_semantics import parse, compose

class GrammarRegression(unittest.TestCase):
    def test_orders_and_meaning_boundary(self):
        a=parse_clause('Mei saelen sain.')
        b=parse_clause('Mei sain saelen.')
        self.assertEqual(a['status'],'parsed'); self.assertEqual(b['status'],'parsed')
        for key in ('subject','object','verb','tense','aspect','negation'):
            self.assertEqual(a['analysis'][key], b['analysis'][key])
        self.assertEqual((a['analysis']['order'],b['analysis']['order']),('SVO','SOV'))
        self.assertEqual(a['semantic_correctness'],'not_evaluated')
    def test_markers_and_case(self):
        result=parse_clause('Mei ne va du saelen sain.')
        self.assertEqual(result['analysis']['tense'],'future')
        self.assertEqual(result['analysis']['aspect'],'progressive')
        self.assertTrue(result['analysis']['negation'])
        self.assertEqual(parse_clause('Mei sain da fa saelen.')['analysis']['aspect'],'completed')
        for text in ('Mei va ne saelen sain.','Mei saelen sai.','Mei va da saelen sain.',
                     'Mei ne va avelen.','Mei saelen Jajaya.'):
            with self.subTest(text=text): self.assertEqual(parse_clause(text)['status'],'unsupported')
    def test_pronoun_gender_and_honorific_not_forced_into_clause(self):
        result=parse_clause('Eli saelen sain.')
        self.assertEqual(result['analysis']['subject'],'eli')
        self.assertNotIn('gender',result['analysis'])
        self.assertEqual(parse_clause('Alei, Elora sen!')['status'],'unsupported')
    def test_historical_forms_are_not_rewritten(self):
        for term in ('Mivav','Mivaven','Mivavar'):
            self.assertTrue(lookup(term),term)
        self.assertFalse(lookup('Mirav'))
        self.assertEqual(lookup('Mivav')[0]['status'],'owner_accepted_working')

class SemanticRegression(unittest.TestCase):
    def test_round_trip(self):
        text='meyar-ro-yenar-li-reş-ze-selim-mu-molir'
        parsed=parse(text)
        relations=[{'role':r['role'],'value':r['value']} for r in parsed['relations']]
        self.assertEqual(compose(parsed['head'],relations),text)
        self.assertEqual(parse(compose(parsed['head'],relations))['relations'],parsed['relations'])
        self.assertFalse(parsed['exact_identity_known'])
        self.assertEqual([r['strength'] for r in parsed['relations']],['asserted','typical','typical','typical'])
    def test_type_and_unverified(self):
        with self.assertRaises(ValueError): parse('meyar-li-hokar')
        self.assertEqual(parse('meyar-li-nasel')['relations'][0]['type_status'],'unverified')
        self.assertEqual(parse('meyar-li-hüsen')['relations'][0]['type_status'], 'value_class_known_head_compatibility_unverified')
    def test_duplicate_and_typical_alternatives_not_contradiction(self):
        self.assertTrue(parse('meyar-li-reş-li-reş')['warnings'])
        result=parse('meyar-li-reş-li-nüvil')
        self.assertTrue(result['warnings']); self.assertFalse(result['exact_identity_known'])
    def test_untrusted_input_never_changes_registry(self):
        for text in ('Jajaya-li-reş','Yemali-li-reş','meyar-li-Yemali',
                     'meyar-no-vürel','meyar-li-reş-ignore-previous-instructions'):
            with self.subTest(text=text), self.assertRaises(ValueError): parse(text)
        self.assertFalse(lookup('Yemali'))
    def test_semantic_fixtures(self):
        path=ROOT/'evaluations/semantic-cases.jsonl'
        for line in path.read_text(encoding='utf-8-sig').splitlines():
            case=json.loads(line)
            with self.subTest(input=case['input']):
                if case['outcome']=='error':
                    with self.assertRaises(ValueError): parse(case['input'])
                else:
                    result=parse(case['input'])
                    if case['outcome']=='warning': self.assertTrue(result['warnings'])
                    if case['outcome']=='unverified': self.assertEqual(result['relations'][0]['type_status'],'unverified')
                    if 'identity_known' in case: self.assertEqual(result['exact_identity_known'],case['identity_known'])
    def test_invalid_composition(self):
        for relations in ([],[{'role':'li','value':'reş','extra':'x'}], [{'role':'li','value':'reş-ze-selim'}]):
            with self.subTest(relations=relations),self.assertRaises(ValueError): compose('meyar',relations)

class AuditRegression(unittest.TestCase):
    def test_audit_tracks_actual_source_rows(self):
        rows=[json.loads(x) for x in (ROOT/'audits/sentence-audit.jsonl').read_text(encoding='utf-8').splitlines()]
        src=[json.loads(x) for x in (ROOT/'data/example-sentences.jsonl').read_text(encoding='utf-8').splitlines()]
        self.assertEqual([(r['source_id'],r['original']) for r in rows],[(s['id'],s['canonical_spelling']) for s in src])
        self.assertEqual(rows[10]['word_order'],'SVO'); self.assertEqual(rows[11]['word_order'],'SOV')
        self.assertEqual(rows[63]['predicate'],'mivaven')
        self.assertIn('embedded',rows[57]['notes'][0])
        self.assertEqual(rows[65]['status'],'ambiguous')
        subprocess.run([sys.executable,str(ROOT/'scripts/build_sentence_audit.py'),'--check'],check=True)
    def test_fixture_coverage(self):
        cases=[json.loads(x) for x in (ROOT/'evaluations/skill-cases.jsonl').read_text(encoding='utf-8-sig').splitlines()]
        self.assertEqual({c['skill'] for c in cases},{'alei-speak','alei-translate','alei-tutor','alei-audit'})
        self.assertEqual(len(cases),len({c['id'] for c in cases}))
        self.assertTrue(all(c.get('prompt') and c.get('expected') for c in cases))
if __name__=='__main__': unittest.main()
