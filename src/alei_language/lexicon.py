from pathlib import Path
import json, unicodedata
ROOT = Path(__file__).resolve().parents[2]
def normalize(s):
    return unicodedata.normalize('NFC', s).translate(str.maketrans({'I':'ı','İ':'i'})).lower()
def records():
    for group in ('roots','lexemes','functions'):
        with (ROOT/'data'/f'{group}.jsonl').open(encoding='utf-8') as f:
            yield from (json.loads(line) for line in f if line.strip())
def lookup(word):
    return [r for r in records() if normalize(r['canonical_spelling']) == normalize(word)]
