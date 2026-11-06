"""L6.1 Generative Semantic Grammar Engine for Alei.

Provides structure-aware, lexicon-grounded semantic analysis:
1. Strict token-level lexical validation against canonical registries and licensed L6 derivations.
2. Argument structure and valency verification with semantic roles:
   - Agent, Patient, Experiencer, Stimulus, Recipient, Destination, Theme, Proposition.
3. Voice distinctions:
   - Active, Passive (-il- on transitive verbs), Middle (analytic 'vo'), Reflexive (co-referential pronoun), Inchoative ('avelen' + stative quality).
4. Aspectual & Aktionsart distinction:
   - Stative zero-copula, Progressive ('du'), Completed ('fa'), Past ('da'), Future ('va').
5. Conditionals, Concessives ('şe-el'), and Counterfactuals ('şe da ... da va') vs standalone Future-in-the-Past ('da va').
6. Canonical comparisons ('peli' ... 'nera') vs non-canonical ablative ('fi').
7. Clause coordination with canonical 'ya' (with independent tenses and polarity) and rejection of 've' as conjunction.
8. Subordinate clauses with 'ke': explicit disambiguation between Complement Clauses, Subject Relatives, and Object Relatives.
9. Mathematical quantification: Universal Affirmative, Partial Negation (NOT ALL), and Total Negation (NONE).

Preserves strict backward compatibility with v1.0 standard and v1.1 owner decisions.
"""
from typing import Dict, List, Any, Optional, Tuple, Set
import re

from .ast import TokenNode, ArgumentRole, PredicateFrame, SentenceAST
from .lexicon import lookup, records, normalize
from .morphology import object_form, plural, analyze
from .valency import get_valency_frame, evaluate_valency, VERB_VALENCY_FRAMES
from .orthography import VOWELS, CONSONANTS

# Core canonical sets
PRONOUNS_NOM = {'mei', 'sai', 'eli', 'meina', 'saina', 'elina', 'elar', 'elarna'}
PRONOUNS_ACC = {'mein', 'sain', 'elin', 'meinan', 'sainan', 'elinan'}
CANONICAL_POSTPOSITIONS = {'lo', 'ta', 'fi', 've', 'se', 'ri'}
CANONICAL_CONJUNCTIONS = {'ya', 'lia', 'sira', 'şe'}
CANONICAL_TAM = {'da', 'va', 'du', 'fa', 'su', 'ne'}
CANONICAL_QUESTION = {'le'}
CANONICAL_FOCUS = {'el'}
CANONICAL_COMPARATIVES = {'peli', 'nera'}
CANONICAL_QUANTITY = {'mi'}
CANONICAL_INTERROGATIVES = {'vena', 'miva', 'keli', 'orai', 'vela', 'hiva', 'vera'}
CANONICAL_COMPLEMENTIZER = {'ke'}
CANONICAL_NUMERALS = {
    'ena', 'davi', 'teli', 'pora', 'lume', 'şari', 'növi', 'kema', 'vüni',
    'des', 'hade', 'mavi', 'zui', 'pada'
}
CANONICAL_INTERJECTIONS = {'alei', 'elai', 'lanei', 'varei', 'sürai', 'ei', 'nai'}
CANONICAL_POLITENESS = {'şira'}

# Explicitly labeled L6 experimental items
L6_EXPERIMENTAL_CONJUNCTIONS = {'şe-el'}
L6_EXPERIMENTAL_PARTICLES = {'vo'}
L6_EXPERIMENTAL_QUANTIFIERS = {'sam'}  # Unadopted universal quantifier proposal


