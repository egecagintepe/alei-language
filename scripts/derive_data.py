from pathlib import Path
import json, hashlib, re
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'standard/adsiz_dil_acik_anlam_standardi_v1_0.md'
def derive():
    out={'roots':[], 'lexemes':[], 'functions':[], 'example-sentences':[]}
    section=''
    for n,line in enumerate(SOURCE.read_text(encoding='utf-8-sig').splitlines(),1):
        m=re.match(r'### (7\.\d+|8\.\d+|9\.\d+)\b',line)
        if m: section=m.group(1)
        if line.startswith('## ') and not line.startswith('### '): section=''
        if not line.startswith('|'): continue
        cols=[x.strip() for x in line.strip().strip('|').split('|')]
        if len(cols)<3 or cols[0].startswith('---'): continue
        group=None
        if section.startswith('7.') and len(cols)==4 and cols[3] in ('K','O','D'):
            group='roots'; form,gloss,anchor,code=cols
            extra={'semantic_anchor_en':anchor,'status':{'K':'owner_locked','O':'owner_accepted_working','D':'delegated_v1'}[code], 'part_of_speech':'root'}
        elif section in ('8.1','8.2','8.3','8.4','8.5') and len(cols)==3 and cols[0] not in ('Sözcük','Bitişik sözcük'):
            group='lexemes'; form=cols[0]
            gloss=cols[2] if section=='8.5' else cols[1]
            extra={'derivation':cols[1] if section=='8.5' else cols[2], 'part_of_speech':{'8.1':'verb','8.2':'quality','8.3':'agent_noun','8.4':'event_noun','8.5':'compound'}[section], 'status':'attested_v1'}
        elif section=='8.6' and len(cols)==3 and cols[0]!='Biçim':
            group='functions'; form,gloss,pos=cols; extra={'part_of_speech':pos,'status':'attested_v1'}
        elif section.startswith('9.') and cols[0].isdigit() and len(cols)==3:
            group='example-sentences'; form,gloss=cols[1:]; extra={'number':int(cols[0]),'part_of_speech':'sentence','status':'attested_v1'}
        if group:
            record={'id':f'{group}:{n}', 'canonical_spelling':form, 'gloss_tr':gloss, 'version':'1.0','provenance':{'file':'standard/adsiz_dil_acik_anlam_standardi_v1_0.md','line':n,'section':section},**extra}
            out[group].append(record)
    return out
def render(items): return ''.join(json.dumps(x,ensure_ascii=False,sort_keys=True)+'\n' for x in items)
def main():
    import argparse
    p=argparse.ArgumentParser(); p.add_argument('--check',action='store_true'); a=p.parse_args(); failed=False
    for group,items in derive().items():
        path=ROOT/'data'/f'{group}.jsonl'; content=render(items)
        if a.check:
            if not path.exists() or path.read_text(encoding='utf-8')!=content: print(f'MISMATCH {path}'); failed=True
        else:
            path.parent.mkdir(exist_ok=True); path.write_text(content,encoding='utf-8',newline='\n')
        print(f'{group}: {len(items)}')
    raise SystemExit(1 if failed else 0)
if __name__=='__main__': main()
