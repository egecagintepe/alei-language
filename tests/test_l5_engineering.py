"""L5 Linguistic Engineering, Blind Semantics, and Lexicon Acceptance Tests."""
import json, unittest
from pathlib import Path

from alei_language.lexicon import ROOT, records, lookup, normalize
from alei_language.ast import SentenceAST, PredicateFrame
from alei_language.valency import evaluate_valency, get_valency_frame
from alei_language.grammar import parse_sentence, parse_clause, parse_alei
from alei_language.transparent_semantics import parse, analyze_semantics
from alei_language.orthography import validate
from alei_language.morphology import object_form

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
        self.assertTrue(any('collides with canonical instrumental postposition' in w for w in ast.warnings))

    def test_experimental_subjectless_imperative(self):
        ast = parse_alei('Aremen!', version='1.1.0', mode='experimental')
        self.assertEqual(ast.status, 'supported')
        self.assertEqual(ast.construction, 'imperative')
        self.assertEqual(ast.speech_act, 'imperative')
        self.assertEqual(ast.subject, 'implied_2nd_person')

    def test_standard_subjectless_imperative(self):
        # Canonical under v1.0 standard §4.1: clear commands permit omitted pronouns
        ast = parse_alei('Aremen!', version='1.1.0', mode='standard')
        self.assertEqual(ast.status, 'supported')
        self.assertEqual(ast.construction, 'imperative')
        self.assertEqual(ast.speech_act, 'imperative')
        self.assertEqual(ast.subject, 'implied_2nd_person')
        self.assertFalse(ast.is_experimental)

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
        canonical_examples = [json.loads(line) for line in (ROOT / 'data/example-sentences.jsonl').read_text(encoding='utf-8').splitlines()]
        self.assertEqual(len(canonical_examples), 101)

        lit_path = ROOT / 'linguistics/corpus/experimental-literature.md'
        dial_path = ROOT / 'linguistics/corpus/experimental-dialogues.md'
        self.assertTrue(lit_path.exists())
        self.assertTrue(dial_path.exists())

        lit_content = normalize(lit_path.read_text(encoding='utf-8'))
        dial_content = normalize(dial_path.read_text(encoding='utf-8'))
        for ex in canonical_examples:
            sent = normalize(ex['canonical_spelling']).strip().rstrip('.!?')
            for line in lit_content.splitlines():
                clean = line.strip().strip('*`_').strip().rstrip('.!?')
                if clean:
                    self.assertNotEqual(clean, sent, f"Canonical sentence '{sent}' duplicated in literature!")
            for line in dial_content.splitlines():
                clean = line.strip().strip('*`_').strip().rstrip('.!?')
                if clean:
                    self.assertNotEqual(clean, sent, f"Canonical sentence '{sent}' duplicated in dialogues!")


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