def validate_token(tok: str, version: str = '1.1.0', mode: str = 'l6') -> Tuple[bool, str, Dict[str, Any]]:
    """Validate a single token against canonical registries or licensed L6 experimental rules."""
    w = normalize(tok)
    if not w:
        return True, 'punctuation', {}

    # 1. Canonical Pronouns
    if w in PRONOUNS_NOM:
        return True, 'pronoun_nom', {'form': 'nominative'}
    if w in PRONOUNS_ACC:
        return True, 'pronoun_acc', {'form': 'accusative'}

    # 2. Canonical Function Words
    if w in CANONICAL_CONJUNCTIONS:
        return True, 'conjunction', {'gloss_tr': 've' if w == 'ya' else 'ama' if w == 'lia' else 'çünkü' if w == 'sira' else 'eğer'}
    if w in CANONICAL_POSTPOSITIONS:
        return True, 'postposition', {'gloss_tr': 'ile' if w == 've' else 'araçla' if w == 'se' else w}
    if w in CANONICAL_TAM:
        return True, 'tam_marker', {'marker': w}
    if w in CANONICAL_QUESTION:
        return True, 'question_particle', {'marker': w}
    if w in CANONICAL_FOCUS:
        return True, 'focus_particle', {'marker': w}
    if w in CANONICAL_COMPARATIVES:
        return True, 'comparison_marker', {'marker': w}
    if w in CANONICAL_QUANTITY:
        return True, 'quantity_marker', {'marker': w}
    if w in CANONICAL_INTERROGATIVES:
        return True, 'interrogative', {'marker': w}
    if w in CANONICAL_COMPLEMENTIZER:
        return True, 'complementizer', {'marker': w}
    if w in CANONICAL_NUMERALS:
        return True, 'numeral', {'marker': w}
    if w in CANONICAL_INTERJECTIONS:
        return True, 'interjection', {'marker': w}
    if w in CANONICAL_POLITENESS:
        return True, 'politeness', {'marker': w}

    # 3. L6 Experimental Particles
    if mode in ('experimental', 'l6'):
        if w in L6_EXPERIMENTAL_CONJUNCTIONS:
            return True, 'experimental_conjunction', {'marker': w}
        if w in L6_EXPERIMENTAL_PARTICLES:
            return True, 'experimental_particle', {'marker': w}
        if w in L6_EXPERIMENTAL_QUANTIFIERS:
            return True, 'experimental_quantifier', {'marker': w, 'status': 'unadopted_proposal'}

        # L6 Experimental Passive Infix -il- on licensed transitive verbs
        m_il = re.match(r'^([a-zıiöü]+)il(en)$', w)
        if m_il:
            stem = m_il.group(1)
            base_verb = stem + 'en'
            frame = get_valency_frame(base_verb)
            if frame and 'Patient' in frame.get('roles', []):
                return True, 'experimental_passive_verb', {'base_verb': base_verb}
            else:
                return False, 'invalid_passive_derivation', {'base_verb': base_verb}

    # 4. Lexicon Lookup (Exact Match)
    exact = lookup(w, version=version)
    if exact:
        pos = exact[0].get('part_of_speech', 'unknown')
        return True, pos, {'matches': exact}

    # 5. Morphological Derivation (Plural, Object, Verb, Quality)
    analysis = analyze(w, version=version)
    if analysis.get('status') in ('attested', 'candidate') and analysis.get('candidates'):
        top = analysis['candidates'][0]
        op = top.get('operation')
        if op in ('object', 'plural_object'):
            return True, 'nominal_object', top
        elif op == 'plural':
            return True, 'nominal_plural', top
        elif op == 'verb_derivation':
            return True, 'verb', top
        elif op == 'quality_derivation':
            return True, 'quality', top
        elif op == 'compound_segmentation':
            return True, 'compound_nominal', top

    return False, 'unknown_lexeme', {}


