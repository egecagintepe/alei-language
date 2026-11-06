"""Machine-readable lexeme valency register and argument-frame verification.

Preserves canonical v1.0 and v1.1 definitions without inventing unapproved senses.
Transitive verbs remain transitive; omitted arguments are flagged explicitly as
ellipsis or valency friction.
"""
from typing import Dict, List, Any, Optional

# Canonical valency frames for core Alei verbs based on v1.0 / v1.1 standards
VERB_VALENCY_FRAMES: Dict[str, Dict[str, Any]] = {
    'nesalen': {
        'class': 'transitive',
        'roles': ['Agent', 'Patient'],
        'obligatory': ['Agent', 'Patient'],
        'subject_role': 'Agent',
        'gloss_tr': 'kaybetmek',
        'semantic_note': 'Strictly transitive in canon. Does not inherently encode inchoative disappear (kaybolmak).'
    },
    'liren': {
        'class': 'transitive',
        'roles': ['Experiencer', 'Stimulus'],
        'obligatory': ['Experiencer', 'Stimulus'],
        'subject_role': 'Experiencer',
        'gloss_tr': 'görmek',
        'semantic_note': 'Perceptual transitive verb.'
    },
    'sileven': {
        'class': 'transitive',
        'roles': ['Agent', 'Patient'],
        'obligatory': ['Agent', 'Patient'],
        'subject_role': 'Agent',
        'gloss_tr': 'yapmak / üretmek',
        'semantic_note': 'Causative/productive transitive verb.'
    },
    'belemen': {
        'class': 'transitive',
        'roles': ['Agent', 'Patient'],
        'obligatory': ['Agent'],
        'optional': ['Patient'],
        'subject_role': 'Agent',
        'gloss_tr': 'saymak / hesaplamak',
        'semantic_note': 'Agent computing or counting; patient may be unexpressed count-domain.'
    },
    'hüvaren': {
        'class': 'transitive',
        'roles': ['Agent', 'Patient'],
        'obligatory': ['Agent', 'Patient'],
        'subject_role': 'Agent',
        'gloss_tr': 'aramak',
        'semantic_note': 'Search verb. Omitting the patient leaves target entity unexpressed.'
    },
    'avelen': {
        'class': 'intransitive',
        'roles': ['Agent', 'Destination'],
        'obligatory': ['Agent'],
        'optional': ['Destination'],
        'subject_role': 'Agent',
        'gloss_tr': 'gelmek / girmek',
        'semantic_note': 'Motion verb with optional destination marked by postposition ta.'
    },
    'vürelen': {
        'class': 'intransitive',
        'roles': ['Agent', 'Path'],
        'obligatory': ['Agent'],
        'optional': ['Path'],
        'subject_role': 'Agent',
        'gloss_tr': 'geçmek / aşmak',
        'semantic_note': 'Motion across a barrier or bridge.'
    },
    'aremen': {
        'class': 'intransitive',
        'roles': ['Agent', 'Destination'],
        'obligatory': ['Agent'],
        'optional': ['Destination'],
        'subject_role': 'Agent',
        'gloss_tr': 'dönmek / geri gelmek',
        'semantic_note': 'Return motion verb.'
    },
    'pürelen': {
        'class': 'intransitive',
        'roles': ['Agent', 'Destination'],
        'obligatory': ['Agent', 'Destination'],
        'subject_role': 'Agent',
        'gloss_tr': 'ulaşmak / varmak',
        'semantic_note': 'Arrival verb requiring destination marked with ta.'
    },
    'nivaren': {
        'class': 'intransitive',
        'roles': ['Agent', 'Duration'],
        'obligatory': ['Agent'],
        'optional': ['Duration'],
        'subject_role': 'Agent',
        'gloss_tr': 'gecelemek / gece beklemek',
        'semantic_note': 'Temporal duration verb.'
    },
    'vesen': {
        'class': 'communicative',
        'roles': ['Agent', 'Recipient', 'Message'],
        'obligatory': ['Agent'],
        'optional': ['Recipient', 'Message'],
        'subject_role': 'Agent',
        'gloss_tr': 'söylemek / demek',
        'semantic_note': 'Speech act verb; can govern direct quote or ke embedded clause.'
    },
    'miraven': {
        'class': 'transitive_benefactive',
        'roles': ['Agent', 'Beneficiary'],
        'obligatory': ['Agent'],
        'optional': ['Beneficiary'],
        'subject_role': 'Agent',
        'gloss_tr': 'yardım etmek',
        'semantic_note': 'Approved v1.1.0 preferred help verb.'
    },
    'mivaven': {
        'class': 'transitive_benefactive',
        'roles': ['Agent', 'Beneficiary'],
        'obligatory': ['Agent'],
        'optional': ['Beneficiary'],
        'subject_role': 'Agent',
        'gloss_tr': 'yardım etmek (legacy alias)',
        'semantic_note': 'Legacy v1.0 alias for miraven.'
    },
    'yelaren': {
        'class': 'transitive',
        'roles': ['Agent', 'Patient', 'Surface'],
        'obligatory': ['Agent'],
        'optional': ['Patient', 'Surface'],
        'subject_role': 'Agent',
        'gloss_tr': 'yazmak',
        'semantic_note': 'Inscribing verb; Patient = inscription/text, Surface = lo substrate.'
    },
    'naelen': {
        'class': 'modal_transitive',
        'roles': ['Experiencer', 'Goal'],
        'obligatory': ['Experiencer', 'Goal'],
        'subject_role': 'Experiencer',
        'gloss_tr': 'istemek',
        'semantic_note': 'Modal volition verb taking ke complement or marked nominal object.'
    },
    'yelen': {
        'class': 'modal_auxiliary',
        'roles': ['Agent', 'Ability'],
        'obligatory': ['Agent', 'Ability'],
        'subject_role': 'Agent',
        'gloss_tr': 'yapabilmek / muktedir olmak',
        'semantic_note': 'Modal dynamic ability verb taking ke complement.'
    },
    'ünaren': {
        'class': 'modal_epistemic',
        'roles': ['Experiencer', 'Proposition'],
        'obligatory': ['Experiencer', 'Proposition'],
        'subject_role': 'Experiencer',
        'gloss_tr': 'bilmek',
        'semantic_note': 'Epistemic verb governing ke complement.'
    }
}

