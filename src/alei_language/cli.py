import argparse,json,sys
from .lexicon import lookup
from .morphology import analyze
from .transparent_semantics import parse
from .audit import validate
from .grammar import parse_clause, parse_sentence
def main():
    p=argparse.ArgumentParser(prog='alei'); sub=p.add_subparsers(dest='command',required=True)
    sub.add_parser('validate')
    for name in ('lookup','analyze','parse-semantic','parse-clause','parse-sentence'):
        q=sub.add_parser(name); q.add_argument('text')
    args=p.parse_args()
    try:
        result=validate() if args.command=='validate' else lookup(args.text) if args.command=='lookup' else analyze(args.text) if args.command=='analyze' else parse(args.text) if args.command=='parse-semantic' else parse_clause(args.text) if args.command=='parse-clause' else parse_sentence(args.text)
        print(json.dumps(result,ensure_ascii=False,indent=2))
    except (ValueError,OSError) as e: print(str(e),file=sys.stderr); return 1
    return 0
if __name__=='__main__': raise SystemExit(main())