def analyze_l6_sentence(text: str, version: str = '1.1.0') -> SentenceAST:
    """Perform comprehensive, lexicon-grounded generative semantic parsing."""
    raw = str(text).strip()
    if not raw:
        return SentenceAST(
            status='unsupported',
            construction='empty',
            raw_text=raw,
            version=version,
            diagnostics=['Expected non-empty text input.']
        )

    # 1. Clean and tokenize text
    punct = raw[-1] if raw and raw[-1] in '.!?' else ''
    clean_text = raw.rstrip('.!?')

    # Detect Direct Quotation Frame before splitting
    if ':' in raw and any(q in raw for q in ('"', '“', '”')):
        return _parse_quotative_sentence(raw, clean_text, punct, version)

    # Token-level lexical audit
    words_clean = re.findall(r"[^\W\d_]+", clean_text, re.UNICODE)
    unknowns = []
    for w in words_clean:
        valid, cat, details = validate_token(w, version=version, mode='l6')
        if not valid:
            unknowns.append(w)

    if unknowns:
        return SentenceAST(
            status='unknown_lexeme',
            construction='unrecognized_lexemes',
            raw_text=raw,
            version=version,
            diagnostics=[f"Unregistered or unrecognizable lexeme(s): {', '.join(unknowns)}."],
            warnings=["Alei generative grammar requires validated roots or licensed derivations."]
        )

    # 2. Syntax Gate: Check for improper use of comitative 've' as coordinating conjunction
    # 've' is strictly comitative postposition ("with/together"), e.g. "Mei ve"
    # Using 've' between clauses or before verbs/clauses is an ungrammatical error
    tokens_raw = [t.strip(',;') for t in clean_text.split() if t.strip(',;')]
    for i, tok in enumerate(tokens_raw):
        if tok.lower() == 've':
            # If 've' is at index 0, or between clauses, or followed by finite verbs/predicates
            if i == 0 or (i + 1 < len(tokens_raw) and tokens_raw[i+1].lower() in PRONOUNS_NOM | CANONICAL_TAM):
                return SentenceAST(
                    status='unsupported',
                    construction='invalid_conjunction',
                    raw_text=raw,
                    version=version,
                    diagnostics=["'ve' is a comitative postposition ('with/together'), not an additive conjunction. Use canonical 'ya' for clause coordination."]
                )

    # 3. Clause Coordination with canonical 'ya' ("and")
    if ' ya ' in f" {clean_text} ":
        return _parse_coordinate_sentence(raw, clean_text, punct, version)

    # 4. Conditional / Concessive / Counterfactual Complex Sentences
    if ',' in clean_text or clean_text.lower().startswith('şe ') or clean_text.lower().startswith('şe-el '):
        parts = [p.strip() for p in clean_text.split(',', 1)]
        first_clause = parts[0]
        first_words = [t.strip(',;') for t in first_clause.split() if t.strip(',;')]
        if first_words and first_words[0].lower() in ('şe', 'şe-el'):
            return _parse_conditional_sentence(raw, parts, punct, version)

    # 5. Single Matrix Clause Parsing
    return _parse_single_clause(raw, clean_text, punct, version)


def _parse_quotative_sentence(raw: str, clean_text: str, punct: str, version: str) -> SentenceAST:
    """Parse direct quotation frame: Matrix speech verb + Quoted clause."""
    colon_idx = raw.index(':')
    frame_part = raw[:colon_idx].strip()
    quote_part = raw[colon_idx+1:].strip().strip('"“”').rstrip('.!?')

    # Parse matrix clause
    frame_ast = _parse_single_clause(frame_part, frame_part, '', version)
    if frame_ast.predicate and frame_ast.predicate.verb_lemma != 'vesen':
        frame_ast.diagnostics.append(f"Speech frame contains non-speech verb '{frame_ast.predicate.verb_lemma}'.")

    # Recursively parse embedded quotation
    quote_ast = analyze_l6_sentence(quote_part, version=version)

    res = SentenceAST(
        status='supported' if frame_ast.status == 'supported' and quote_ast.status in ('supported', 'ambiguous') else 'unsupported',
        construction='quotative',
        speech_act='quotation',
        subject=frame_ast.subject,
        predicate=frame_ast.predicate,
        tense=frame_ast.tense,
        aspect=frame_ast.aspect,
        polarity=frame_ast.polarity,
        mood='indicative',
        raw_text=raw,
        version=version,
        is_experimental=True,
        subordinate_clauses=[{
            'type': 'direct_quotation',
            'quote_text': quote_part,
            'quote_ast': quote_ast.to_dict()
        }],
        diagnostics=[f"Quotative frame with speech verb 'vesen'; embedded quote status: {quote_ast.status}."]
    )
    return res


def _parse_coordinate_sentence(raw: str, clean_text: str, punct: str, version: str) -> SentenceAST:
    """Parse coordinate sentence joined by canonical 'ya' with independent features."""
    parts = clean_text.split(' ya ')
    clause_asts: List[SentenceAST] = []
    all_supported = True

    for p in parts:
        c_ast = _parse_single_clause(p.strip(), p.strip(), '', version)
        if c_ast.status != 'supported':
            all_supported = False
        clause_asts.append(c_ast)

    res = SentenceAST(
        status='supported' if all_supported else 'unsupported',
        construction='coordinate_sentence',
        speech_act='assertion',
        polarity=clause_asts[0].polarity if clause_asts else True,
        tense=clause_asts[0].tense if clause_asts else 'unmarked',
        aspect=clause_asts[0].aspect if clause_asts else 'unmarked',
        mood='indicative',
        raw_text=raw,
        version=version,
        is_experimental=True,
        coordinate_clauses=[c.to_dict() for c in clause_asts],
        diagnostics=["Coordinate sentence conjoined via canonical additive conjunction 'ya'."]
    )
    return res


