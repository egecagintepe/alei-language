"""Generate the v1.1 view from immutable v1.0 data and explicit owner decisions."""
from pathlib import Path
import hashlib,json,sys
ROOT=Path(__file__).resolve().parents[1]
def read(name):
 return [json.loads(s) for s in (ROOT/'data'/f'{name}.jsonl').read_text(encoding='utf-8').splitlines()]
def render(rows): return ''.join(json.dumps(r,ensure_ascii=False,sort_keys=True)+'\n' for r in rows)
def text_hash(path):
 return hashlib.sha256(path.read_text(encoding='utf-8-sig').encode('utf-8')).hexdigest()
def build():
 overlay=json.loads((ROOT/'standard/versions/1.1.0.json').read_text(encoding='utf-8-sig'))
 if (overlay['language_name']!='Alei' or overlay['preferred_help_root']!='Mirav' or
     overlay['preferred_help_verb']!='Miraven' or overlay['legacy_aliases']!={'Mivav':'Mirav','Mivaven':'Miraven'} or
     overlay['historical_pending']!=['Mivavar'] or overlay['unadopted_candidates']!=['Miravar']):
  raise ValueError('overlay differs from implemented owner decisions')
 raw=(ROOT/'standard/adsiz_dil_acik_anlam_standardi_v1_0.md').read_bytes()
 if hashlib.sha256(raw).hexdigest()!=overlay['base_sha256']: raise ValueError('v1.0 checksum mismatch')
 roots=read('roots'); lexemes=read('lexemes')
 def one(rows,name):
  found=[r for r in rows if r['canonical_spelling']==name]
  if len(found)!=1: raise ValueError('expected one historical record: '+name)
  return found[0]
 oldroot=one(roots,'Mivav'); oldverb=one(lexemes,'Mivaven'); oldagent=one(lexemes,'Mivavar')
 def preferred(old,name,kind):
  r=dict(old); r.update({'id':'ad:1.1.0:'+kind+':'+name.lower(),'canonical_spelling':name,
       'status':'owner_adopted','version':'1.1.0','decision_id':'AD-2026-002',
       'provenance':{'file':'governance/decisions/2026-11-05.json','decision':'AD-2026-002'},
       'historical_reference':{'id':old['id'],'provenance':old['provenance']}})
  if kind=='lexeme': r['derivation']='Mirav+-en'
  return r
 def alias(old,preferred):
  r=dict(old);r.update({'status':'legacy_alias','language_version':'1.1.0','preferred_form':preferred,
       'warning':f'Legacy v1.0 spelling; preferred v1.1.0 form: {preferred}.','decision_id':'AD-2026-002'})
  return r
 pending=dict(oldagent);pending.update({'status':'historical_v1_pending','language_version':'1.1.0',
  'warning':'Historical v1.0 form; v1.1.0 status remains undecided. Miravar is not adopted.'})
 newroots=[preferred(r,'Mirav','root') if r['id']==oldroot['id'] else r for r in roots]
 newlex=[preferred(r,'Miraven','lexeme') if r['id']==oldverb['id'] else r for r in lexemes if r['id']!=oldagent['id']]
 return {'roots':newroots,'lexemes':newlex,'compatibility':[alias(oldroot,'Mirav'),alias(oldverb,'Miraven'),pending]}
def main():
 check='--check' in sys.argv; errors=[]; groups=build()
 for name,rows in groups.items():
  path=ROOT/'data/versions/1.1.0'/f'{name}.jsonl';content=render(rows)
  if check:
   if not path.exists() or path.read_text(encoding='utf-8')!=content:errors.append(str(path))
  else:path.write_text(content,encoding='utf-8',newline='\n')
  print(name,len(rows))
 manifest={'text_hash_normalization':'UTF-8, LF, no BOM', 'language_version':'1.1.0','base_sha256':json.loads((ROOT/'standard/versions/1.1.0.json').read_text(encoding='utf-8-sig'))['base_sha256'],
           'overlay_sha256':text_hash(ROOT/'standard/versions/1.1.0.json'),
           'decisions_sha256':text_hash(ROOT/'governance/decisions/2026-11-05.json'),
           'inherited_functions_sha256':text_hash(ROOT/'data/functions.jsonl'),
           'counts':{k:len(v) for k,v in groups.items()},
           'files':{k+'.jsonl':hashlib.sha256(render(v).encode('utf-8')).hexdigest() for k,v in groups.items()}}
 path=ROOT/'data/versions/1.1.0/manifest.json';content=json.dumps(manifest,ensure_ascii=False,sort_keys=True,indent=2)+'\n'
 if check:
  if not path.exists() or path.read_text(encoding='utf-8')!=content: errors.append(str(path))
 else:path.write_text(content,encoding='utf-8',newline='\n')
 if errors: raise SystemExit('mismatch: '+', '.join(errors))
if __name__=='__main__': main()
