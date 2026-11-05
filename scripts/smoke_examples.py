from pathlib import Path
import json,re,sys
from alei_language.orthography import validate
ROOT=Path(__file__).resolve().parents[1]
def check():
    rows=[json.loads(s) for s in (ROOT/'data/example-sentences.jsonl').read_text(encoding='utf-8').splitlines()]
    issues=[]
    for row in rows:
        for word in re.findall(r'[^\W\d_]+',row['canonical_spelling'],re.UNICODE):
            errors=validate(word)
            if errors: issues.append((row['number'],word,errors))
    return rows,issues
if __name__=='__main__':
    rows,issues=check()
    print(f'{len(rows)} sentence rows checked for alphabet and adjacent-letter runs; {len(issues)} flagged tokens. Not a grammar or translation audit.')
    for issue in issues: print(issue)
    sys.exit(bool(issues))
