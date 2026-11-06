from pathlib import Path
import json, unicodedata
ROOT = Path(__file__).resolve().parents[2]
def normalize(s):
    return unicodedata.normalize('NFC', s).translate(str.maketrans({'I':'ı','İ':'i'})).lower()
def resolve_version(version='1.0'):
    if version=='current':
        version=json.loads((ROOT/'standard/current.json').read_text(encoding='utf-8-sig'))['current_language_version']
    if version not in ('1.0','1.1.0'): raise ValueError('Unsupported language version: '+str(version))
    return version
def records(version='1.0', include_compatibility=False):
    version=resolve_version(version)
    for group in ('roots','lexemes','functions'):
        path=(ROOT/'data'/f'{group}.jsonl') if version=='1.0' or group=='functions' else (ROOT/'data/versions'/version/f'{group}.jsonl')
        with path.open(encoding='utf-8') as f:
            yield from (json.loads(line) for line in f if line.strip())
    if version=='1.1.0' and include_compatibility:
        with (ROOT/'data/versions'/version/'compatibility.jsonl').open(encoding='utf-8') as f:
            yield from (json.loads(line) for line in f if line.strip())
def lookup(word,version='1.0'):
    return [r for r in records(version,include_compatibility=True) if normalize(r['canonical_spelling'])==normalize(word)]
