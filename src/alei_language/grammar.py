"""A deliberately narrow recognizer, not a complete grammar checker."""
import re
from .lexicon import normalize, lookup
from .morphology import object_form

PRONOUNS = ('mei','sai','eli','meina','saina','elina','elar','elarna')
PATTERN = re.compile(r'^(?:(ne) )?(?:(da|va) )?(?:(du|fa|su) )?([^ ]+)$')

def parse_clause(text):
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
def _inventory():
    nominal={normalize(r['canonical_spelling']) for r in records()
             if r['part_of_speech'] in {'root','compound','pron','interrogative'}}
    qualities={normalize(r['canonical_spelling']) for r in records()
               if r['part_of_speech']=='quality'}
    verbs={normalize(r['canonical_spelling']) for r in records()
           if r['part_of_speech']=='verb'}
    objects={}
    for stem in nominal:
        objects.setdefault(object_form(stem),set()).add(stem)
    return nominal,qualities,verbs,objects

def parse_sentence(text):
    """Recognize a small documented grammar; unrecognized does not mean invalid."""
    if not isinstance(text,str) or not text.strip():
        return {'status':'unsupported','reason':'Expected a sentence'}
    s=normalize(text).strip()
    # Do not silently remove clause boundaries, vocatives or unknown punctuation.
    if any(c in s for c in ',;:[]-'):
        return {'status':'unsupported','reason':'Clause boundaries or vocatives are not supported'}
    words=s.rstrip('.!?').split()
    nominal,qualities,verbs,objects=_inventory()
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
