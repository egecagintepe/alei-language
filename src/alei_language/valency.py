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
        'semantic_note': 'Strictly transitive in canon (roots:525). Does not inherently encode inchoative disappear (kaybolmak).'
    },
    'liren': {
        'class': 'transitive',
        'roles': ['Experiencer', 'Stimulus'],
        'obligatory': ['Experiencer', 'Stimulus'],
        'subject_role': 'Experiencer',
        'gloss_tr': 'görmek',
        'semantic_note': 'Perceptual transitive verb (roots:514).'
    },
    'sileven': {
        'class': 'transitive',
        'roles': ['Agent', 'Patient'],
        'obligatory': ['Agent', 'Patient'],
        'subject_role': 'Agent',
        'gloss_tr': 'okumak',
        'semantic_note': 'Canonical reading verb (roots:508, lexemes:793). §4.2: Sai da sileven tüvanan = Kitabı okudun.'
    },
    'belemen': {
        'class': 'transitive',
        'roles': ['Agent', 'Patient'],
        'obligatory': ['Agent'],
        'optional': ['Patient'],
        'subject_role': 'Agent',
        'gloss_tr': 'saymak / hesaplamak',
        'semantic_note': 'Agent computing or counting (roots:446); patient may be unexpressed count-domain.'
    },
    'hüvaren': {
        'class': 'transitive',
        'roles': ['Agent', 'Patient'],
        'obligatory': ['Agent', 'Patient'],
        'subject_role': 'Agent',
        'gloss_tr': 'aramak / araştırmak',
        'semantic_note': 'Search verb (roots:524). Omitting the patient leaves target entity unexpressed.'
    },
    'avelen': {
        'class': 'intransitive',
        'roles': ['Agent', 'Destination', 'Theme'],
        'obligatory': ['Agent'],
        'optional': ['Destination', 'Theme'],
        'subject_role': 'Agent',
        'gloss_tr': 'gitmek / yönelmek',
        'semantic_note': 'Motion verb (roots:432, lexemes:755). Destination marked by postposition ta. Undergoes inchoative periphrasis as auxiliary.'
    },
    'pürelen': {
        'class': 'intransitive',
        'roles': ['Agent', 'Destination'],
        'obligatory': ['Agent'],
        'optional': ['Destination'],
        'subject_role': 'Agent',
        'gloss_tr': 'gelmek / ulaşmak',
        'semantic_note': 'Arrival motion verb (roots:431, lexemes:754). Destination marked by ta.'
    },
    'nelaren': {
        'class': 'intransitive',
        'roles': ['Agent', 'Destination'],
        'obligatory': ['Agent'],
        'optional': ['Destination'],
        'subject_role': 'Agent',
        'gloss_tr': 'geri dönmek',
        'semantic_note': 'Canonical return verb (roots:433 Nelar, lexemes:756 Nelaren).'
    },
    'aremen': {
        'class': 'cognitive',
        'roles': ['Experiencer', 'Proposition'],
        'obligatory': ['Experiencer'],
        'optional': ['Proposition'],
        'subject_role': 'Experiencer',
        'gloss_tr': 'düşünmek',
        'semantic_note': 'Canonical thinking verb (roots:434 Arem, lexemes:757 Aremen). Not returning.'
    },
    'vürelen': {
        'class': 'experiential',
        'roles': ['Experiencer', 'Stimulus'],
        'obligatory': ['Experiencer'],
        'optional': ['Stimulus'],
        'subject_role': 'Experiencer',
        'gloss_tr': 'korkmak',
        'semantic_note': 'Canonical fearing verb (roots:502 Vürel, lexemes:787 Vürelen). Not crossing.'
    },
    'nivaren': {
        'class': 'cognitive',
        'roles': ['Agent', 'Patient'],
        'obligatory': ['Agent'],
        'optional': ['Patient'],
        'subject_role': 'Agent',
        'gloss_tr': 'öğrenmek',
        'semantic_note': 'Canonical learning verb (roots:721 Nivar, lexemes:921 Nivaren). Not nightwatching.'
    },
    'vesen': {
        'class': 'communicative',
        'roles': ['Agent', 'Recipient', 'Message'],
        'obligatory': ['Agent'],
        'optional': ['Recipient', 'Message'],
        'subject_role': 'Agent',
        'gloss_tr': 'söylemek / konuşmak',
        'semantic_note': 'Canonical speech verb (roots:448 Ves, lexemes:770 Vesen).'
    },
    'miraven': {
        'class': 'transitive_benefactive',
        'roles': ['Agent', 'Beneficiary'],
        'obligatory': ['Agent'],
        'optional': ['Beneficiary'],
        'subject_role': 'Agent',
        'gloss_tr': 'yardım etmek',
        'semantic_note': 'Approved v1.1.0 preferred help verb (AD-2026-002).'
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
    'saelen': {
        'class': 'transitive',
        'roles': ['Experiencer', 'Patient'],
        'obligatory': ['Experiencer', 'Patient'],
        'subject_role': 'Experiencer',
        'gloss_tr': 'sevmek',
        'semantic_note': 'Canonical affection verb (roots:430 Sael, lexemes:753 Saelen). §4.2: Mei saelen sain.'
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
    },
    'davelen': {
        'class': 'ditransitive',
        'roles': ['Agent', 'Patient', 'Recipient'],
        'obligatory': ['Agent', 'Patient'],
        'optional': ['Recipient'],
        'subject_role': 'Agent',
        'gloss_tr': 'vermek',
        'semantic_note': 'Canonical giving verb (roots:527 Dav, lexemes:806 Davelen). Recipient marked with ta.'
    },
    'javen': {
        'class': 'transitive',
        'roles': ['Agent', 'Patient'],
        'obligatory': ['Agent', 'Patient'],
        'subject_role': 'Agent',
        'gloss_tr': 'yapmak / üretmek',
        'semantic_note': 'Canonical production verb (roots:447 Jav, lexemes:784 Javen).'
    },
    'dumen': {
        'class': 'transitive',
        'roles': ['Agent', 'Patient'],
        'obligatory': ['Agent', 'Patient'],
        'subject_role': 'Agent',
        'gloss_tr': 'kapatmak',
        'semantic_note': 'Canonical closing verb (roots:517 Dum, lexemes:797 Dumen).'
    },
    'falen': {
        'class': 'transitive',
        'roles': ['Agent', 'Patient'],
        'obligatory': ['Agent', 'Patient'],
        'subject_role': 'Agent',
        'gloss_tr': 'açmak',
        'semantic_note': 'Canonical opening verb (roots:516 Fal, lexemes:796 Falen).'
    },
    'lümalen': {
        'class': 'transitive',
        'roles': ['Agent', 'Patient'],
        'obligatory': ['Agent', 'Patient'],
        'subject_role': 'Agent',
        'gloss_tr': 'onarmak',
        'semantic_note': 'Canonical repair verb (roots:667 Lümal, lexemes:899 Lümalen).'
    },
    'revalen': {
        'class': 'communicative',
        'roles': ['Agent', 'Recipient', 'Message'],
        'obligatory': ['Agent'],
        'optional': ['Recipient', 'Message'],
        'subject_role': 'Agent',
        'gloss_tr': 'yanıtlamak / cevap vermek',
        'semantic_note': 'Canonical answering verb (roots:443 Reval, lexemes:766 Revalen).'
    },
    'şürelen': {
        'class': 'intransitive',
        'roles': ['Agent'],
        'obligatory': ['Agent'],
        'subject_role': 'Agent',
        'gloss_tr': 'ayakta durmak',
        'semantic_note': 'Canonical posture verb (roots:659 Şürel, lexemes:891 Şürelen).'
    }
}

