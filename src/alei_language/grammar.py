"""A deliberately narrow recognizer, not a complete grammar checker."""
import re
from .lexicon import normalize, lookup, resolve_version
from .morphology import object_form, analyze

PRONOUNS = ('mei','sai','eli','meina','saina','elina','elar','elarna')
PATTERN = re.compile(r'^(?:(ne) )?(?:(da|va) )?(?:(du|fa|su) )?([^ ]+)$')

def _parse_clause(text, version='1.0'):
    """Parse pronoun subject + marked pronoun object + attested verb.

    Either SVO or SOV is accepted. A successful structural parse does not
    establish lexical senses, discourse reference, or semantic correctness.
    Inputs outside this narrow grammar are explicitly unsupported.
    """
    if not isinstance(text,str):
        return {'status':'unsupported','reason':'Expected text'}
    words=normalize(text).strip().rstrip('.!?').split()
    if len(words)<3 or words[0] not in PRONOUNS:
        return {'status':'unsupported','reason':'Requires a pronoun subject and marked pronoun object'}
    object_forms={object_form(p):p for p in PRONOUNS}
    candidates=[]
    for index in (1,len(words)-1):
        if words[index] not in object_forms: continue
        group=' '.join(words[2:] if index==1 else words[1:-1])
        match=PATTERN.fullmatch(group)
        if not match: continue
        negative,tense,aspect,verb=match.groups()
        if any(r['part_of_speech']=='verb' for r in lookup(verb)):
            candidates.append({'subject':words[0], 'object':object_forms[words[index]],
                'verb':verb, 'order':'SOV' if index==1 else 'SVO',
                'negation':bool(negative), 'tense':{'da':'past','va':'future',None:'unmarked'}[tense],
                'aspect':{'du':'progressive','fa':'completed','su':'habitual',None:'unmarked'}[aspect]})
    if len(candidates)==1:
        return {'status':'parsed','analysis':candidates[0],
                'semantic_correctness':'not_evaluated'}
    if candidates: return {'status':'ambiguous','analyses':candidates}
    return {'status':'unsupported','reason':'Outside the supported clause pattern or marker order'}

# Extended recognition is a separate API: the original parse_clause contract is
# retained. Results describe surface structure, never translation correctness.
from functools import lru_cache
from .lexicon import records

@lru_cache(maxsize=1)
def _inventory(version='1.0'):
    nominal={normalize(r['canonical_spelling']) for r in records(version,include_compatibility=True)
             if r['part_of_speech'] in {'root','compound','pron','interrogative'}}
    qualities={normalize(r['canonical_spelling']) for r in records(version,include_compatibility=True)
               if r['part_of_speech']=='quality'}
    verbs={normalize(r['canonical_spelling']) for r in records(version,include_compatibility=True)
           if r['part_of_speech']=='verb'}
    objects={}
    for stem in nominal:
        objects.setdefault(object_form(stem),set()).add(stem)
    return nominal,qualities,verbs,objects

