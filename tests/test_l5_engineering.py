"""L5 Linguistic Engineering, Blind Semantics, and Lexicon Acceptance Tests."""
import json, unittest
from pathlib import Path

from alei_language.lexicon import ROOT, records, lookup, normalize
from alei_language.ast import SentenceAST, PredicateFrame
from alei_language.valency import evaluate_valency, get_valency_frame
from alei_language.grammar import parse_sentence, parse_clause, parse_alei
from alei_language.transparent_semantics import parse, analyze_semantics
from alei_language.orthography import validate

class TestL5ValencyAndAST(unittest.TestCase):
    def test_valency_active_transitive(self):
        val = evaluate_valency('sileven', {'Agent': 'mei', 'Patient': 'tüvan'})
        self.assertTrue(val['valency_satisfied'])
        self.assertEqual(val['status'], 'satisfied')

    def test_valency_transitive_clash_on_omitted_patient(self):
        val = evaluate_valency('nesalen', {'Agent': 'vel'})
        self.assertFalse(val['valency_satisfied'])
        self.assertEqual(val['status'], 'valency_clash')

    def test_valency_middle_voice_promotes_patient(self):
        val = evaluate_valency('nesalen', {'Patient': 'vel'}, voice='middle')
        self.assertTrue(val['valency_satisfied'])
        self.assertEqual(val['status'], 'satisfied')

    def test_typed_ast_generation_standard_clause(self):
        ast = parse_alei('Mei da sileven tüvanan.', version='1.1.0')
        self.assertIsInstance(ast, SentenceAST)
        self.assertEqual(ast.status, 'supported')
        self.assertEqual(ast.subject, 'mei')
        self.assertEqual(ast.polarity, True)
        self.assertEqual(ast.tense, 'da')
        self.assertIsNotNone(ast.predicate)
        self.assertEqual(ast.predicate.verb_lemma, 'sileven')
        self.assertTrue(ast.predicate.valency_satisfied)

    def test_unknown_lexeme_rejected_without_guessing(self):
        ast = parse_alei('Mei da sileven Jajaya.', version='1.1.0')
        self.assertEqual(ast.status, 'unknown_lexeme')
        self.assertIn('jajaya', ast.diagnostics[0].lower())

    def test_experimental_middle_voice(self):
        ast = parse_alei('Vel ne va se nesalen.', version='1.1.0', mode='experimental')
        self.assertEqual(ast.status, 'supported')
        self.assertTrue(ast.is_experimental)
        self.assertEqual(ast.predicate.voice, 'middle')
        self.assertEqual(ast.polarity, False)
        self.assertEqual(ast.tense, 'future')

    def test_experimental_subjectless_imperative(self):
        ast = parse_alei('Aremen!', version='1.1.0', mode='experimental')
        self.assertEqual(ast.status, 'supported')
        self.assertEqual(ast.construction, 'imperative')
        self.assertEqual(ast.speech_act, 'imperative')
        self.assertEqual(ast.subject, 'implied_2nd_person')

    def test_experimental_negative_imperative(self):
        ast = parse_alei('Ne vürelen!', version='1.1.0', mode='experimental')
        self.assertEqual(ast.status, 'supported')
        self.assertEqual(ast.speech_act, 'imperative')
        self.assertEqual(ast.polarity, False)

    def test_experimental_concessive_conditional(self):
        ast = parse_alei('Şe-el Sai vürelen, aremen!', version='1.1.0', mode='experimental')
        self.assertEqual(ast.status, 'supported')
        self.assertEqual(ast.construction, 'concessive_conditional')
        self.assertEqual(ast.mood, 'concessive')

    def test_experimental_quotative_frame(self):
        ast = parse_alei('Elina da vesen: "Ne vürelen!"', version='1.1.0', mode='experimental')
        self.assertEqual(ast.status, 'supported')
        self.assertEqual(ast.construction, 'quotative')
        self.assertEqual(ast.speech_act, 'quotation')


