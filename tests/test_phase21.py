import json, subprocess, sys, unittest
from pathlib import Path
from alei_language.grammar import parse_sentence
from alei_language.lexicon import ROOT

class ExtendedGrammarTests(unittest.TestCase):
    def test_nominal_predicate_and_temporal_markers(self):
        for text,negative,tense in [('Mei süli.',False,'unmarked'),('Mei ne süli.',True,'unmarked'),('Mei da süli.',False,'da')]:
            with self.subTest(text=text):
                result=parse_sentence(text)
                self.assertEqual(result['status'],'parsed')
                self.assertEqual(result['analysis']['construction'],'nominal_predicate')
                self.assertEqual(result['analysis']['negation'],negative)
                self.assertEqual(result['analysis']['tense'],tense)
                self.assertEqual(result['semantic_correctness'],'not_evaluated')
    def test_location_and_possession_are_distinct(self):
        phrase=parse_sentence('Mei ri lem.')['analysis']
        self.assertEqual(phrase['construction'],'possession_phrase')
        self.assertNotIn('subject',phrase)
        loc=parse_sentence('Mei Sai ri lem lo.')['analysis']
        self.assertEqual((loc['subject'],loc['possessor'],loc['location']),('mei','sai','lem'))
        self.assertEqual(parse_sentence('Mei lem lo.')['analysis']['location'],'lem')
    def test_marked_noun_objects_and_order(self):
        a=parse_sentence('Sai da sileven tüvanan.')['analysis']
        b=parse_sentence('Sai tüvanan da sileven.')['analysis']
        self.assertEqual((a['object'],b['object']),('tüvan','tüvan'))
        self.assertEqual((a['order'],b['order']),('SVO','SOV'))
        self.assertEqual(parse_sentence('Sai sileven tüvan.')['status'],'unsupported')
    def test_questions(self):
        for text,interrogative in [('Sai vena?','vena'),('Keli da avelen?','keli'),('Sai naelen mivan?','miva')]:
            with self.subTest(text=text):
                a=parse_sentence(text)['analysis']; self.assertTrue(a['question']); self.assertEqual(a['interrogative'],interrogative)
        self.assertTrue(parse_sentence('Sai süli le?')['analysis']['question'])
        self.assertEqual(parse_sentence('Keli da avelen le?')['status'],'unsupported')
    def test_embedded_verb_has_object_and_optional_subject(self):
        a=parse_sentence('Sai yelen ke sileven tüvanan le?')['analysis']
        self.assertEqual((a['verb'],a['embedded_verb'],a['embedded_object']),('yelen','sileven','tüvan'))
        a=parse_sentence('Mei naelen ke Sai avelen.')['analysis']
        self.assertEqual((a['subject'],a['embedded_subject']),('mei','sai'))
        self.assertEqual(parse_sentence('Mei naelen ke avelen lem ta.')['analysis']['destination'],'lem')
    def test_scope_negation_and_unrecognized_forms(self):
        a=parse_sentence('Mei ne va avelen.')['analysis']
        self.assertEqual((a['negation'],a['tense']),(True,'va'))
        for text in ('Mei va ne avelen.','Mei naelen ke Jajaya.','Mei yelen ke ke avelen.', 'Alei, Elora sen!', 'Mei saelen Jajaya.'):
            with self.subTest(text=text): self.assertEqual(parse_sentence(text)['status'],'unsupported')

class IndependentFieldsTests(unittest.TestCase):
    def test_review_status_is_not_parser_status(self):
        rows=[json.loads(line) for line in (ROOT/'audits/sentence-audit.jsonl').read_text(encoding='utf-8').splitlines()]
        self.assertEqual(len(rows),101)
        self.assertEqual((rows[0]['parser_status'],rows[0]['linguistic_review_status'],rows[0]['translation_review_status']),('unsupported','consistent','accurate'))
        self.assertEqual((rows[18]['parser_status'],rows[18]['linguistic_review_status'],rows[18]['translation_review_status']),('parsed','contextual','context_dependent'))
        self.assertEqual(rows[57]['extended_structure']['analysis']['embedded_object'],'tüvan')
        for row in rows:
            self.assertTrue(row['linguistic_review']['assessment'])
            self.assertIn(row['linguistic_review_status'],{'consistent','contextual','needs_review'})
            self.assertIn(row['translation_review_status'],{'accurate','context_dependent','questionable'})
            self.assertEqual(row['linguistic_review']['reviewer'],'project assistant, not independent human')
        subprocess.run([sys.executable,str(ROOT/'scripts/build_sentence_audit.py'),'--check'],check=True)
    def test_original_source_still_controls_historical_lookup(self):
        from alei_language.lexicon import lookup
        self.assertTrue(lookup('Mivav')); self.assertTrue(lookup('Mivaven')); self.assertTrue(lookup('Mivavar'))
        self.assertFalse(lookup('Mirav')); self.assertFalse(lookup('Miraven')); self.assertFalse(lookup('Miravar'))

if __name__=='__main__': unittest.main()
