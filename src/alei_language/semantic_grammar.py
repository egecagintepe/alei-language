"""L6 Generative Semantic Grammar Engine for Alei.

Provides structured semantic analysis across 11 core linguistic domains:
1. Argument structure and valency (Agent, Patient, Recipient, Experiencer)
2. Voice modulation (Active, Passive/Middle -il-/vo, Reflexive, Inchoative)
3. Aspectual & Aktionsart distinction (State vs Dynamic Event vs Resultative)
4. Conditionals, Concessives (şe-el), and Counterfactuals (şe da ... da va)
5. Negation scope and quantified expressions (sam, ena, ne sam, ne ena)
6. Relative clauses (Noun + ke + Clause) and Complement clauses (Verb + ke + Prop)
7. Temporal sequencing and discourse connectives (den, pür, orai lo)
8. Comparatives (fi) and Superlatives (sam fi), and Ordinals (-i)
9. Pronoun reference and anaphora (co-referential reflexives, reciprocals)
10. Speech acts (Questions, Imperatives, Reported speech frames)
11. Complex sentence coordination (ve, lia, sira)

Preserves backward compatibility with v1.0 standard while enabling rich generative human expression.
"""
from typing import Dict, List, Any, Optional, Tuple
import re

from .ast import TokenNode, ArgumentRole, PredicateFrame, SentenceAST
from .lexicon import lookup, records, normalize
from .morphology import object_form, plural, analyze
from .valency import get_valency_frame, evaluate_valency, VERB_VALENCY_FRAMES

# Core canonical pronouns and case forms
PRONOUNS_NOM = {'mei', 'sai', 'eli', 'meina', 'saina', 'elina'}
PRONOUNS_ACC = {'mein', 'sain', 'elin', 'meinan', 'sainan', 'elinan'}
DEMONSTRATIVES = {'so'}
POSTPOSITIONS = {'lo', 'ta', 'fi', 'se', 've'}
CONJUNCTIONS = {'ve', 'lia', 'sira', 'şe', 'şe-el', 'den', 'pür'}
ASPECT_MARKERS = {'du', 'fa'}
TENSE_MARKERS = {'da', 'va'}
QUESTION_PARTICLES = {'le'}
FOCUS_PARTICLES = {'el'}

