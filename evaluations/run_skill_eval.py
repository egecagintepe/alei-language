"""Print evaluation prompts or check a human-recorded response file's coverage.

No model is called and no responses are scored automatically.
"""
import argparse, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--responses',type=Path,help='JSONL with id, output, model, settings and reviewer_notes')
    args=parser.parse_args()
    cases=[json.loads(s) for s in (ROOT/'evaluations/skill-cases.jsonl').read_text(encoding='utf-8-sig').splitlines() if s.strip()]
    if not args.responses:
        for case in cases: print(json.dumps(case,ensure_ascii=False))
        print('No model invoked; expected outputs are human review criteria.',file=__import__('sys').stderr)
        return
    responses=[json.loads(s) for s in args.responses.read_text(encoding='utf-8-sig').splitlines() if s.strip()]
    required={'id','output','model','settings','reviewer_notes'}
    ids=[r.get('id') for r in responses]
    missing={c['id'] for c in cases}-set(ids); extra=set(ids)-{c['id'] for c in cases}
    bad=[r.get('id') for r in responses if not required.issubset(r) or not all(r.get(k) for k in required)]
    if missing or extra or bad or len(ids)!=len(set(ids)):
        raise SystemExit(f'Incomplete records: missing={sorted(missing)}, extra={sorted(extra)}, bad={bad}, duplicates={len(ids)!=len(set(ids))}')
    print(f'{len(responses)} response records present; human assessment still required; no score computed.')
if __name__=='__main__': main()
