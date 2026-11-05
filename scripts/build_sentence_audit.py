"""Produce a reviewable linguistic annotation, not a canonical rewrite."""
import json, re, sys
from functools import lru_cache
from pathlib import Path
from alei_language.lexicon import lookup, normalize
from alei_language.morphology import analyze
ROOT=Path(__file__).resolve().parents[1]
@lru_cache(None)
def segmentation(token):
    if normalize(token)=='elora':
        return {'form':token,'segments':['Elora (example proper name)'],'certainty':'source_example'}
    matches=lookup(token)
    if matches:
        analyses=[]
        for r in matches:
            analyses.append({'form':r['canonical_spelling'],'part_of_speech':r['part_of_speech'],
                             'segments':r.get('derivation',r['canonical_spelling']), 'gloss_tr':r['gloss_tr'], 'source_id':r['id']})
        return {'form':token,'analyses':analyses,'certainty':'attested'}
    result=analyze(token)
    candidates=result['candidates']
    for candidate in candidates:
        if 'base' in candidate:
            candidate['base_glosses_tr']=[r['gloss_tr'] for r in lookup(candidate['base'])]
    return {'form':token,'analyses':candidates,'certainty':result['status']}

def audit():
    rows=[json.loads(line) for line in (ROOT/'data/example-sentences.jsonl').read_text(encoding='utf-8').splitlines()]
    annotations=(ROOT/'audits/sentence-roles.tsv').read_text(encoding='utf-8').splitlines()
    if len(rows)!=len(annotations): raise ValueError('source/annotation count mismatch')
    output=[]
    for row,line in zip(rows,annotations):
        subject,predicate,obj,other,order=line.split('|')
        tokens=re.findall(r'[^\W\d_]+',row['canonical_spelling'],re.UNICODE)
        words=[normalize(x) for x in tokens]
        for part in [subject,predicate,obj]:
            for term in re.findall(r'[^\W\d_]+',part, re.UNICODE):
                if normalize(term) not in words and term not in {'omitted','imperative'}:
                    raise ValueError(f"#{row['number']} annotation refers to absent {term}")
        warnings=[]
        if row['number']==19: warnings.append('Quality describes being fearful; do not infer an exact emotional state.')
        if row['number']==35: warnings.append('Omitted object: no particular object can be recovered.')
        if row['number']==40: warnings.append('Possessive noun phrase, not a complete clause.')
        if row['number']==44: warnings.append('Comparison standard is omitted; interpretation depends on context.')
        if row['number'] in (58,82): warnings.append('Object belongs to the embedded verb, not the modal predicate.')
        if row['number']==66: warnings.append('Vocative does not by itself prove that the object refers to Elora.')
        if row['number']==93: warnings.append('Tense and subject apply separately to two clauses.')
        if row['number']==100: warnings.append('Source marks the phrase grammatically possible but semantically odd.')
        segments=[segmentation(t) for t in tokens]
        unknown=[s['form'] for s in segments if s['certainty']=='unknown']
        if unknown: warnings.append('Unresolved token analysis: '+', '.join(unknown))
        status='unsupported' if unknown else ('ambiguous' if row['number'] in (19,35,44,66) else 'valid')
        output.append({'source_id':row['id'],'number':row['number'],'source_line':row['provenance']['line'],
          'original':row['canonical_spelling'],'tokens':segments,'subject':subject,'predicate':predicate,
          'objects':obj,'other_roles':other,'word_order':order,
          'tense': 'past' if 'da' in words else 'future' if 'va' in words else 'unmarked/contextual',
          'aspect': next(({'du':'progressive','fa':'completed','su':'habitual'}[w] for w in words if w in ('du','fa','su')),'unmarked'),
          'negation': 'ne' in words,'turkish_gloss':row['gloss_tr'],
          'literal_interpretation': [{'token':s['form'], 'glosses_tr':[a.get('gloss_tr', a.get('base_glosses_tr', [])) for a in s.get('analyses', [])]} for s in segments],
          'status':status,'evidence':f"v1.0 §{row['provenance']['section']} line {row['provenance']['line']}; grammar §§3–4",
          'proposed_correction':None,'notes':warnings,
          'review_scope':'initial manual role review; literal gloss is a word-by-word aid, candidates and context remain uncertain'})
    return output

def main():
    rendered=''.join(json.dumps(r,ensure_ascii=False,sort_keys=True)+'\n' for r in audit())
    path=ROOT/'audits/sentence-audit.jsonl'
    if '--check' in sys.argv:
        if path.read_text(encoding='utf-8')!=rendered: raise SystemExit('audit differs')
    else: path.write_text(rendered,encoding='utf-8',newline='\n')
    print('Sentence audit rows:',len(audit()))
if __name__=='__main__': main()
