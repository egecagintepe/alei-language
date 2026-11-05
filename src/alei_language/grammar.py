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