def analyze_l6_sentence(text: str, version: str = '1.1.0') -> SentenceAST:
    """Perform comprehensive generative semantic parsing of an Alei sentence."""
    raw = text.strip()
    punct = raw[-1] if raw and raw[-1] in '.!?' else ''
    clean_text = raw.rstrip('.!?')

    ast = SentenceAST(
        status='supported',
        construction='verbal',
        speech_act='assertion',
        polarity=True,
        tense='unmarked',
        aspect='unmarked',
        mood='indicative',
        raw_text=raw,
        version=version,
        is_experimental=True
    )

    # 1. Detect Direct Quotative / Reported Speech Frame
    if ':' in raw and ('"' in raw or '“' in raw):
        ast.construction = 'quotative'
        ast.speech_act = 'quotation'
        colon_idx = raw.index(':')
        frame_part = raw[:colon_idx].strip()
        quote_part = raw[colon_idx+1:].strip().strip('"“”')

        # Subordinate clause record for quote
        quote_ast = analyze_l6_sentence(quote_part, version=version)
        ast.subordinate_clauses.append({
            'type': 'direct_quotation',
            'quote_text': quote_part,
            'quote_ast': quote_ast.to_dict()
        })
        # Parse the matrix frame (e.g., 'Elina da vesen')
        frame_ast = analyze_l6_sentence(frame_part, version=version)
        ast.subject = frame_ast.subject
        ast.predicate = frame_ast.predicate
        ast.tense = frame_ast.tense
        ast.aspect = frame_ast.aspect
        ast.polarity = frame_ast.polarity
        return ast

    # 2. Extract initial tokens
    tokens_raw = [t.strip(',;') for t in clean_text.split() if t.strip(',;')]

    # Check for Sentence-Final Question Particle 'le'
    if tokens_raw and tokens_raw[-1].lower() == 'le':
        ast.speech_act = 'question'
        tokens_raw = tokens_raw[:-1]

    # 3. Check for Concessive Conditional 'şe-el' or Pure Conditional 'şe'
    is_concessive = False
    is_conditional = False
    matrix_tokens = list(tokens_raw)

    if ',' in clean_text:
        parts = [p.strip() for p in clean_text.split(',', 1)]
        first_tokens = [t.strip(',;') for t in parts[0].split() if t.strip(',;')]
        second_tokens = [t.strip(',;') for t in parts[1].split() if t.strip(',;')]
        if first_tokens and first_tokens[0].lower() in ('şe', 'şe-el'):
            if first_tokens[0].lower() == 'şe-el':
                is_concessive = True
                ast.mood = 'concessive'
            else:
                is_conditional = True
                ast.mood = 'conditional'
            ast.subordinate_clauses.append({
                'type': 'concessive_condition' if is_concessive else 'conditional_antecedent',
                'marker': first_tokens[0],
                'clause_text': parts[0]
            })
            matrix_tokens = second_tokens
    else:
        if matrix_tokens and matrix_tokens[0].lower() == 'şe-el':
            is_concessive = True
            ast.mood = 'concessive'
            matrix_tokens = matrix_tokens[1:]
        elif matrix_tokens and matrix_tokens[0].lower() == 'şe':
            is_conditional = True
            ast.mood = 'conditional'
            matrix_tokens = matrix_tokens[1:]

    # 4. Check for Counterfactual Stacking ('şe da ... da va')
    if is_conditional or is_concessive:
        full_lower = clean_text.lower()
        if ' da va ' in full_lower or full_lower.endswith(' da va') or (' da ' in full_lower and ' va ' in full_lower):
            ast.mood = 'counterfactual'
            ast.diagnostics.append("Compositional counterfactual conditional detected (şe da ... da va).")

    # 5. Check for Relative Clauses with 'ke' modifying a noun head
    # e.g., 'Lera ke da avelen samel ve.'
    tokens_low = [t.lower() for t in matrix_tokens]
    if 'ke' in tokens_low:
        ke_idx = tokens_low.index('ke')
        prev_token = matrix_tokens[ke_idx - 1].lower() if ke_idx > 0 else ''
        frame_prev = get_valency_frame(prev_token)
        # If preceding token is not a verb taking modal complement, this is a post-nominal relative clause
        if not (frame_prev and frame_prev.get('class') in ('modal_transitive', 'modal_auxiliary', 'modal_epistemic', 'communicative')):
            head_noun = matrix_tokens[ke_idx - 1] if ke_idx > 0 else 'unspecified_head'
            rel_tokens = matrix_tokens[ke_idx + 1:]
            rel_clause_str = " ".join(rel_tokens)
            ast.subordinate_clauses.append({
                'type': 'relative_clause',
                'head_noun': head_noun,
                'rel_clause_text': rel_clause_str
            })
            ast.diagnostics.append(f"Post-nominal relative clause modifying '{head_noun}' via 'ke'.")

    # 6. Check for Comparative Constructions with 'fi' (Ablative comparison)
    # e.g., 'Eli süli Mei fi.' or 'Eli lavar süli Mei fi.' or 'Eli süli sam fi.'
    if len(matrix_tokens) >= 3 and matrix_tokens[-1].lower() == 'fi':
        standard_entity = matrix_tokens[-2]
        degree = 'standard'
        if 'lavar' in [t.lower() for t in matrix_tokens]:
            degree = 'intensified_comparative'
        is_superlative = (standard_entity.lower() == 'sam')
        ast.comparative = {
            'is_comparative': True,
            'is_superlative': is_superlative,
            'standard': standard_entity,
            'degree': 'superlative' if is_superlative else degree,
            'marker': 'fi'
        }
        ast.diagnostics.append(f"Comparative construction: standard='{standard_entity}', superlative={is_superlative}.")

    # 7. Check for Quantifier Scope
    # Universal: 'sam', Existential: 'ena', Negative: 'ne sam', 'ne ena'
    first_two = [t.lower() for t in matrix_tokens[:2]]
    if 'ne' in first_two and 'sam' in first_two:
        ast.quantifier_scope = {
            'quantifier': 'sam',
            'scope': 'partial_negation',
            'meaning': 'not all / not every'
        }
        ast.polarity = False
    elif 'sam' in first_two and 'ne' not in first_two:
        ast.quantifier_scope = {
            'quantifier': 'sam',
            'scope': 'universal_affirmative',
            'meaning': 'all / every'
        }
    elif 'ne' in first_two and 'ena' in first_two:
        ast.quantifier_scope = {
            'quantifier': 'ena',
            'scope': 'total_negation',
            'meaning': 'none / not one / nobody'
        }
        ast.polarity = False

    # 8. Check for Discourse Connectives
    for conn in ('den', 'pür', 'lia', 'sira'):
        if conn in [t.lower() for t in matrix_tokens]:
            ast.discourse_connectives.append(conn)

    # 9. Main Clause Verbal / Predicate Parsing
    _parse_main_clause_features(matrix_tokens, ast, version)

    # 10. Check for Imperative Speech Act
    if punct == '!':
        subj_str = str(ast.subject or '').lower()
        if subj_str in ('', 'none', 'implied_2nd_person', 'sai', 'saina'):
            ast.speech_act = 'imperative'
            ast.construction = 'imperative'
            if not ast.subject:
                ast.subject = 'implied_2nd_person'

    return ast

