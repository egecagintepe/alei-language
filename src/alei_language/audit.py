import hashlib,json,subprocess,sys
from .lexicon import ROOT
def validate():
    manifest=json.loads((ROOT/'standard/manifest.json').read_text(encoding='utf-8'))
    standard=ROOT/'standard'/manifest['standard']['file']
    if hashlib.sha256(standard.read_bytes()).hexdigest()!=manifest['standard']['sha256']: raise ValueError('Standard checksum mismatch')
    subprocess.run([sys.executable,str(ROOT/'scripts/derive_data.py'),'--check'],check=True)
    return 'Source checksum and source-derived rows match; linguistic correctness requires human review.'
