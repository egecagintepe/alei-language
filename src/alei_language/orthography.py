from .lexicon import normalize
VOWELS=set('aeıioöuü')
CONSONANTS=set('bdfghjklmnñŋprsştvyz')
DIPHTHONGS={'ai','ei','ae','au'}
def validate(word):
    s=normalize(word); errors=[]
    if not s: errors.append('empty word')
    if any(c not in VOWELS|CONSONANTS for c in s): errors.append('character outside alphabet')
    for chars in (VOWELS,CONSONANTS):
        run=0
        for c in s:
            run = run+1 if c in chars else 0
            if run==3: errors.append('three adjacent vowels or consonants')
    return errors
def syllables(word):
    s=normalize(word); result=[]; i=0
    while i<len(s):
        if s[i] in VOWELS:
            if s[i:i+2] in DIPHTHONGS: result.append(s[i:i+2]); i+=2; continue
            result.append(s[i])
        i+=1
    return result
def stress_index(word):
    n=len(syllables(word)); return max(0,n-2) if n else None