def get_valency_frame(verb_lemma: str) -> Optional[Dict[str, Any]]:
    """Retrieve canonical valency frame for a verb lemma."""
    return VERB_VALENCY_FRAMES.get(verb_lemma.lower())

def evaluate_valency(verb_lemma: str, overt_roles: Dict[str, str], voice: str = 'active') -> Dict[str, Any]:
    """Check whether provided arguments satisfy the verb's canonical valency frame.

    Does not modify canon or guess unexpressed identities.
    Unregistered verbs never satisfy valency.
    """
    frame = get_valency_frame(verb_lemma)
    if not frame:
        return {
            'status': 'unregistered_verb',
            'valency_satisfied': False,
            'frame_class': 'unregistered',
            'subject_role': 'Agent',
            'missing_roles': [],
            'notes': [f"Verb lemma '{verb_lemma}' has no registered valency schema in v1.1; cannot satisfy valency."]
        }

    obligatory = list(frame.get('obligatory', []))
    optional = list(frame.get('optional', []))
    notes = []

    # Voice modulation logic
    if voice in ('middle', 'passive'):
        if 'Patient' not in frame.get('roles', []):
            notes.append(f"Invalid voice derivation: Intransitive verb '{verb_lemma}' lacks a Patient role and cannot undergo passive or middle voice.")
            return {
                'status': 'invalid_voice_derivation',
                'valency_satisfied': False,
                'frame_class': frame['class'],
                'subject_role': frame.get('subject_role', 'Agent'),
                'missing_roles': [],
                'notes': notes
            }
        notes.append("Passive/Middle voice: External Agent requirement suppressed; Patient promoted to Subject.")
        if 'Agent' in obligatory:
            obligatory.remove('Agent')
        if 'Patient' not in obligatory and 'Patient' in frame.get('roles', []):
            obligatory.append('Patient')
    elif voice == 'reflexive':
        notes.append("Reflexive voice: Agent/Experiencer and Patient/Stimulus are co-referential.")
        # When reflexive, Patient or Stimulus is satisfied by reflexive accusative pronoun
        if 'Patient' in obligatory and 'Patient' in overt_roles:
            pass  # Satisfied
        if 'Stimulus' in obligatory and 'Stimulus' in overt_roles:
            pass  # Satisfied
    elif voice == 'inchoative':
        notes.append("Inchoative voice: Spontaneous state change; external agent requirement absent; Theme promoted to Subject.")
        if 'Agent' in obligatory:
            obligatory.remove('Agent')
        if 'Theme' not in obligatory:
            obligatory.append('Theme')

    missing = [role for role in obligatory if role not in overt_roles]
    extraneous = [role for role in overt_roles if role not in obligatory and role not in optional]

    if missing:
        if voice == 'active' and verb_lemma == 'nesalen' and 'Patient' in missing:
            notes.append("Valency defect: Transitive 'nesalen' requires overt Patient. Subject cannot be parsed as patient without middle/passive voice.")
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