def _parse_main_clause_features(tokens: List[str], ast: SentenceAST, version: str) -> None:
    """Extract Subject, Tense, Aspect, Polarity, Voice, Verb, and Object Arguments."""
    if not tokens:
        ast.status = 'unsupported'
        return

    # Check for negation 'ne'
    toks_lower = [t.lower() for t in tokens]
    if 'ne' in toks_lower:
        ast.polarity = False

    # Check for Tense
    if 'da' in toks_lower:
        ast.tense = 'past'
    elif 'va' in toks_lower:
        ast.tense = 'future'
    else:
        ast.tense = 'unmarked'

    # Check for Aspect
    if 'du' in toks_lower:
        ast.aspect = 'progressive'
    elif 'fa' in toks_lower:
        ast.aspect = 'completed'

    # Extract Subject candidate (first nominal token)
    subject_candidate = None
    for tok in tokens:
        t_low = tok.lower()
        if t_low in PRONOUNS_NOM or (not t_low.endswith(('en', 'an', 'in', 'on', 'ön', 'un', 'ün')) and t_low not in POSTPOSITIONS and t_low not in ('da', 'va', 'ne', 'du', 'fa', 'vo', 'şe', 'şe-el')):
            subject_candidate = tok
            break

    sub_lower = subject_candidate.lower() if subject_candidate else ''

    # Detect Voice:
    # 1. Passive / Middle with infix -il-: e.g., 'falilen', 'nesalilen'
    # 2. Middle with particle 'vo': e.g., 'vo falen'
    # 3. Reflexive: overt object pronoun matching subject (e.g. Mei ... mein)
    # 4. Inchoative: periphrastic 'avelen fali'
    voice = 'active'
    verb_lemma = None
    target_verb_token = None

    for i, tok in enumerate(tokens):
        t_low = tok.lower()
        # Infix -il- passive detection
        m_il = re.match(r'^([a-zıiöü]+)il(en)$', t_low)
        if m_il:
            stem = m_il.group(1)
            verb_lemma = stem + 'en'
            target_verb_token = tok
            voice = 'passive'
            ast.diagnostics.append(f"Passive voice detected via regular infix '-il-': '{tok}' -> lemma '{verb_lemma}'.")
            break

        # Suffix -en canonical verb
        if t_low.endswith('en') and t_low not in POSTPOSITIONS:
            verb_lemma = t_low
            target_verb_token = tok

            # Check if preceded by middle particle 'vo'
            if i > 0 and tokens[i-1].lower() == 'vo':
                voice = 'middle'
                ast.diagnostics.append(f"Middle voice detected via analytic particle 'vo': 'vo {tok}'.")
            break

    # Check for Inchoative Periphrasis ('avelen fali')
    if verb_lemma == 'avelen':
        for tok in tokens:
            if tok.lower().endswith('i') and tok.lower() not in ('mei', 'sai', 'eli'):
                voice = 'inchoative'
                ast.diagnostics.append(f"Inchoative state-transition periphrasis detected: 'avelen {tok}'.")
                break

    # Determine Arguments and Valency
    overt_roles: Dict[str, str] = {}
    predicate_arguments: List[ArgumentRole] = []

    # Subject assignment
    if subject_candidate:
        ast.subject = subject_candidate
        subj_role = 'Agent'
        if voice in ('passive', 'middle'):
            subj_role = 'Patient'
        overt_roles[subj_role] = subject_candidate
        predicate_arguments.append(ArgumentRole(role=subj_role, value=subject_candidate, is_overt=True))

    # Recipient / Goal assignment with 'ta'
    recip_candidate = None
    frame = get_valency_frame(verb_lemma) if verb_lemma else None
    for i, tok in enumerate(tokens):
        if tok.lower() == 'ta' and i > 0:
            recip_candidate = tokens[i-1]
            if frame and 'Destination' in frame.get('roles', []):
                overt_roles['Destination'] = recip_candidate
                predicate_arguments.append(ArgumentRole(role='Destination', value=recip_candidate, is_overt=True))
            else:
                overt_roles['Recipient'] = recip_candidate
                predicate_arguments.append(ArgumentRole(role='Recipient', value=recip_candidate, is_overt=True))

    # Location assignment with 'lo'
    for i, tok in enumerate(tokens):
        if tok.lower() == 'lo' and i > 0:
            loc = tokens[i-1]
            overt_roles['Location'] = loc
            predicate_arguments.append(ArgumentRole(role='Location', value=loc, is_overt=True))

    # Object / Patient assignment
    for i, tok in enumerate(tokens):
        t_low = tok.lower()
        if i + 1 < len(tokens) and tokens[i+1].lower() == 'ta':
            continue
        if tok == recip_candidate:
            continue
        if t_low in PRONOUNS_ACC or (t_low.endswith(('an', 'en', 'in', 'on', 'ön', 'un', 'ün')) and not t_low.endswith(('len', 'ren', 'sen', 'ven', 'men')) and tok != subject_candidate):
            # Check for Reflexive co-reference: Subject and Object share person/number
            if (sub_lower == 'mei' and t_low == 'mein') or \
               (sub_lower == 'sai' and t_low == 'sain') or \
               (sub_lower == 'eli' and t_low == 'elin') or \
               (sub_lower == 'meina' and t_low == 'meinan') or \
               (sub_lower == 'saina' and t_low == 'sainan') or \
               (sub_lower == 'elina' and t_low == 'elinan'):
                voice = 'reflexive'
                ast.diagnostics.append(f"Reflexive voice detected: Subject '{subject_candidate}' and Object '{tok}' are co-referential.")

            overt_roles['Patient'] = tok
            predicate_arguments.append(ArgumentRole(role='Patient', value=tok, is_overt=True))

    if verb_lemma:
        val_eval = evaluate_valency(verb_lemma, overt_roles, voice=voice)
        pred_frame = PredicateFrame(
            verb_lemma=verb_lemma,
            verb_token=TokenNode(surface=target_verb_token or verb_lemma, normalized=verb_lemma),
            voice=voice,
            valency_class=val_eval.get('frame_class', 'transitive'),
            arguments=predicate_arguments,
            valency_satisfied=val_eval.get('valency_satisfied', True),
            valency_notes=val_eval.get('notes', [])
        )
        ast.predicate = pred_frame

        if not val_eval.get('valency_satisfied', True):
            ast.diagnostics.extend(val_eval.get('notes', []))
            if val_eval.get('status') == 'valency_clash':
                ast.status = 'ambiguous'
                ast.ambiguities.append({
                    'type': 'valency_clash',
                    'detail': f"Verb '{verb_lemma}' lacks obligatory patient in active voice; subject may be intended as patient."
                })
    else:
        # Check for nominal / quality predicate
        # e.g., 'Lüra fali.' or 'Mei süli.'
        for tok in tokens:
            t_low = tok.lower()
            if t_low.endswith('i') and t_low not in PRONOUNS_NOM and t_low not in POSTPOSITIONS:
                ast.construction = 'nominal_predicate'
                pred_frame = PredicateFrame(
                    verb_lemma=t_low,
                    verb_token=TokenNode(surface=tok, normalized=t_low),
                    voice='active',
                    valency_class='copular',
                    arguments=[ArgumentRole(role='Theme', value=ast.subject, is_overt=True)],
                    valency_satisfied=True
                )
                ast.predicate = pred_frame
                break
