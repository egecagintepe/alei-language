"""Restricted demonstration of the two historical/current help examples."""
from .grammar import parse_sentence

def translate_help_example(text,version='1.0'):
    parsed=parse_sentence(text,version=version)
    if parsed.get('status')!='parsed': return {'status':'unsupported'}
    a=parsed['analysis']
    forms={('mei','unmarked'):('Sana yardım ediyorum.','I help you.'),
           ('eli','va'):('O sana yardım edecek.','They will help you.')}
    key=(a.get('subject'),a.get('tense'))
    if a.get('verb') not in ('mivaven','miraven') or a.get('object')!='sai' or a.get('negation') or a.get('aspect')!='unmarked' or key not in forms or a.get('question'):
        return {'status':'unsupported'}
    tr,en=forms[key]
    return {'status':'translated','tr':tr,'en':en,'scope':'restricted help examples; not a general translator',
            'object_focus':a.get('order')=='SOV','warnings':parsed.get('warnings',[])}
