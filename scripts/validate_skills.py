from pathlib import Path
import re, shutil, subprocess, sys
root=Path(__file__).resolve().parents[1]
paths=sorted((root/'.agents/skills').glob('*/SKILL.md'))
errors=[]
if len(paths)!=7: errors.append('Expected seven skills')
for path in paths:
    text=path.read_text(encoding='utf-8'); match=re.match(r'\A---\nname: ([^\n]+)\ndescription: ([^\n]+)\n---\n',text)
    if not match: errors.append(f'{path}: invalid supported frontmatter'); continue
    name,description=match.groups()
    if name!=path.parent.name or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',name) or len(name)>64: errors.append(f'{path}: invalid name')
    if not 1<=len(description)<=1024: errors.append(f'{path}: invalid description')
    for link in re.findall(r'\]\(([^)]+)\)',text):
        if not (path.parent/link).exists(): errors.append(f'{path}: missing {link}')
    if len(text.split('---',2)[-1].strip())<100: errors.append(f'{path}: empty instructions')
    if shutil.which('skills-ref'):
        if subprocess.run(['skills-ref','validate',str(path.parent)]).returncode: errors.append(f'{path}: skills-ref failed')
print('Validator:', 'skills-ref and local checks' if shutil.which('skills-ref') else 'local checks only (skills-ref unavailable)')
for e in errors: print(e)
print(f'{len(paths)} skills checked; {len(errors)} errors')
sys.exit(bool(errors))
