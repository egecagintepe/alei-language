"""Typed Abstract Syntax Tree (AST) and Intermediate Representation (IR) for Alei.

Provides structured, inspectable representations of words, constituents,
argument frames, and full sentence parse trees with explicit ambiguity status.
"""
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass
class TokenNode:
    surface: str
    normalized: str
    lemma: Optional[str] = None
    part_of_speech: Optional[str] = None
    morphology: Dict[str, Any] = field(default_factory=dict)
    provenance: Optional[Dict[str, Any]] = None
    is_canonical: bool = True
    is_legacy_alias: bool = False
    warning: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            'surface': self.surface,
            'normalized': self.normalized,
            'lemma': self.lemma,
            'pos': self.part_of_speech,
            'morphology': self.morphology,
            'is_canonical': self.is_canonical,
            'is_legacy_alias': self.is_legacy_alias,
            'warning': self.warning
        }

@dataclass
class ArgumentRole:
    role: str  # Agent, Patient, Experiencer, Stimulus, Destination, Location, Beneficiary, Message
    token: Optional[TokenNode] = None
    value: Optional[str] = None
    is_overt: bool = True
    is_omitted: bool = False
    is_implied: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return {
            'role': self.role,
            'value': self.value,
            'is_overt': self.is_overt,
            'is_omitted': self.is_omitted,
            'is_implied': self.is_implied
        }

@dataclass
class PredicateFrame:
    verb_lemma: str
    verb_token: Optional[TokenNode] = None
    voice: str = 'active'  # active, middle, inchoative, passive
    valency_class: str = 'transitive'  # intransitive, transitive, ditransitive, copular
    arguments: List[ArgumentRole] = field(default_factory=list)
    valency_satisfied: bool = True
    valency_notes: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            'verb_lemma': self.verb_lemma,
            'voice': self.voice,
            'valency_class': self.valency_class,
            'arguments': [arg.to_dict() for arg in self.arguments],
            'valency_satisfied': self.valency_satisfied,
            'valency_notes': self.valency_notes
        }

@dataclass
class SentenceAST:
    status: str  # 'supported', 'ambiguous', 'unsupported', 'contradictory', 'unknown_lexeme'
    construction: str  # 'verbal', 'nominal_predicate', 'imperative', 'location_predicate', 'possession_phrase', 'embedded_clause', 'quotative', 'concessive_conditional'
    speech_act: str = 'assertion'  # 'assertion', 'question', 'imperative', 'quotation'
    polarity: bool = True  # True = affirmative, False = negative
    tense: str = 'unmarked'  # 'past', 'future', 'unmarked'
    aspect: str = 'unmarked'  # 'progressive', 'completed', 'habitual', 'unmarked'
    mood: str = 'indicative'  # 'indicative', 'conditional', 'concessive', 'imperative'
    subject: Optional[str] = None
    predicate: Optional[PredicateFrame] = None
    tokens: List[TokenNode] = field(default_factory=list)
    diagnostics: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    ambiguities: List[Dict[str, Any]] = field(default_factory=list)
    raw_text: str = ''
    version: str = '1.0'
    is_experimental: bool = False

    def to_dict(self) -> Dict[str, Any]:
        res = {
            'status': self.status,
            'construction': self.construction,
            'speech_act': self.speech_act,
            'polarity': self.polarity,
            'tense': self.tense,
            'aspect': self.aspect,
            'mood': self.mood,
            'subject': self.subject,
            'raw_text': self.raw_text,
            'version': self.version,
            'is_experimental': self.is_experimental,
            'diagnostics': self.diagnostics,
            'warnings': self.warnings
        }
        if self.predicate:
            res['predicate'] = self.predicate.to_dict()
        if self.ambiguities:
            res['ambiguities'] = self.ambiguities
        return res

    def format_tree(self, indent: int = 0) -> str:
        pad = "  " * indent
        lines = [
            f"{pad}(SENTENCE [{self.status}]",
            f"{pad}  (CONSTRUCTION {self.construction})",
            f"{pad}  (SPEECH_ACT {self.speech_act})",
            f"{pad}  (FEATURES polarity={'+' if self.polarity else '-'} tense={self.tense} aspect={self.aspect} mood={self.mood})"
        ]
        if self.subject:
            lines.append(f"{pad}  (SUBJECT {self.subject})")
        if self.predicate:
            lines.append(f"{pad}  (PREDICATE {self.predicate.verb_lemma} voice={self.predicate.voice} class={self.predicate.valency_class})")
            for arg in self.predicate.arguments:
                overt_str = "overt" if arg.is_overt else ("omitted" if arg.is_omitted else "implied")
                lines.append(f"{pad}    (ARG {arg.role}: {arg.value} [{overt_str}])")
        if self.diagnostics:
            lines.append(f"{pad}  (DIAGNOSTICS {'; '.join(self.diagnostics)})")
        lines.append(f"{pad})")
        return "\n".join(lines)
