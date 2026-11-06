"""Conservative, explicitly incomplete v1.0 transparent semantics.

Type annotations describe known examples, not an exhaustive ontology or facts
about the world. Source: standard v1.0 sections 5.2–5.5.
"""
from .lexicon import normalize, lookup

ROLES = {'ro':'source_from','li':'typical_color','ze':'typical_taste',
         'mu':'typical_shape','ku':'typical_texture','su':'typical_size',
         'ge':'associated_location','pe':'purpose','di':'material_of',
         'sa':'subtype_kind'}
TYPICAL = {'li','ze','mu','ku','su'}
# Positive evidence; these are multi-label, not a closed-world type hierarchy.
CLASSES = {
    'savel': {'plant', 'organism'}, 'yenar': {'plant', 'organism'},
    'famel': {'organism'}, 'melir': {'organism', 'animal'},
    'lera': {'organism'}, 'püra': {'animal'}, 'zanar': {'animal'},
    'reş': {'color'}, 'lüven': {'color'}, 'nüvil': {'color'},
    'şeral': {'color'}, 'hüsen': {'color'}, 'morun': {'color'},
    'selim': {'taste'}, 'koral': {'taste'}, 'püsel': {'taste'}, 'zel': {'taste'},
    'molir': {'shape'}, 'firak': {'texture'}, 'süval': {'texture'}, 'toram': {'texture'},
    'lavar': {'size'}, 'mir': {'size'}, 'nasel': {'location'},
    'belem': {'function'}, 'ves': {'function'}, 'arim': {'function'}, 'nesar': {'function'},
    'liman': {'material'}, 'süvar': {'material'}, 'hokar': {'emotion'},
}
EXPECTED = {'li':'color','ze':'taste','mu':'shape','ku':'texture','su':'size'}
# Negative evidence is explicit; absence from CLASSES is never a type error.
KNOWN_INVALID = {('li','hokar')}
RANGES = {
    ('meyar','ro'):{'savel','yenar'}, ('meyar','li'):{'reş','lüven','nüvil','şeral'},
    ('meyar','ze'):{'selim','koral','püsel','zel'}, ('meyar','mu'):{'molir'},
    ('meyar','ku'):{'firak','süval','toram'}, ('len','pe'):{'belem','ves','arim','nesar'},
    ('len','di'):{'liman','süvar'}, ('famel','sa'):{'savel','melir','lera'},
    ('melir','sa'):{'püra','zanar'}, ('savel','ge'):{'nasel'},
}

def _attested_root(word):
    return any(record['part_of_speech']=='root' for record in lookup(word))

def parse(text):
    if not isinstance(text, str):
        raise ValueError('Expected a string')
    parts = normalize(text).split('-')
    if len(parts)<3 or len(parts)%2==0 or any(not part for part in parts):
        raise ValueError('Expected HEAD-ROLE-VALUE pairs')
    head = parts[0]
    if not _attested_root(head):
        raise ValueError('Unknown or unregistered root head')
    relations=[]
    warnings=[]
    seen={}
    for role,value in zip(parts[1::2],parts[2::2]):
        if role not in ROLES:
            raise ValueError('Unknown or disabled role: '+role)
        if not _attested_root(value):
            raise ValueError('Unknown or unregistered root value: '+value)
        if (role,value) in KNOWN_INVALID:
            raise ValueError('Known color type mismatch')
        if value in seen.get(role,set()):
            warnings.append('Repeated identical relation: '+role+'-'+value)
        elif role in seen:
            warnings.append('Multiple values for '+role+'; compatibility is not established')
        seen.setdefault(role,set()).add(value)
        allowed=RANGES.get((head,role),set())
        if value in allowed:
            status='verified_example'
        elif EXPECTED.get(role) in CLASSES.get(value,set()):
            status='value_class_known_head_compatibility_unverified'
        else:
            status='unverified'
        relations.append({'role':role,'value':value,'relation':ROLES[role],
                          'strength':'typical' if role in TYPICAL else 'asserted',
                          'type_status':status})
    return {'head':head,'relations':relations,'exact_identity_known':False,
            'warnings':warnings,
            'warning':'Type examples are incomplete; asserted relations are not verified facts.'}

def compose(head, relations):
    """Serialize validated role/value pairs without inferring an identity."""
    if not isinstance(head,str) or not isinstance(relations,list) or not relations:
        raise ValueError('Expected a head and nonempty relation list')
    pieces=[head]
    for item in relations:
        if not isinstance(item,dict) or set(item)!={'role','value'}:
            raise ValueError('Relations must contain only role and value')
        role,value=item['role'],item['value']
        if not isinstance(role,str) or not isinstance(value,str) or '-' in role or '-' in value:
            raise ValueError('Invalid role or value')
        pieces.extend((role,value))
    text=normalize('-'.join(pieces))
    parse(text)
    return text