def _parse_conditional_sentence(raw: str, parts: List[str], punct: str, version: str) -> SentenceAST:
    """Parse conditional ('şe'), concessive ('şe-el'), and counterfactual ('şe da ... da va') structures."""
    ant_text = parts[0].strip()
    con_text = parts[1].strip() if len(parts) > 1 else ''

    ant_words = [t.lower() for t in ant_text.split()]
    is_concessive = ant_words[0] == 'şe-el'
    is_conditional = ant_words[0] == 'şe'

    # Check for Counterfactual Past condition: Antecedent has past 'da' + Consequent has past-future 'da va'
    full_lower = raw.lower()
    is_counterfactual = False
    if is_conditional or is_concessive:
        if ' da ' in f" {ant_text.lower()} " and (' da va ' in f" {con_text.lower()} " or con_text.lower().endswith(' da va')):
            is_counterfactual = True

    # Parse matrix clause (consequent)
    matrix_ast = _parse_single_clause(con_text, con_text, punct, version)

    # Set mood and speech act
    if is_counterfactual:
        matrix_ast.mood = 'counterfactual'
        matrix_ast.diagnostics.append("Compositional counterfactual conditional detected (şe da ... da va).")
    elif is_concessive:
        matrix_ast.mood = 'concessive'
        matrix_ast.diagnostics.append("Concessive conditional detected ('şe-el').")
    else:
        matrix_ast.mood = 'conditional'
        matrix_ast.diagnostics.append("Standard conditional detected ('şe').")

    if punct == '!' and matrix_ast.subject in (None, 'implied_2nd_person', 'Sai', 'Saina'):
        matrix_ast.speech_act = 'imperative'

    matrix_ast.construction = 'complex_conditional'
    matrix_ast.raw_text = raw
    matrix_ast.subordinate_clauses.append({
        'type': 'concessive_condition' if is_concessive else 'counterfactual_antecedent' if is_counterfactual else 'conditional_antecedent',
        'marker': ant_words[0],
        'clause_text': ant_text
    })
    return matrix_ast


