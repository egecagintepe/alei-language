"""Comprehensive unit, semantic regression, and adversarial test suite for L6.1 Generative Grammar.

Tests the hardened structure-aware semantic parser across all required failure classes and linguistic domains:
1. Lexical grounding and rejection of unknown words (invented subject, verb, adjective).
2. Valency satisfaction and rejection of spurious arguments on intransitive verbs.
3. Proper Experiencer/Stimulus semantic role mapping on perceptual/experiential verbs.
4. Voice distinctions: Passive (-il-), Middle (vo), Inchoative, Reflexive, and rejection of unlicensed passives.
5. Canonical comparisons with 'peli' and 'nera' vs ablative 'fi'.
6. Coordination with canonical 'ya' vs rejection of comitative 've' as conjunction.
7. Disambiguation of 'ke': Subject Relative vs Object Relative vs Verb Complement Clause.
8. Counterfactual conditionals ('şe da ... da va') vs standalone Future-in-the-Past ('da va').
9. Mathematical quantification: Universal, Partial Negation (NOT ALL), and Total Negation (NONE).
10. Strict isolation: Experimental constructs rejected in standard mode.
"""
import unittest
from alei_language.grammar import parse_alei


class TestL61HardenedGrammar(unittest.TestCase):

    # -------------------------------------------------------------
    # Domain 1: Lexical Grounding and Rejection of Invented Words
    # -------------------------------------------------------------
    def test_rejection_of_invented_subject_and_verb(self):
        # Invented subject 'Xyza' + invented verb 'blabla'
        ast = parse_alei("Xyza da blabla.", version="1.1.0", mode="l6")
        self.assertEqual(ast.status, "unknown_lexeme")
        self.assertTrue(any("Xyza" in d or "blabla" in d for d in ast.diagnostics))

    def test_rejection_of_fake_adjective_ending_in_i(self):
        # 'fakei' is not an attested quality or legal derivation
        ast = parse_alei("Lüra fakei.", version="1.1.0", mode="l6")
        self.assertEqual(ast.status, "unknown_lexeme")

    def test_rejection_of_fake_verb_ending_in_en(self):
        # 'fakeen' is not an attested verb
        ast = parse_alei("Mei da fakeen.", version="1.1.0", mode="l6")
        self.assertEqual(ast.status, "unknown_lexeme")

    # -------------------------------------------------------------
    # Domain 2: Valency & Spurious Arguments on Intransitive Verbs
    # -------------------------------------------------------------
    def test_rejection_of_spurious_patient_on_posture_verb(self):
        # 'şürelen' is an intransitive posture verb; adding an accusative patient must fail
        ast = parse_alei("Eli da şürelen lüran.", version="1.1.0", mode="l6")
        self.assertEqual(ast.status, "unsupported")
        self.assertFalse(ast.predicate.valency_satisfied)
        self.assertTrue(any("Unexpected argument role(s)" in n for n in ast.predicate.valency_notes))

    def test_rejection_of_spurious_patient_on_motion_verb(self):
        # 'avelen' is an intransitive motion verb; taking an accusative patient must fail
        ast = parse_alei("Mei da avelen tüvanan.", version="1.1.0", mode="l6")
        self.assertEqual(ast.status, "unsupported")
        self.assertFalse(ast.predicate.valency_satisfied)

    def test_missing_obligatory_patient_on_transitive_verb(self):
        # 'nesalen' is strictly transitive; omitted patient causes valency defect
        ast = parse_alei("Vel ne va nesalen.", version="1.1.0", mode="l6")
        self.assertNotEqual(ast.status, "supported")
        self.assertEqual(ast.status, "ambiguous")
        self.assertTrue(len(ast.ambiguities) >= 1)
        self.assertEqual(ast.ambiguities[0]['type'], 'valency_clash')

    # -------------------------------------------------------------
    # Domain 3: Perceptual and Experiential Verbs (Experiencer/Stimulus)
    # -------------------------------------------------------------
    def test_perceptual_verb_experiencer_stimulus_mapping(self):
        # 'liren' is perceptual: Experiencer = Eli, Stimulus = lüran
        ast = parse_alei("Eli da liren lüran.", version="1.1.0", mode="l6")
        self.assertEqual(ast.status, "supported")
        roles = {arg.role: arg.value for arg in ast.predicate.arguments}
        self.assertEqual(roles.get('Experiencer'), 'Eli')
        self.assertEqual(roles.get('Stimulus'), 'lüran')

    def test_experiential_verb_vurelen(self):
        # 'vürelen' is experiential: Experiencer = Mei, Stimulus = moran
        ast = parse_alei("Mei du vürelen moran.", version="1.1.0", mode="l6")
        self.assertEqual(ast.status, "supported")
        roles = {arg.role: arg.value for arg in ast.predicate.arguments}
        self.assertEqual(roles.get('Experiencer'), 'Mei')
        self.assertEqual(roles.get('Stimulus'), 'moran')

    # -------------------------------------------------------------
    # Domain 4: Voice Modulation and Unlicensed Passive Derivations
    # -------------------------------------------------------------
    def test_passive_voice_infix_il(self):
        # 'Lüra da falilen.' -> Patient promoted to subject
        ast = parse_alei("Lüra da falilen.", version="1.1.0", mode="l6")
        self.assertEqual(ast.status, "supported")
        self.assertEqual(ast.predicate.voice, "passive")
        self.assertEqual(ast.predicate.verb_lemma, "falen")
        roles = {arg.role: arg.value for arg in ast.predicate.arguments}
        self.assertEqual(roles.get('Patient'), 'Lüra')

    def test_middle_voice_analytic_vo(self):
        # 'Vel ne va vo nesalen.' -> Patient promoted to subject via middle particle 'vo'
        ast = parse_alei("Vel ne va vo nesalen.", version="1.1.0", mode="l6")
        self.assertEqual(ast.status, "supported")
        self.assertEqual(ast.predicate.voice, "middle")
        self.assertEqual(ast.predicate.verb_lemma, "nesalen")

    def test_reflexive_co_reference(self):
        # 'Mei da miraven mein.' -> 1SG subject co-referential with 1SG accusative object
        ast1 = parse_alei("Mei da miraven mein.", version="1.1.0", mode="l6")
        self.assertEqual(ast1.status, "supported")
        self.assertEqual(ast1.predicate.voice, "reflexive")

        # 'Eli da liren elin.' -> 3SG subject co-referential with 3SG accusative object
        ast2 = parse_alei("Eli da liren elin.", version="1.1.0", mode="l6")
        self.assertEqual(ast2.status, "supported")
        self.assertEqual(ast2.predicate.voice, "reflexive")

    def test_inchoative_periphrasis(self):
        # 'Lüra da avelen fali.' -> inchoative state change (door became open)
        ast = parse_alei("Lüra da avelen fali.", version="1.1.0", mode="l6")
        self.assertEqual(ast.status, "supported")
        self.assertEqual(ast.predicate.voice, "inchoative")
        self.assertEqual(ast.predicate.verb_lemma, "avelen")

    def test_rejection_of_unlicensed_passive_on_intransitive_verb(self):
        # 'şürelen' is intransitive; '-il-' passive must be rejected
        ast = parse_alei("Lüra da şürelilen.", version="1.1.0", mode="l6")
        self.assertEqual(ast.status, "unknown_lexeme")

    def test_rejection_of_unlicensed_passive_on_unknown_stem(self):
        # 'fakilen' has unknown base 'faken'
        ast = parse_alei("Lüra da fakilen.", version="1.1.0", mode="l6")
        self.assertEqual(ast.status, "unknown_lexeme")

    # -------------------------------------------------------------
    # Domain 5: Canonical Comparisons ('peli' ... 'nera')
    # -------------------------------------------------------------
    def test_canonical_comparison_peli_and_nera(self):
        # Full comparative: 'Eli peli süli Mei nera.' (He is better compared with me)
        ast1 = parse_alei("Eli peli süli Mei nera.", version="1.1.0", mode="l6")
        self.assertEqual(ast1.status, "supported")
        self.assertIsNotNone(ast1.comparative)
        self.assertEqual(ast1.comparative['marker'], 'peli')
        self.assertEqual(ast1.comparative['quality'], 'süli')
        self.assertEqual(ast1.comparative['standard'], 'Mei')
        self.assertEqual(ast1.comparative['standard_marker'], 'nera')

        # Complex attested example (§4.9): 'Mei ri lem peli lavari Sai ri lem nera.'
        ast2 = parse_alei("Mei ri lem peli lavari Sai ri lem nera.", version="1.1.0", mode="l6")
        self.assertEqual(ast2.status, "supported")
        self.assertEqual(ast2.comparative['quality'], 'lavari')
        self.assertEqual(ast2.comparative['standard'], 'Sai ri lem')

        # Short comparative: 'Eli peli süli.'
        ast3 = parse_alei("Eli peli süli.", version="1.1.0", mode="l6")
        self.assertEqual(ast3.status, "supported")
        self.assertEqual(ast3.comparative['quality'], 'süli')
        self.assertIsNone(ast3.comparative['standard'])

    # -------------------------------------------------------------
    # Domain 6: Clause Coordination ('ya') vs Rejection of 've'
    # -------------------------------------------------------------
    def test_canonical_clause_coordination_with_ya(self):
        # Two independent clauses conjoined by canonical 'ya'
        ast = parse_alei("Mei da lümalen lüran ya Sai da falen elin.", version="1.1.0", mode="l6")
        self.assertEqual(ast.status, "supported")
        self.assertEqual(ast.construction, "coordinate_sentence")
        self.assertEqual(len(ast.coordinate_clauses), 2)
        # Verify independent clauses maintain their own subjects and verbs
        c1 = ast.coordinate_clauses[0]
        c2 = ast.coordinate_clauses[1]
        self.assertEqual(c1['subject'], 'Mei')
        self.assertEqual(c1['predicate']['verb_lemma'], 'lümalen')
        self.assertEqual(c2['subject'], 'Sai')
        self.assertEqual(c2['predicate']['verb_lemma'], 'falen')

    def test_rejection_of_ve_as_conjunction(self):
        # 've' is comitative ('with/together'), NOT an additive conjunction
        ast = parse_alei("Lera da avelen ve Mei da liren elin.", version="1.1.0", mode="l6")
        self.assertEqual(ast.status, "unsupported")
        self.assertTrue(any("comitative postposition" in d for d in ast.diagnostics))

    # -------------------------------------------------------------
    # Domain 7: Subordinate Clauses with 'ke' Disambiguation
    # -------------------------------------------------------------
    def test_subject_relative_clause_with_ke(self):
        # 'Lera ke sileven tüvanan da avelen.' -> Head 'Lera' is Agent of 'sileven'
        ast = parse_alei("Lera ke sileven tüvanan da avelen.", version="1.1.0", mode="l6")
        self.assertEqual(ast.status, "supported")
        self.assertTrue(len(ast.subordinate_clauses) >= 1)
        rel = ast.subordinate_clauses[0]
        self.assertEqual(rel['type'], 'subject_relative_clause')
        self.assertEqual(rel['head_noun'], 'Lera')
        self.assertEqual(rel['embedded_role'], 'Agent')

    def test_object_relative_clause_with_ke(self):
        # 'Tüvan ke lera sileven fali.' -> Head 'Tüvan' is Patient of embedded clause
        ast = parse_alei("Tüvan ke lera sileven fali.", version="1.1.0", mode="l6")
        self.assertEqual(ast.status, "supported")
        self.assertTrue(len(ast.subordinate_clauses) >= 1)
        rel = ast.subordinate_clauses[0]
        self.assertEqual(rel['type'], 'object_relative_clause')
        self.assertEqual(rel['head_noun'], 'Tüvan')
        self.assertEqual(rel['embedded_role'], 'Patient')

    def test_verb_complement_clause_with_ke(self):
        # 'Eli da vesen ke tüvan süli.' -> Preceded by communicative verb 'vesen'
        ast = parse_alei("Eli da vesen ke tüvan süli.", version="1.1.0", mode="l6")
        self.assertEqual(ast.status, "supported")
        self.assertEqual(ast.construction, "embedded_clause")
        self.assertEqual(ast.subordinate_clauses[0]['type'], 'complement_clause')
        self.assertEqual(ast.subordinate_clauses[0]['matrix_verb'], 'vesen')

    # -------------------------------------------------------------
    # Domain 8: TAM, Future-in-the-Past vs Counterfactuals
    # -------------------------------------------------------------
    def test_future_in_the_past_standalone_da_va(self):
        # Standalone 'da va' without conditional antecedent is future-in-the-past / unfulfilled intention
        ast = parse_alei("Mei da va avelen.", version="1.1.0", mode="l6")
        self.assertEqual(ast.status, "supported")
        self.assertEqual(ast.tense, "future_in_past")
        self.assertEqual(ast.mood, "indicative")
        self.assertNotEqual(ast.mood, "counterfactual")

    def test_compositional_counterfactual_with_se_condition(self):
        # 'Şe Sai da avelen, Mei da va miraven sain.' -> Conditional past antecedent + da va consequent
        ast = parse_alei("Şe Sai da avelen, Mei da va miraven sain.", version="1.1.0", mode="l6")
        self.assertEqual(ast.status, "supported")
        self.assertEqual(ast.mood, "counterfactual")
        self.assertTrue(any("counterfactual" in d.lower() for d in ast.diagnostics))

    def test_concessive_conditional_se_el(self):
        # 'Şe-el Sai vürelen, aremen!' -> Concessive mood + Imperative speech act
        ast = parse_alei("Şe-el Sai vürelen, aremen!", version="1.1.0", mode="l6")
        self.assertEqual(ast.status, "supported")
        self.assertEqual(ast.mood, "concessive")
        self.assertEqual(ast.speech_act, "imperative")

    # -------------------------------------------------------------
    # Domain 9: Quantification Logic
    # -------------------------------------------------------------
    def test_quantifier_scope_universal_and_negations(self):
        # Universal Affirmative (experimental quantifier 'sam')
        ast1 = parse_alei("Sam lera da avelen.", version="1.1.0", mode="l6")
        self.assertEqual(ast1.quantifier_scope['scope'], 'universal_affirmative')
        self.assertTrue(ast1.polarity)

        # Partial Negation: 'Ne sam lera da avelen.' (Not all people arrived)
        # Mathematical note: ¬∀x does not imply ∃x
        ast2 = parse_alei("Ne sam lera da avelen.", version="1.1.0", mode="l6")
        self.assertEqual(ast2.quantifier_scope['scope'], 'partial_negation')
        self.assertFalse(ast2.polarity)

        # Total Negation: 'Ne ena lera da avelen.' (None / not one person arrived)
        ast3 = parse_alei("Ne ena lera da avelen.", version="1.1.0", mode="l6")
        self.assertEqual(ast3.quantifier_scope['scope'], 'total_negation')
        self.assertFalse(ast3.polarity)

    # -------------------------------------------------------------
    # Domain 10: Ditransitive Valency with Recipient 'ta'
    # -------------------------------------------------------------
    def test_valency_ditransitive_recipient_ta(self):
        # 'Mei da davelen tüvanan sain ta.' -> I gave the book to you
        ast = parse_alei("Mei da davelen tüvanan sain ta.", version="1.1.0", mode="l6")
        self.assertEqual(ast.status, "supported")
        self.assertEqual(ast.predicate.verb_lemma, "davelen")
        roles = {arg.role: arg.value for arg in ast.predicate.arguments}
        self.assertEqual(roles.get('Agent'), 'Mei')
        self.assertEqual(roles.get('Patient'), 'tüvanan')
        self.assertEqual(roles.get('Recipient'), 'sain')
        self.assertTrue(ast.predicate.valency_satisfied)

    # -------------------------------------------------------------
    # Domain 11: Standard Mode Strict Isolation
    # -------------------------------------------------------------
    def test_experimental_constructs_rejected_in_standard_mode(self):
        # Middle voice 'vo' must not be recognized in mode='standard'
        ast = parse_alei("Vel ne va vo nesalen.", version="1.1.0", mode="standard")
        self.assertNotEqual(ast.status, "supported")

        # Passive infix '-il-' must not be recognized in mode='standard'
        ast2 = parse_alei("Lüra da falilen.", version="1.1.0", mode="standard")
        self.assertNotEqual(ast2.status, "supported")


if __name__ == '__main__':
    unittest.main()
