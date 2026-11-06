import argparse,json,sys
from .lexicon import lookup
from .morphology import analyze
from .transparent_semantics import parse
from .audit import validate
from .grammar import parse_clause, parse_sentence, parse_alei

def main():
    p=argparse.ArgumentParser(prog='alei'); sub=p.add_subparsers(dest='command',required=True)
    sub.add_parser('validate')
    for name in ('lookup','analyze','parse-semantic','parse-clause','parse-sentence','parse-ast'):
        q=sub.add_parser(name); q.add_argument('text')
        if name!='parse-semantic':
            q.add_argument('--version',choices=('1.0','1.1.0','current'),default='1.0',help='Language version (default: 1.0 for compatibility)')
        if name=='parse-ast':
            q.add_argument('--mode',choices=('standard','experimental'),default='standard',help='Grammar parsing mode')
    args=p.parse_args()
    try:
        if args.command=='validate': result=validate()
        elif args.command=='parse-semantic': result=parse(args.text)
        elif args.command=='lookup': result=lookup(args.text,version=args.version)
        elif args.command=='analyze': result=analyze(args.text,version=args.version)
        elif args.command=='parse-clause': result=parse_clause(args.text,version=args.version)
        elif args.command=='parse-ast': result=parse_alei(args.text,version=args.version,mode=args.mode).to_dict()
        else: result=parse_sentence(args.text,version=args.version)
        print(json.dumps(result,ensure_ascii=False,indent=2))
    except (ValueError,OSError) as e: print(str(e),file=sys.stderr); return 1
    return 0
if __name__=='__main__': raise SystemExit(main())