def _parse_sentence(text, version='1.0'):
    """Recognize a small documented grammar; unrecognized does not mean invalid."""
    if not isinstance(text,str) or not text.strip():
        return {'status':'unsupported','reason':'Expected a sentence'}
    s=normalize(text).strip()
    # Do not silently remove clause boundaries, vocatives or unknown punctuation.
    if any(c in s for c in ',;:[]-'):
        return {'status':'unsupported','reason':'Clause boundaries or vocatives are not supported'}
    words=s.rstrip('.!?').split()
    nominal,qualities,verbs,objects=_inventory(version)
    if len(words)<2 or words[0] not in (*PRONOUNS,'keli'):
        return {'status':'unsupported','reason':'Unsupported subject or fragment'}
    subject=words[0]; tail=words[1:]
    question=False
    if tail and tail[-1]=='le': question=True; tail=tail[:-1]
    # Question words are not interchangeable with le (source §4.6).
    if question and (words[0]=='keli' or any(w in {'vena','miva','keli','orai','vela','hiva','vera','mivan','veran'} for w in tail)):
        return {'status':'unsupported','reason':'Question-particle combination needs review'}
    interrogative=None
    if tail and tail[-1] in {'vena','orai','vela','hiva'}:
        interrogative=tail[-1]; tail=tail[:-1]
    if not tail and interrogative=='vena':
        return {'status':'parsed','analysis':{'construction':'location_question','subject':subject,
                'interrogative':'vena','question':True},'semantic_correctness':'not_evaluated'}
    if not tail: return {'status':'unsupported','reason':'Missing predicate'}
    def parsed(analysis):
        question_word=interrogative or ('keli' if subject=='keli' else None)
        if analysis.get('object') in {'miva','keli','vera'}:
            question_word=analysis['object']
        analysis.update({'subject':subject,'question':bool(question or question_word),'interrogative':question_word})
        return {'status':'parsed','analysis':analysis,'semantic_correctness':'not_evaluated'}
    # Simple possession phrase: no assumption of a zero-copula clause.
    if len(tail)==2 and tail[0]=='ri' and tail[1] in nominal and not question:
        return {'status':'parsed','analysis':{'construction':'possession_phrase','possessor':subject,
                'possessed':tail[1]},'semantic_correctness':'not_evaluated'}
    # Source-supported location predicate and optional X ri Y possession.
    if tail[-1:] == ['lo']:
        place=tail[:-1]
        if len(place)==1 and place[0] in nominal:
            return parsed({'construction':'location_predicate','location':place[0]})
        if len(place)==3 and place[0] in nominal and place[1]=='ri' and place[2] in nominal:
            return parsed({'construction':'location_predicate','location':place[2],'possessor':place[0]})
    # Modal plus ke: embedded subject optional and separately identified.
    if 'ke' in tail:
        if tail.count('ke')!=1: return {'status':'unsupported','reason':'Nested complement'}
        cut=tail.index('ke'); outer=tail[:cut]; embedded=tail[cut+1:]
        if not embedded: return {'status':'unsupported','reason':'Missing embedded clause'}
        match=PATTERN.fullmatch(' '.join(outer))
        if not match or match.group(4) not in {'naelen','yelen','ünaren'}:
            return {'status':'unsupported','reason':'Unsupported matrix predicate'}
        embedded_subject=None
        if embedded[0] in PRONOUNS:
            embedded_subject=embedded[0]; embedded=embedded[1:]
        if not embedded or embedded[0] not in verbs:
            return {'status':'unsupported','reason':'Unsupported embedded verb'}
        ev=embedded[0]; rest=embedded[1:]; embedded_object=None; destination=None
        if len(rest)==1 and rest[0] in objects:
            choices=objects[rest[0]]
            if len(choices)!=1: return {'status':'ambiguous','reason':'Multiple embedded object analyses','candidates':sorted(choices)}
            embedded_object=next(iter(choices))
        elif len(rest)==2 and rest[0] in nominal and rest[1]=='ta': destination=rest[0]
        elif rest: return {'status':'unsupported','reason':'Unsupported embedded complement'}
        neg,tense,aspect,verb=match.groups()
        return parsed({'construction':'embedded_clause','verb':verb,'embedded_verb':ev,
          'embedded_subject':embedded_subject,'embedded_object':embedded_object,'destination':destination,
          'tense':tense or 'unmarked','aspect':aspect or 'unmarked','negation':bool(neg)})
    # Explicit zero-copula quality/nominal predicates (not finite verbs).
    m=PATTERN.fullmatch(' '.join(tail))
    if m:
        neg,tense,aspect,pred=m.groups()
        if pred in verbs:
            return parsed({'construction':'verbal','verb':pred,'object':None,'order':'SV',
                           'tense':tense or 'unmarked','aspect':aspect or 'unmarked','negation':bool(neg)})
        if aspect is None and pred in qualities|nominal:
            return parsed({'construction':'nominal_predicate','predicate':pred,
                           'tense':tense or 'unmarked','negation':bool(neg)})
    # A finite verb plus an overt marked nominal object, in either order.
    candidates=[]
    for index in (0,len(tail)-1):
        if tail[index] not in objects: continue
        group=tail[1:] if index==0 else tail[:-1]
        m=PATTERN.fullmatch(' '.join(group))
        if not m or m.group(4) not in verbs: continue
        neg,tense,aspect,verb=m.groups()
        for obj in sorted(objects[tail[index]]):
            candidates.append({'construction':'verbal','verb':verb,'object':obj,
              'order':'SOV' if index==0 else 'SVO','tense':tense or 'unmarked',
              'aspect':aspect or 'unmarked','negation':bool(neg)})
    if len(candidates)==1: return parsed(candidates[0])
    if candidates: return {'status':'ambiguous','candidates':candidates,'semantic_correctness':'not_evaluated'}
    return {'status':'unsupported','reason':'Outside documented recognizer patterns'}