class TestL5LinguisticAuditRegressions(unittest.TestCase):
    """Rigorous regression tests for all 11 audited lexical and grammatical issues."""

    def test_canonical_lexical_provenance(self):
        # 1. Arem is thinking (roots:434), NOT returning
        arem = lookup('Arem')[0]
        self.assertEqual(arem['semantic_anchor_en'], 'thinking')
        self.assertIn('düşünce', arem['gloss_tr'])

        # Canonical returning is Nelar (roots:656)
        nelar = lookup('Nelar')[0]
        self.assertEqual(nelar['semantic_anchor_en'], 'returning')
        self.assertIn('dönüş', nelar['gloss_tr'])

        # 2. Vürel is fear (roots:502), NOT crossing
        vürel = lookup('Vürel')[0]
        self.assertEqual(vürel['semantic_anchor_en'], 'fear')
        self.assertIn('korku', vürel['gloss_tr'])

        # 3. Mora is night (roots:455), NOT one
        mora = lookup('Mora')[0]
        self.assertEqual(mora['semantic_anchor_en'], 'night')
        self.assertIn('gece', mora['gloss_tr'])

        # Canonical one is numeral Ena (functions:1100)
        ena = lookup('Ena')[0]
        self.assertEqual(ena['part_of_speech'], 'numeral')
        self.assertEqual(ena['gloss_tr'], 'bir')

        # 4. Dei is day (roots:454), NOT star
        dei = lookup('Dei')[0]
        self.assertEqual(dei['semantic_anchor_en'], 'day')
        self.assertIn('gün', dei['gloss_tr'])

        # Canonical star/celestial body is nüra (roots:497)
        nüra = lookup('Nüra')[0]
        self.assertEqual(nüra['semantic_anchor_en'], 'moon')
        self.assertIn('ay', nüra['gloss_tr'])

        # 5. Nave is city (roots:476), NOT nine
        nave = lookup('Nave')[0]
        self.assertEqual(nave['semantic_anchor_en'], 'city')
        self.assertIn('şehir', nave['gloss_tr'])

        # Canonical nine is numeral Vüni (functions:1108)
        vüni = lookup('Vüni')[0]
        self.assertEqual(vüni['gloss_tr'], 'dokuz')

        # 6. Silev is reading (roots:508), NOT making
        silev = lookup('Silev')[0]
        self.assertEqual(silev['semantic_anchor_en'], 'reading')
        self.assertIn('okuma', silev['gloss_tr'])

        # Canonical making/producing is Jav (roots:447)
        jav = lookup('Jav')[0]
        self.assertIn('yapma', jav['gloss_tr'])

        # 7. Nasel is forest (roots:548), NOT generic place
        nasel = lookup('Nasel')[0]
        self.assertEqual(nasel['semantic_anchor_en'], 'forest')
        self.assertIn('orman', nasel['gloss_tr'])

        # 8. Nivar is learning (roots:721), NOT nightwatch
        nivar = lookup('Nivar')[0]
        self.assertEqual(nivar['semantic_anchor_en'], 'learning')
        self.assertIn('öğrenme', nivar['gloss_tr'])

    def test_canonical_postpositions_and_rejected_invented_suffixes(self):
        # Canonical instrumental postposition is 'se' (functions:1080)
        se = lookup('se')[0]
        self.assertEqual(se['part_of_speech'], 'postposition')
        self.assertIn('araçla', se['gloss_tr'])

        # Canonical ablative postposition is 'fi' (functions:1078)
        fi = lookup('fi')[0]
        self.assertEqual(fi['part_of_speech'], 'postposition')
        self.assertIn('-den/-dan', fi['gloss_tr'])

        # Suffix/particle '-ra' is uncanonical and must not be in registry
        self.assertEqual(lookup('ra'), [])

    def test_pronoun_accusative_forms(self):
        # Standard §4.1/§4.2: vowel-ending stems take -n
        self.assertEqual(object_form('mei'), 'mein')
        self.assertEqual(object_form('sai'), 'sain')
        self.assertEqual(object_form('eli'), 'elin')

        # Erroneous 'Meian' and 'Saian' must fail lookup and fail standard parsing
        self.assertEqual(lookup('Meian'), [])
        self.assertEqual(lookup('Saian'), [])

        ast = parse_alei('Mei naelen ke miraven Saian.', version='1.1.0')
        self.assertEqual(ast.status, 'unknown_lexeme')

    def test_middle_voice_collision_warning(self):
        # Parsing middle voice with 'se' in experimental mode must emit a collision warning
        ast = parse_alei('Vel ne va se nesalen.', version='1.1.0', mode='experimental')
        self.assertEqual(ast.status, 'supported')
        self.assertTrue(any('instrumental postposition' in d.lower() for d in ast.diagnostics))
        self.assertTrue(any('collides with canonical instrumental postposition' in w for w in ast.warnings))

    def test_subjectless_imperative_standard_compliance(self):
        # Standard v1.0 §4.1 explicitly authorizes omitting pronoun in clear imperatives
        ast = parse_alei('Aremen!', version='1.1.0', mode='standard')
        self.assertEqual(ast.status, 'supported')
        self.assertEqual(ast.construction, 'imperative')
        self.assertEqual(ast.speech_act, 'imperative')
        self.assertEqual(ast.subject, 'implied_2nd_person')
        self.assertFalse(ast.is_experimental)


if __name__ == '__main__':
    unittest.main()