def _parse_single_clause(raw: str, clean_text: str, punct: str, version: str) -> SentenceAST:
    """Parse a single clause into typed AST with argument valency and semantic roles."""
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

    tokens = [t.strip(',;') for t in clean_text.split() if t.strip(',;')]
    if not tokens:
        ast.status = 'unsupported'
        return ast

    # 1. Question Particle 'le'
    if tokens and tokens[-1].lower() == 'le':
        ast.speech_act = 'question'
        tokens = tokens[:-1]

    # 2. Check for Future-in-the-Past vs Counterfactual:
    # A standalone clause with 'da va' without 'şe' condition is future-in-the-past / unfulfilled intention
    toks_lower = [t.lower() for t in tokens]
    if 'da' in toks_lower and 'va' in toks_lower:
        # Check order: 'da' followed by 'va'
        da_idx = toks_lower.index('da')
        va_idx = toks_lower.index('va')
        if da_idx + 1 == va_idx:
            ast.tense = 'future_in_past'
            ast.diagnostics.append("Past-future sequence 'da va' represents future-in-the-past or unfulfilled intention; not counterfactual without 'şe' condition.")
        else:
            ast.tense = 'past'
    elif 'da' in toks_lower:
        ast.tense = 'past'
    elif 'va' in toks_lower:
        ast.tense = 'future'

    # Aspect
    if 'du' in toks_lower:
        ast.aspect = 'progressive'
    elif 'fa' in toks_lower:
        ast.aspect = 'completed'
    elif 'su' in toks_lower:
        ast.aspect = 'habitual'

    # Polarity
    if 'ne' in toks_lower:
        ast.polarity = False

    # 3. Canonical Comparison with 'peli' and 'nera'
    # Pattern: [Subject] peli [Quality] [Standard] nera
    # Or short: [Subject] peli [Quality]
    if 'peli' in toks_lower:
        peli_idx = toks_lower.index('peli')
        quality = tokens[peli_idx + 1] if peli_idx + 1 < len(tokens) else None
        standard = None
        if 'nera' in toks_lower:
            nera_idx = toks_lower.index('nera')
            if nera_idx > peli_idx + 1:
                standard = " ".join(tokens[peli_idx + 2:nera_idx])
        ast.comparative = {
            'is_comparative': True,
            'marker': 'peli',
            'quality': quality,
            'standard': standard,
            'standard_marker': 'nera' if standard else None,
            'degree': 'comparative'
        }
        ast.diagnostics.append(f"Canonical comparison detected via 'peli' (more) and 'nera' (compared with); standard: '{standard}'.")

    # Flag non-canonical comparison using ablative 'fi'
    if 'fi' in toks_lower and not ast.comparative:
        fi_idx = toks_lower.index('fi')
        if fi_idx == len(tokens) - 1 and fi_idx >= 2:
            ast.diagnostics.append("Note: Postposition 'fi' is canonically ablative ('from'). Canonical comparison uses 'peli ... nera'.")

    # 4. Quantifiers and Negation Scope
    # Universal: 'sam' (experimental candidate), Existential/Numeral: 'ena'
    first_two = [t.lower() for t in tokens[:2]]
    if 'ne' in first_two and 'sam' in first_two:
        ast.quantifier_scope = {
            'quantifier': 'sam',
            'scope': 'partial_negation',
            'logical_formula': '¬∀x (Noun(x) → P(x))',
            'meaning': 'not all / not every (does not mathematically imply existence)'
        }
        ast.polarity = False
        ast.is_experimental = True
    elif 'sam' in first_two and 'ne' not in first_two:
        ast.quantifier_scope = {
            'quantifier': 'sam',
            'scope': 'universal_affirmative',
            'logical_formula': '∀x (Noun(x) → P(x))',
            'meaning': 'all / every (unadopted experimental proposal)'
        }
        ast.is_experimental = True
    elif 'ne' in first_two and 'ena' in first_two:
        ast.quantifier_scope = {
            'quantifier': 'ena',
            'scope': 'total_negation',
            'logical_formula': '∀x (Noun(x) → ¬P(x))',
            'meaning': 'none / not one / nobody'
        }
        ast.polarity = False

    # 5. Subordinate Clauses with 'ke': Disambiguate Relatives vs Verb Complements
    if 'ke' in toks_lower:
        ke_idx = toks_lower.index('ke')
        prev_tok = tokens[ke_idx - 1] if ke_idx > 0 else ''
        frame_prev = get_valency_frame(prev_tok)

        # Case A: Verb Complement Clause (preceded by communicative/modal/epistemic verb)
        if frame_prev and frame_prev.get('class') in ('modal_transitive', 'modal_auxiliary', 'modal_epistemic', 'communicative'):
            comp_tokens = tokens[ke_idx + 1:]
            comp_str = " ".join(comp_tokens)
            ast.subordinate_clauses.append({
                'type': 'complement_clause',
                'matrix_verb': prev_tok,
                'embedded_text': comp_str
            })
            ast.construction = 'embedded_clause'
            ast.diagnostics.append(f"Canonical verb complement clause governed by '{prev_tok} ke'.")

        # Case B: Post-nominal Relative Clause (preceded by noun)
        else:
            head_noun = prev_tok
            embedded_tokens = tokens[ke_idx + 1:]

            # Determine boundary of embedded relative clause:
            emb_first = embedded_tokens[0].lower() if embedded_tokens else ''
            is_obj_rel = emb_first in PRONOUNS_NOM or (lookup(emb_first) and lookup(emb_first)[0].get('part_of_speech') == 'root')

            matrix_rem_tokens = []
            rel_clause_tokens = []

            if is_obj_rel:
                # Object Relative: [embedded subject] + [TAM?] + [verb]
                verb_found = False
                for t in embedded_tokens:
                    if not verb_found:
                        rel_clause_tokens.append(t)
                        if t.lower().endswith('en') and t.lower() not in CANONICAL_POSTPOSITIONS and t.lower() not in CANONICAL_TAM:
                            verb_found = True
                    else:
                        matrix_rem_tokens.append(t)
                ast.subordinate_clauses.append({
                    'type': 'object_relative_clause',
                    'head_noun': head_noun,
                    'embedded_role': 'Patient',
                    'embedded_subject': embedded_tokens[0],
                    'embedded_text': " ".join(rel_clause_tokens)
                })
                ast.diagnostics.append(f"Post-nominal Object Relative Clause: Head '{head_noun}' is Patient of embedded clause.")
            else:
                # Subject Relative: [TAM?] + [verb] + [optional object]
                verb_found = False
                obj_found = False
                for t in embedded_tokens:
                    if not verb_found:
                        rel_clause_tokens.append(t)
                        if t.lower().endswith('en') and t.lower() not in CANONICAL_POSTPOSITIONS and t.lower() not in CANONICAL_TAM:
                            verb_found = True
                    elif not obj_found and (t.lower() in PRONOUNS_ACC or t.lower().endswith(('an', 'n'))):
                        rel_clause_tokens.append(t)
                        obj_found = True
                    else:
                        matrix_rem_tokens.append(t)
                ast.subordinate_clauses.append({
                    'type': 'subject_relative_clause',
                    'head_noun': head_noun,
                    'embedded_role': 'Agent',
                    'embedded_text': " ".join(rel_clause_tokens)
                })
                ast.diagnostics.append(f"Post-nominal Subject Relative Clause: Head '{head_noun}' is Agent of embedded clause.")

            if matrix_rem_tokens:
                tokens = tokens[:ke_idx] + matrix_rem_tokens

    # 6. Extract Subject, Verb, Arguments, and Voice
    _resolve_arguments_and_valency(tokens, ast, version, punct=punct)

    # 7. Imperative Speech Act Check
    if punct == '!':
        subj_str = str(ast.subject or '').lower()
        if subj_str in ('', 'none', 'implied_2nd_person', 'sai', 'saina'):
            ast.speech_act = 'imperative'
            ast.construction = 'imperative'
            if not ast.subject:
                ast.subject = 'implied_2nd_person'

    return ast