def get_valency_frame(verb_lemma: str) -> Optional[Dict[str, Any]]:
    """Retrieve canonical valency frame for a verb lemma."""
    return VERB_VALENCY_FRAMES.get(verb_lemma.lower())

def evaluate_valency(verb_lemma: str, overt_roles: Dict[str, str], voice: str = 'active') -> Dict[str, Any]:
    """Check whether provided arguments satisfy the verb's canonical valency frame.

    Does not modify canon or guess unexpressed identities.
    """
    frame = get_valency_frame(verb_lemma)
    if not frame:
        return {
            'status': 'unregistered_verb',
            'valency_satisfied': True,
            'notes': [f"Verb lemma '{verb_lemma}' has no registered valency schema in v1.1."]
        }

    obligatory = list(frame.get('obligatory', []))
    optional = list(frame.get('optional', []))
    notes = []

    # Voice adjustment in experimental mode
    if voice == 'middle':
        # Middle voice suppresses external agent and promotes patient to subject
        if 'Agent' in obligatory:
            obligatory.remove('Agent')
        # Patient is the obligatory promoted subject role
        if 'Patient' not in obligatory and 'Patient' in frame.get('roles', []):
            obligatory.append('Patient')
        notes.append("Middle voice suppresses canonical external Agent requirement and promotes Patient to subject.")


    missing = [role for role in obligatory if role not in overt_roles]
    extraneous = [role for role in overt_roles if role not in obligatory and role not in optional]

    if missing:
        if voice == 'active' and verb_lemma == 'nesalen' and 'Patient' in missing:
            notes.append("Valency defect: Transitive 'nesalen' requires overt Patient. Subject cannot be parsed as patient without middle voice.")
            status = 'valency_clash'
        else:
            notes.append(f"Omitted obligatory argument(s): {', '.join(missing)} (contextual ellipsis or zero-anaphora).")
            status = 'omitted_argument'
        satisfied = False
    elif extraneous:
        notes.append(f"Unexpected argument role(s) for verb: {', '.join(extraneous)}.")
        status = 'unexpected_argument'
        satisfied = False
    else:
        status = 'satisfied'
        satisfied = True

    return {
        'status': status,
        'valency_satisfied': satisfied,
        'frame_class': frame['class'],
        'subject_role': frame.get('subject_role', 'Agent'),
        'missing_roles': missing,
        'notes': notes
    }
