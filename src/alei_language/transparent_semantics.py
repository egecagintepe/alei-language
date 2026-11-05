from .lexicon import normalize, lookup
ROLES={'ro':'source_from','li':'typical_color','ze':'typical_taste','mu':'typical_shape','ku':'typical_texture','su':'typical_size','ge':'associated_location','pe':'purpose','di':'material_of','sa':'subtype_kind'}
TYPICAL={'li','ze','mu','ku','su'}
# Explicit, deliberately incomplete examples of the standard's type table.
RANGES={('meyar','ro'):{'savel','yenar'},('meyar','li'):{'reş','lüven','nüvil','şeral'},('meyar','ze'):{'selim','koral','püsel','zel'},('meyar','mu'):{'molir'},('meyar','ku'):{'firak','süval','toram'},('len','pe'):{'belem','ves','arim','nesar'},('len','di'):{'liman','süvar'},('famel','sa'):{'savel','melir','lera'},('melir','sa'):{'püra','zanar'},('savel','ge'):{'nasel'}}
def parse(text):
    parts=normalize(text).split('-')
    if len(parts)<3 or len(parts)%2==0 or any(not p for p in parts): raise ValueError('Expected HEAD-ROLE-VALUE pairs')
    head=parts[0]
    if not lookup(head): raise ValueError('Unknown head')
    relations=[]
    for role,value in zip(parts[1::2],parts[2::2]):
        if role not in ROLES: raise ValueError('Unknown or disabled role: '+role)
        if not lookup(value): raise ValueError('Unknown value: '+value)
        allowed=RANGES.get((head,role))
        status='verified_example' if allowed and value in allowed else 'unverified'
        # Known category mismatches are failures, but an incomplete enumeration cannot prove invalidity.
        if role=='li' and value=='hokar': raise ValueError('Known color type mismatch')
        relations.append({'role':role,'value':value,'relation':ROLES[role],'strength':'typical' if role in TYPICAL else 'asserted','type_status':status})
    return {'head':head,'relations':relations,'exact_identity_known':False,'warning':'Type examples are incomplete; asserted relations are not verified facts.'}