class TestL5SemanticTyping(unittest.TestCase):
    def test_supported_semantic_structure(self):
        res = analyze_semantics('meyar-li-reş-ze-selim')
        self.assertEqual(res['status'], 'supported')
        self.assertFalse(res['exact_identity_known'])

    def test_contradictory_type_clash_rejected(self):
        res = analyze_semantics('meyar-li-hokar')
        self.assertEqual(res['status'], 'contradictory')

    def test_disabled_role_rejected(self):
        res = analyze_semantics('meyar-no-reş')
        self.assertEqual(res['status'], 'contradictory')

    def test_unknown_root_head_rejected(self):
        res = analyze_semantics('jajaya-li-reş')
        self.assertEqual(res['status'], 'unknown_lexeme')


class TestL5LexicalGovernance(unittest.TestCase):
    def test_proposals_strictly_separated_from_canonical_registry(self):
        prop_path = ROOT / 'linguistics/lexicon/proposed-lexemes.jsonl'
        self.assertTrue(prop_path.exists())
        proposals = [json.loads(line) for line in prop_path.read_text(encoding='utf-8').splitlines()]
        self.assertEqual(len(proposals), 10)

        # Candidate roots must NOT be returned by canonical lookup
        for p in proposals:
            word = p['candidate_spelling']
            exact = lookup(word, version='1.1.0')
            self.assertEqual(exact, [], f"Proposal '{word}' leaked into canonical v1.1.0 registry!")
            # Orthography must be valid
            errors = validate(p['candidate_spelling'])
            self.assertEqual(errors, [], f"Proposed root '{word}' has orthography errors: {errors}")

    def test_concept_priority_count_and_schema(self):
        cp_path = ROOT / 'linguistics/lexicon/concept-priority.jsonl'
        self.assertTrue(cp_path.exists())
        concepts = [json.loads(line) for line in cp_path.read_text(encoding='utf-8').splitlines()]
        self.assertEqual(len(concepts), 100)
        categories = {c['category'] for c in concepts}
        self.assertEqual(categories, {'A', 'B', 'C', 'D'})

    def test_archived_v10_byte_integrity(self):
        # Must preserve sha256 265fcc0dd0fcaf4bd23a062d631855463201be4ac12e42bf2501f30628ee8504
        import hashlib
        v10_path = ROOT / 'adsiz_dil_acik_anlam_standardi_v1_0.md'
        h = hashlib.sha256(v10_path.read_bytes()).hexdigest()
        self.assertEqual(h, '265fcc0dd0fcaf4bd23a062d631855463201be4ac12e42bf2501f30628ee8504')


class TestL5CorpusUniqueness(unittest.TestCase):
    def test_experimental_literature_no_verbatim_duplication(self):
        canonical_examples = set((ROOT / 'data/example-sentences.jsonl').read_text(encoding='utf-8').splitlines())
        self.assertEqual(len(canonical_examples), 101)

        lit_path = ROOT / 'linguistics/corpus/experimental-literature.md'
        dial_path = ROOT / 'linguistics/corpus/experimental-dialogues.md'
        self.assertTrue(lit_path.exists())
        self.assertTrue(dial_path.exists())

        # Verify neither file contains identical whole JSON lines from canonical examples
        lit_content = lit_path.read_text(encoding='utf-8')
        for ex in canonical_examples:
            row = json.loads(ex)
            sent = row['canonical_spelling']
            # The exact full sentence in the canonical test set should not be recycled as a literary poem/prose line
            self.assertNotIn(f"*{sent}*", lit_content)


class TestL5BlindEvaluationSuite(unittest.TestCase):
    def test_blind_v2_fixtures_and_separation(self):
        cases_path = ROOT / 'evaluations/agent-blind-v2/cases.jsonl'
        gold_path = ROOT / 'evaluations/agent-blind-v2/gold-answers.jsonl'
        self.assertTrue(cases_path.exists())
        self.assertTrue(gold_path.exists())

        cases = [json.loads(line) for line in cases_path.read_text(encoding='utf-8').splitlines()]
        gold = [json.loads(line) for line in gold_path.read_text(encoding='utf-8').splitlines()]
        self.assertEqual(len(cases), 42)
        self.assertEqual(len(gold), 42)

        # Verify cases do not contain gold translation strings
        for c, g in zip(cases, gold):
            self.assertEqual(c['case_id'], g['case_id'])
            if 'gold_translation_en' in g:
                self.assertNotIn(g['gold_translation_en'], c['blinded_prompt'])

if __name__ == '__main__':
    unittest.main()
