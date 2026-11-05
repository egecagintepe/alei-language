from .lexicon import lookup, records, normalize
from .orthography import VOWELS
def plural(stem): return stem+'na'
def object_form(stem): return stem+('n' if normalize(stem)[-1:] in VOWELS else 'an')
def analyze(word):
    exact=lookup(word)
    if exact: return {'status':'attested','matches':exact,'candidates':[]}
    s=normalize(word); candidates=[]
    for record in records():
        stem=record['canonical_spelling']; base=normalize(stem)
        if not base: continue
        for label,form in [('plural',plural(base)),('object',object_form(base)),('plural_object',object_form(plural(base)))]:
            if form==s: candidates.append({'base':stem,'operation':label,'status':'candidate'})
        if record['part_of_speech']=='root':
            # v epenthesis only after a two-vowel stem
            suffix=('v' if len(base)>1 and base[-1] in VOWELS and base[-2] in VOWELS else '')+'en'
            if base+suffix==s: candidates.append({'base':stem,'operation':'verb_derivation','status':'candidate'})
            if base[-1] not in VOWELS and base+'i'==s: candidates.append({'base':stem,'operation':'quality_derivation','status':'candidate'})
    roots=[r for r in records() if r['part_of_speech']=='root']
    for left in roots:
        a=normalize(left['canonical_spelling'])
        if s.startswith(a) and len(a)<len(s):
            for right in roots:
                if a+normalize(right['canonical_spelling'])==s:
                    candidates.append({'components':[left['canonical_spelling'],right['canonical_spelling']],'operation':'compound_segmentation','status':'candidate'})
    return {'status':'candidate' if candidates else 'unknown','matches':[],'candidates':candidates}


def analyze_simple_sentence(text):
    """Recognize a minimal pronoun + attested verb + marked pronoun sentence.

    This deliberately does not claim to parse arbitrary v1.0 grammar.
    """
    words=[normalize(w.strip('.,!?')) for w in text.split()]
    if len(words)!=3 or words[0] not in {'mei','sai','eli'}:
        return {'status':'unsupported'}
    subject=words[0]
    for verb_index, object_index, order in [(1,2,'SVO'),(2,1,'SOV')]:
        verb=words[verb_index]; obj=words[object_index]
        verb_rows=lookup(verb)
        objects=[p for p in ('mei','sai','eli') if object_form(p)==obj]
        if objects and any(r['part_of_speech']=='verb' for r in verb_rows):
            return {'status':'parsed','subject':subject,'verb':verb,'object':objects[0], 'order':order,'object_focus':order=='SOV'}
    return {'status':'unsupported'}