def _with_compatibility_warnings(result, text, version):
    if isinstance(text,str) and version=='1.1.0':
        warnings=[]
        for word in re.findall(r"[^\W\d_]+",text,re.UNICODE):
            exact=lookup(word,version=version)
            if not exact:
                for candidate in analyze(word,version=version).get('candidates',[]):
                    warning=candidate.get('warning')
                    if warning and warning not in warnings: warnings.append(warning)
            for record in exact:
                if record.get('warning') and record['warning'] not in warnings:
                    warnings.append(record['warning'])
        if warnings: result['warnings']=warnings
    return result

def parse_clause(text, version='1.0'):
    """Original narrow parser with optional language-version selection."""
    version=resolve_version(version)
    return _with_compatibility_warnings(_parse_clause(text,version),text,version)

def parse_sentence(text, version='1.0'):
    """Version-aware parser; report legacy spelling without rewriting input."""
    version=resolve_version(version)
    return _with_compatibility_warnings(_parse_sentence(text,version),text,version)

from .ast import SentenceAST, TokenNode, PredicateFrame, ArgumentRole
from .valency import evaluate_valency, get_valency_frame
from .semantic_grammar import analyze_l6_sentence

def parse_alei(text, version='1.0', mode='standard'):
    """Principled, typed AST analysis of Alei expressions.

    Returns a SentenceAST with explicit status:
    - 'supported': fully recognized within the grammar model and argument frames
    - 'ambiguous': multiple syntactically valid parses exist
    - 'unsupported': outside recognized sentence patterns or ungrammatical
    - 'contradictory': mutually exclusive markers or contradictory semantic assertions
    - 'unknown_lexeme': contains roots/stems unrecorded in standard or legal derivations

    mode='standard' enforces canonical rules only.
    mode='experimental' enables RFC-2026-001 candidates (middle voice particle 'se',
    concessive 'şe-el', subjectless imperatives, quotatives).
    """
    version = resolve_version(version)
    if not isinstance(text, str) or not text.strip():
        return SentenceAST(
            status='unsupported',
            construction='empty',
            raw_text=str(text),
            version=version,
            diagnostics=['Expected non-empty text input.']
        )

    if mode == 'l6':
        return analyze_l6_sentence(text, version=version)

    s = normalize(text).strip()

    # Step 1: Lexical verification and unknown lexeme detection
    words_clean = re.findall(r"[^\W\d_]+", s, re.UNICODE)
    recognized_particles = {
        'mei','sai','eli','meina','saina','elina','elar','elarna',
        'keli','vena','miva','orai','vela','hiva','vera','mivan','veran',
        'le','ke','ve','lo','ta','fi','se','ri','şe','el','lia','da','va','ne','du','fa','su','şe-el','teli'
    }
    unknowns = []
    for w in words_clean:
        if w in recognized_particles:
            continue
        rec = lookup(w, version=version)
        if not rec:
            an = analyze(w, version=version)
            if an.get('status') == 'unknown':
                unknowns.append(w)
    if unknowns:
        return SentenceAST(
            status='unknown_lexeme',
            construction='unrecognized_lexemes',
            raw_text=text,
            version=version,
            diagnostics=[f"Unregistered or unrecognizable lexeme(s): {', '.join(unknowns)}."],
            warnings=["Alei grammar does not guess arbitrary unrecorded words without shared definitions."]
        )

    # Step 2: Experimental Quotative direct speech
    if mode == 'experimental' and (':' in text and any(q in text for q in ('"', '“', '”'))):
        match = re.match(r'^(.*?)\s*:\s*["“](.*?)["”][.!?]?\s*$', text.strip())
        if match:
            matrix_clause, quote_clause = match.groups()
            m_words = normalize(matrix_clause).split()
            if len(m_words) >= 2 and any(w in ('vesen', 'ves') for w in m_words):
                sub_ast = parse_alei(quote_clause, version=version, mode=mode)
                subj = m_words[0] if m_words[0] in PRONOUNS else 'unmarked_speaker'
                return SentenceAST(
                    status='supported' if sub_ast.status in ('supported', 'ambiguous') else 'unsupported',
                    construction='quotative',
                    speech_act='quotation',
                    subject=subj,
                    raw_text=text,
                    version=version,
                    is_experimental=True,
                    diagnostics=[f"Quotative frame with speech verb '{m_words[-1]}'; embedded quote status: {sub_ast.status}."],
                    predicate=PredicateFrame(
                        verb_lemma='vesen',
                        valency_class='communicative',
                        arguments=[
                            ArgumentRole(role='Agent', value=subj, is_overt=True),
                            ArgumentRole(role='Message', value=quote_clause, is_overt=True)
                        ],
                        valency_satisfied=True
                    )
                )

    # Step 3: Experimental Concessive conditional (şe-el)
    if mode == 'experimental' and (s.startswith('şe-el ') or s.startswith('se-el ')):
        body = s[len('şe-el '):].strip()
        parts = [p.strip() for p in re.split(r'[,;]', body) if p.strip()]
        if len(parts) >= 2:
            cond_ast = parse_alei(parts[0], version=version, mode=mode)
            main_ast = parse_alei(parts[1], version=version, mode=mode)
            status = 'supported' if cond_ast.status in ('supported', 'ambiguous') and main_ast.status in ('supported', 'ambiguous') else 'unsupported'
            return SentenceAST(
                status=status,
                construction='concessive_conditional',
                speech_act=main_ast.speech_act,
                mood='concessive',
                subject=main_ast.subject,
                raw_text=text,
                version=version,
                is_experimental=True,
                diagnostics=["Concessive conditional compound 'şe-el' ('even if / olsa bile')."]
            )

    # Step 4: Imperative / Hortative (Standard §4.1 permits omitted pronouns in clear commands)
    if text.strip().endswith('!') or (mode == 'experimental' and text.strip().endswith('.')):
        s_clean = s.rstrip('.! ')
        w = s_clean.split()
        neg = False
        if w and w[0] == 'ne':
            neg = True
            w = w[1:]
        if len(w) == 1 and any(r['part_of_speech'] == 'verb' for r in lookup(w[0], version=version)):
            verb = w[0]
            val = evaluate_valency(verb, {'Agent': 'implied_2nd_person'})
            return SentenceAST(
                status='supported',
                construction='imperative',
                speech_act='imperative',
                polarity=not neg,
                mood='imperative',
                subject='implied_2nd_person',
                raw_text=text,
                version=version,
                is_experimental=False,
                predicate=PredicateFrame(
                    verb_lemma=verb,
                    voice='active',
                    valency_class=val.get('frame_class', 'transitive'),
                    arguments=[ArgumentRole(role='Agent', value='implied_2nd_person', is_overt=False, is_implied=True)],
                    valency_satisfied=True
                ),
                diagnostics=["Standard §4.1 subjectless imperative; addressee implied (2nd person)."]
            )

    # Step 5: Experimental Middle Voice (se) - Caution: 'se' is canonically instrumental postposition (functions:1080)
    if mode == 'experimental' and ' se ' in (' ' + s + ' '):
        raw_mod = re.sub(r'\bse\b', '', s)
        raw_mod = re.sub(r'\s+', ' ', raw_mod).strip()
        w_mod = raw_mod.rstrip('.!?').split()
        if len(w_mod) >= 2:
            subj = w_mod[0]
            verb = w_mod[-1]
            if any(r['part_of_speech'] == 'verb' for r in lookup(verb, version=version)):
                val = evaluate_valency(verb, {'Patient': subj}, voice='middle')
                neg = 'ne' in w_mod
                tense = 'past' if 'da' in w_mod else ('future' if 'va' in w_mod else 'unmarked')
                aspect = 'progressive' if 'du' in w_mod else ('completed' if 'fa' in w_mod else ('habitual' if 'su' in w_mod else 'unmarked'))
                return SentenceAST(
                    status='supported' if val['valency_satisfied'] else 'unsupported',
                    construction='verbal',
                    speech_act='assertion',
                    polarity=not neg,
                    tense=tense,
                    aspect=aspect,
                    mood='indicative',
                    subject=subj,
                    raw_text=text,
                    version=version,
                    is_experimental=True,
                    warnings=["'se' collides with canonical instrumental postposition (functions:1080)."],
                    predicate=PredicateFrame(
                        verb_lemma=verb,
                        voice='middle',
                        valency_class=val.get('frame_class', 'transitive'),
                        arguments=[ArgumentRole(role='Patient', value=subj, is_overt=True)],
                        valency_satisfied=val['valency_satisfied'],
                        valency_notes=val['notes']
                    ),
                    diagnostics=[
                        "Experimental middle voice particle 'se' promoting Patient to subject position.",
                        "COLLISION WARNING: 'se' is canonically the instrumental postposition (functions:1080, e.g. 'tüvan se'). Middle voice usage is an unadopted RFC proposal."
                    ] + val['notes']
                )

    # Step 6: Standard sentence parsing
    raw_res = _with_compatibility_warnings(_parse_sentence(text, version=version), text, version)
    status_raw = raw_res.get('status')
    warnings = raw_res.get('warnings', [])

    if status_raw == 'parsed':
        an = raw_res['analysis']
        const = an.get('construction', 'verbal')
        subj = an.get('subject')
        neg = an.get('negation', False)
        tense = an.get('tense', 'unmarked')
        aspect = an.get('aspect', 'unmarked')
        is_q = an.get('question', False)

        ast = SentenceAST(
            status='supported',
            construction=const,
            speech_act='question' if is_q else 'assertion',
            polarity=not neg,
            tense=tense,
            aspect=aspect,
            subject=subj,
            raw_text=text,
            version=version,
            warnings=warnings,
            diagnostics=[f"Standard recognized construction '{const}'."]
        )

        if const == 'verbal' and an.get('verb'):
            verb = an['verb']
            obj = an.get('object')
            overt_roles = {}
            if subj:
                overt_roles['Agent'] = subj
            if obj:
                overt_roles['Patient'] = obj
            val = evaluate_valency(verb, overt_roles)
            ast.predicate = PredicateFrame(
                verb_lemma=verb,
                voice='active',
                valency_class=val.get('frame_class', 'transitive'),
                arguments=[
                    ArgumentRole(role=val.get('subject_role', 'Agent'), value=subj, is_overt=bool(subj)),
                    ArgumentRole(role='Patient', value=obj, is_overt=bool(obj), is_omitted=not bool(obj))
                ],
                valency_satisfied=val['valency_satisfied'],
                valency_notes=val['notes']
            )
            if val['status'] == 'valency_clash':
                ast.status = 'unsupported'
                ast.diagnostics.append("Valency defect: Obligatory patient omitted in transitive clause without middle voice.")
            elif not val['valency_satisfied']:
                ast.diagnostics.extend(val['notes'])

        return ast

    elif status_raw == 'ambiguous':
        return SentenceAST(
            status='ambiguous',
            construction='ambiguous',
            raw_text=text,
            version=version,
            warnings=warnings,
            ambiguities=raw_res.get('candidates', []),
            diagnostics=[raw_res.get('reason', 'Multiple syntactic analyses exist for this surface string.')]
        )
    else:
        if mode in ('experimental', 'l6'):
            l6_ast = analyze_l6_sentence(text, version=version)
            if l6_ast.status == 'supported':
                l6_ast.warnings.extend(warnings)
                return l6_ast

        return SentenceAST(
            status='unsupported',
            construction='unsupported',
            raw_text=text,
            version=version,
            warnings=warnings,
            diagnostics=[raw_res.get('reason', 'Input string falls outside supported grammatical constructions.')]
        )