def _resolve_arguments_and_valency(tokens: List[str], ast: SentenceAST, version: str, punct: str = '') -> None:
    """Ground and verify subject, predicate, voice, and arguments against valency frames."""
    if not tokens:
        ast.status = 'unsupported'
        return

    # Filter out function particles to isolate potential subject, verb, objects
    particles_to_skip = CANONICAL_TAM | {'le', 'ke', 'ya', 'lia', 'sira', 'şe', 'şe-el', 'peli', 'nera'}

    # 1. Detect Voice and Target Verb
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
        if t_low.endswith('en') and t_low not in CANONICAL_POSTPOSITIONS and t_low not in particles_to_skip:
            verb_lemma = t_low
            target_verb_token = tok

            # Check if preceded by middle particle 'vo'
            if i > 0 and tokens[i-1].lower() == 'vo':
                voice = 'middle'
                ast.diagnostics.append(f"Middle voice detected via analytic particle 'vo': 'vo {tok}'.")
            break

    # Check for Inchoative Periphrasis ('avelen' + stative quality)
    if verb_lemma == 'avelen':
        for tok in tokens:
            t_low = tok.lower()
            if t_low.endswith('i') and t_low not in PRONOUNS_NOM and t_low != 'mi':
                # Verify that this is an attested quality
                q_an = analyze(t_low, version=version)
                if lookup(t_low, version=version) or (q_an.get('candidates') and q_an['candidates'][0].get('operation') == 'quality_derivation'):
                    voice = 'inchoative'
                    ast.diagnostics.append(f"Inchoative state-transition periphrasis detected: 'avelen {tok}'.")
                    break

    # 2. Extract Subject
    # Subject must be validated nominal or pronoun
    subject_candidate = None
    for tok in tokens:
        t_low = tok.lower()
        if t_low in particles_to_skip or t_low in ('vo', 'sam'):
            continue
        if tok == target_verb_token:
            continue
        # Check if nominal pronoun or attested noun
        if t_low in PRONOUNS_NOM:
            subject_candidate = tok
            break
        rec = lookup(t_low, version=version)
        if rec and rec[0].get('part_of_speech') in ('root', 'nominal', 'name'):
            subject_candidate = tok
            break
        an = analyze(t_low, version=version)
        if an.get('candidates') and an['candidates'][0].get('operation') in ('plural', 'compound_segmentation'):
            subject_candidate = tok
            break

    overt_roles: Dict[str, str] = {}
    predicate_arguments: List[ArgumentRole] = []

    # Assign Subject Role
    frame = get_valency_frame(verb_lemma) if verb_lemma else None

    # Handle implied 2nd person in imperative
    if not subject_candidate and (punct == '!' or ast.speech_act == 'imperative'):
        subject_candidate = 'implied_2nd_person'
        ast.subject = subject_candidate
        subj_role = frame.get('subject_role', 'Agent') if frame else 'Agent'
        overt_roles[subj_role] = subject_candidate
        predicate_arguments.append(ArgumentRole(role=subj_role, value=subject_candidate, is_overt=False, is_omitted=True))
        ast.speech_act = 'imperative'
    elif subject_candidate:
        ast.subject = subject_candidate
        subj_role = 'Agent'
        if voice in ('passive', 'middle'):
            subj_role = 'Patient'
        elif voice == 'inchoative':
            subj_role = 'Theme'
        elif frame and frame.get('subject_role'):
            subj_role = frame['subject_role']

        overt_roles[subj_role] = subject_candidate
        predicate_arguments.append(ArgumentRole(role=subj_role, value=subject_candidate, is_overt=True))

    # 3. Extract Recipient or Destination with 'ta'
    recip_candidate = None
    for i, tok in enumerate(tokens):
        if tok.lower() == 'ta' and i > 0:
            recip_candidate = tokens[i-1]
            if frame and 'Destination' in frame.get('roles', []):
                overt_roles['Destination'] = recip_candidate
                predicate_arguments.append(ArgumentRole(role='Destination', value=recip_candidate, is_overt=True))
            else:
                overt_roles['Recipient'] = recip_candidate
                predicate_arguments.append(ArgumentRole(role='Recipient', value=recip_candidate, is_overt=True))

    # 4. Extract Location with 'lo'
    for i, tok in enumerate(tokens):
        if tok.lower() == 'lo' and i > 0:
            loc = tokens[i-1]
            overt_roles['Location'] = loc
            predicate_arguments.append(ArgumentRole(role='Location', value=loc, is_overt=True))

    # 5. Extract Object (Patient, Stimulus, Beneficiary)
    for i, tok in enumerate(tokens):
        t_low = tok.lower()
        if i + 1 < len(tokens) and tokens[i+1].lower() in ('ta', 'lo', 've', 'se', 'fi', 'nera'):
            continue
        if tok == recip_candidate or tok == subject_candidate or tok == target_verb_token:
            continue
        if t_low in particles_to_skip or t_low in ('vo', 'sam'):
            continue

        # Check if valid accusative object
        is_object = False
        if t_low in PRONOUNS_ACC:
            is_object = True
        else:
            an = analyze(t_low, version=version)
            if an.get('candidates') and an['candidates'][0].get('operation') in ('object', 'plural_object'):
                is_object = True

        if is_object:
            # Check for Reflexive co-reference: Subject and Object share person/number
            sub_lower = (subject_candidate or '').lower()
            if (sub_lower == 'mei' and t_low == 'mein') or \
               (sub_lower == 'sai' and t_low == 'sain') or \
               (sub_lower == 'eli' and t_low == 'elin') or \
               (sub_lower == 'meina' and t_low == 'meinan') or \
               (sub_lower == 'saina' and t_low == 'sainan') or \
               (sub_lower == 'elina' and t_low == 'elinan'):
                voice = 'reflexive'
                ast.diagnostics.append(f"Reflexive voice detected: Subject '{subject_candidate}' and Object '{tok}' are co-referential.")

            # Map role based on verb frame
            obj_role = 'Patient'
            if frame:
                if 'Stimulus' in frame.get('roles', []):
                    obj_role = 'Stimulus'
                elif 'Beneficiary' in frame.get('roles', []):
                    obj_role = 'Beneficiary'
                elif 'Proposition' in frame.get('roles', []):
                    obj_role = 'Proposition'

            overt_roles[obj_role] = tok
            predicate_arguments.append(ArgumentRole(role=obj_role, value=tok, is_overt=True))

    # 6. Evaluate Predicate Frame
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
                ast.status = 'unsupported'
    else:
        # Check for nominal / quality predicate
        # e.g., 'Lüra fali.' or 'Mei süli.'
        found_pred = False
        for tok in tokens:
            t_low = tok.lower()
            if t_low.endswith('i') and t_low not in PRONOUNS_NOM and t_low not in CANONICAL_POSTPOSITIONS and t_low != 'mi':
                # Verify that tok is actually an attested quality or legal quality derivation
                an = analyze(t_low, version=version)
                is_legit_quality = bool(lookup(t_low, version=version)) or (
                    bool(an.get('candidates')) and an['candidates'][0].get('operation') == 'quality_derivation'
                )
                if is_legit_quality:
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
                    found_pred = True
                    break

        if not found_pred and not ast.comparative:
            ast.status = 'unsupported'
            ast.diagnostics.append("Clause lacks a supported finite verb or verified quality predicate.")
