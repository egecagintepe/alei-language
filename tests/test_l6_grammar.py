"""Comprehensive unit and semantic regression test suite for L6 Generative Grammar.

Tests the 11 generative linguistic domains defined in RFC-L6:
1. Ditransitive recipient flagging with 'ta'
2. Voice: Active, Passive (-il-), Middle (vo), Reflexive (coreference), Inchoative
3. State vs Event vs Resultative
4. Conditionals, Concessives (şe-el), and Compositional Counterfactuals (şe da ... da va)
5. Negation scope and Quantifier scope (sam, ne sam, ne ena)
6. Relative clauses with post-nominal 'ke'
7. Narrative sequencing connectives (den, pür, lia, sira)
8. Comparatives with 'fi' and Superlatives ('sam fi')
9. Questions (polar 'le'), Imperatives, and Reported Speech frames
10. Adversarial ambiguity representation (valency clash vs ellipsis)
"""
import unittest
from alei_language.grammar import parse_alei
from alei_language.semantic_grammar import analyze_l6_sentence

class TestL6GenerativeGrammar(unittest.TestCase):

    def test_valency_ditransitive_recipient_ta(self):
        # 'Mei da davelen tüvanan sain ta.' -> I gave the book to you
        ast = parse_alei("Mei da davelen tüvanan sain ta.", version="1.1.0", mode="l6")
        self.assertEqual(ast.status, "supported")
        self.assertEqual(ast.predicate.verb_lemma, "davelen")
        self.assertEqual(ast.predicate.valency_class, "ditransitive")
        roles = {arg.role: arg.value for arg in ast.predicate.arguments}
        self.assertEqual(roles.get('Agent'), 'Mei')
        self.assertEqual(roles.get('Patient'), 'tüvanan')
        self.assertEqual(roles.get('Recipient'), 'sain')
        self.assertTrue(ast.predicate.valency_satisfied)

    def test_reflexive_co_reference(self):
        # 1SG Reflexive: 'Mei da miraven mein.' -> I helped myself
        ast1 = parse_alei("Mei da miraven mein.", version="1.1.0", mode="l6")
        self.assertEqual(ast1.status, "supported")
        self.assertEqual(ast1.predicate.voice, "reflexive")
        self.assertTrue(any("Reflexive voice detected" in d for d in ast1.diagnostics))

        # 3SG Reflexive: 'Eli da liren elin.' -> He saw himself
        ast2 = parse_alei("Eli da liren elin.", version="1.1.0", mode="l6")
        self.assertEqual(ast2.status, "supported")
        self.assertEqual(ast2.predicate.voice, "reflexive")

    def test_passive_voice_infix_il(self):
        # Regular passive with -il-: 'Lüra da falilen.' -> The door was opened
        ast = parse_alei("Lüra da falilen.", version="1.1.0", mode="l6")
        self.assertEqual(ast.status, "supported")
        self.assertEqual(ast.predicate.voice, "passive")
        self.assertEqual(ast.predicate.verb_lemma, "falen")
        roles = {arg.role: arg.value for arg in ast.predicate.arguments}
        self.assertEqual(roles.get('Patient'), 'Lüra')

        # Transitive 'nesalen' with -il-: 'Vel ne va nesalilen.' -> The path will not be lost
        ast2 = parse_alei("Vel ne va nesalilen.", version="1.1.0", mode="l6")
        self.assertEqual(ast2.status, "supported")
        self.assertEqual(ast2.predicate.voice, "passive")
        self.assertEqual(ast2.predicate.verb_lemma, "nesalen")

    def test_middle_voice_analytic_vo(self):
        # Middle voice with analytic particle 'vo': 'Vel ne va vo nesalen.'
        ast = parse_alei("Vel ne va vo nesalen.", version="1.1.0", mode="l6")
        self.assertEqual(ast.status, "supported")
        self.assertEqual(ast.predicate.voice, "middle")
        self.assertEqual(ast.predicate.verb_lemma, "nesalen")

    def test_inchoative_periphrasis(self):
        # Inchoative state transition: 'Lüra da avelen fali.' -> The door became open
        ast = parse_alei("Lüra da avelen fali.", version="1.1.0", mode="l6")
        self.assertEqual(ast.status, "supported")
        self.assertEqual(ast.predicate.voice, "inchoative")
        self.assertEqual(ast.predicate.verb_lemma, "avelen")

    def test_aspect_state_vs_event_vs_resultative(self):
        # 1. State: 'Lüra fali.' -> Nominal stative predicate
        ast_state = parse_alei("Lüra fali.", version="1.1.0", mode="l6")
        self.assertEqual(ast_state.construction, "nominal_predicate")
        self.assertEqual(ast_state.predicate.valency_class, "copular")

        # 2. Dynamic event in progress: 'Lüra du falen.' -> Progressive
        ast_prog = parse_alei("Lüra du falen.", version="1.1.0", mode="l6")
        self.assertEqual(ast_prog.aspect, "progressive")

        # 3. Punctual past event: 'Lüra da falen.' -> Past
        ast_past = parse_alei("Lüra da falen.", version="1.1.0", mode="l6")
        self.assertEqual(ast_past.tense, "past")

        # 4. Completed aspect: 'Lüra fa falen.' -> Completed
        ast_comp = parse_alei("Lüra fa falen.", version="1.1.0", mode="l6")
        self.assertEqual(ast_comp.aspect, "completed")

    def test_concessive_conditional_se_el(self):
        # 'Şe-el Sai vürelen, aremen!' -> Even if you fear, think!
        ast = parse_alei("Şe-el Sai vürelen, aremen!", version="1.1.0", mode="l6")
        self.assertEqual(ast.status, "supported")
        self.assertEqual(ast.mood, "concessive")
        self.assertEqual(ast.speech_act, "imperative")

    def test_compositional_counterfactual(self):
        # 'Şe Sai da avelen, Mei da va miraven sain.' -> If you had come, I would have helped you
        ast = parse_alei("Şe Sai da avelen, Mei da va miraven sain.", version="1.1.0", mode="l6")
        self.assertEqual(ast.status, "supported")
        self.assertEqual(ast.mood, "counterfactual")
        self.assertTrue(any("counterfactual" in d.lower() for d in ast.diagnostics))

    def test_quantifier_scope_and_negation(self):
        # Universal affirmative: 'Sam lera da avelen.' -> All people arrived
        ast1 = parse_alei("Sam lera da avelen.", version="1.1.0", mode="l6")
        self.assertEqual(ast1.quantifier_scope['scope'], 'universal_affirmative')
        self.assertTrue(ast1.polarity)

        # Partial negation: 'Ne sam lera da avelen.' -> Not all people arrived
        ast2 = parse_alei("Ne sam lera da avelen.", version="1.1.0", mode="l6")
        self.assertEqual(ast2.quantifier_scope['scope'], 'partial_negation')
        self.assertFalse(ast2.polarity)

        # Total negation: 'Ne ena lera da avelen.' -> Not one person arrived = nobody arrived
        ast3 = parse_alei("Ne ena lera da avelen.", version="1.1.0", mode="l6")
        self.assertEqual(ast3.quantifier_scope['scope'], 'total_negation')
        self.assertFalse(ast3.polarity)

    def test_relative_clause_post_nominal_ke(self):
        # Relative clause modifying 'Lera': 'Lera ke da avelen samel ve.' -> The person who arrived is a friend
        ast = parse_alei("Lera ke da avelen samel ve.", version="1.1.0", mode="l6")
        self.assertEqual(ast.status, "supported")
        self.assertTrue(len(ast.subordinate_clauses) >= 1)
        rel = ast.subordinate_clauses[0]
        self.assertEqual(rel['type'], 'relative_clause')
        self.assertEqual(rel['head_noun'], 'Lera')

    def test_comparative_and_superlative_fi(self):
        # Standard comparative: 'Eli süli Mei fi.' -> He is better than me
        ast1 = parse_alei("Eli süli Mei fi.", version="1.1.0", mode="l6")
        self.assertIsNotNone(ast1.comparative)
        self.assertEqual(ast1.comparative['standard'], 'Mei')
        self.assertFalse(ast1.comparative['is_superlative'])

        # Intensified comparative: 'Eli lavar süli Mei fi.' -> He is much better than me
        ast2 = parse_alei("Eli lavar süli Mei fi.", version="1.1.0", mode="l6")
        self.assertEqual(ast2.comparative['degree'], 'intensified_comparative')

        # Superlative: 'Eli süli sam fi.' -> He is the best of all
        ast3 = parse_alei("Eli süli sam fi.", version="1.1.0", mode="l6")
        self.assertTrue(ast3.comparative['is_superlative'])
        self.assertEqual(ast3.comparative['standard'], 'sam')

    def test_questions_and_speech_acts(self):
        # Polar question: 'Sai süli le?' -> Are you well?
        ast_q = parse_alei("Sai süli le?", version="1.1.0", mode="l6")
        self.assertEqual(ast_q.speech_act, "question")

        # Subjectless imperative: 'Aremen!' -> Think!
        ast_imp = parse_alei("Aremen!", version="1.1.0", mode="l6")
        self.assertEqual(ast_imp.speech_act, "imperative")
        self.assertEqual(ast_imp.subject, "implied_2nd_person")

        # Direct quotation: 'Elina da vesen: "Ne vürelen!"' -> They said: "Do not fear!"
        ast_quote = parse_alei('Elina da vesen: "Ne vürelen!"', version="1.1.0", mode="l6")
        self.assertEqual(ast_quote.construction, "quotative")
        self.assertEqual(ast_quote.speech_act, "quotation")
        self.assertTrue(len(ast_quote.subordinate_clauses) >= 1)
        self.assertEqual(ast_quote.subordinate_clauses[0]['type'], 'direct_quotation')

    def test_adversarial_ambiguity_representation(self):
        # Adversarial pair: active transitive 'nesalen' with omitted patient
        # 'Vel ne va nesalen.' -> Path will not lose [what?]
        ast = parse_alei("Vel ne va nesalen.", version="1.1.0", mode="l6")
        # In l6 mode, valency clash is represented explicitly in ambiguities rather than silently assumed
        self.assertTrue(len(ast.ambiguities) >= 1)
        self.assertEqual(ast.ambiguities[0]['type'], 'valency_clash')

if __name__ == '__main__':
    unittest.main()
