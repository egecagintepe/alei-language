"""Generate and validate Alei L5 concept priority inventory and lexical proposals.

Enforces strict separation between canonical v1.1.0 and experimental proposals.
"""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))

from alei_language.lexicon import records, normalize
from alei_language.orthography import validate, syllables, stress_index

canonical_roots = {normalize(r['canonical_spelling']): r for r in records('1.1.0') if r['part_of_speech'] == 'root'}
canonical_lexemes = {normalize(r['canonical_spelling']): r for r in records('1.1.0')}

def main():
    print("Building concept priority and lexical proposal registers...")

    # 1. Ten Proposed Candidate Roots (Category C)
    proposed_roots = [
        {
            "id": "PROP-ROOT-001",
            "candidate_spelling": "Pol",
            "ipa": "/pol/",
            "syllables": "pol",
            "syllable_structure": "CVC",
            "stress": "monosyllabic",
            "gloss_tr": "karşıt / zıt",
            "semantic_anchor_en": "opposite",
            "part_of_speech": "root",
            "semantic_class": "spatial_relation",
            "phonological_neighborhood": ["pal", "sol", "pel"],
            "rationale": "Directly resolves Evidence Case C08 (arrival from opposite ends). Currently unexpressed.",
            "example_sentence": "Davi ena da pürelen pol-ra vümar ta.",
            "example_gloss_tr": "İki kişi köprüye zıt yönlerden ulaştı.",
            "example_gloss_en": "Two people reached the bridge from opposite directions.",
            "interlinear": "davi ena da pürel-en pol-ra vümar ta | two person PST arrive-VB opposite-ABL bridge DAT",
            "status": "unadopted_candidate_root"
        },
        {
            "id": "PROP-ROOT-002",
            "candidate_spelling": "Gor",
            "ipa": "/ɡor/",
            "syllables": "gor",
            "syllable_structure": "CVC",
            "stress": "monosyllabic",
            "gloss_tr": "yön / istikamet",
            "semantic_anchor_en": "direction",
            "part_of_speech": "root",
            "semantic_class": "spatial_relation",
            "phonological_neighborhood": ["toram", "morun", "kor"],
            "rationale": "Resolves Evidence Case C06 (showing direction). Introduces spatial orientation head.",
            "example_sentence": "Pemar da sileven goran.",
            "example_gloss_tr": "Işık yönü belirledi / gösterdi.",
            "example_gloss_en": "The light showed the direction.",
            "interlinear": "pemar da silev-en gor-an | light PST make-VB direction-ACC",
            "status": "unadopted_candidate_root"
        },
        {
            "id": "PROP-ROOT-003",
            "candidate_spelling": "Bav",
            "ipa": "/bav/",
            "syllables": "bav",
            "syllable_structure": "CVC",
            "stress": "monosyllabic",
            "gloss_tr": "şafak / seher",
            "semantic_anchor_en": "dawn",
            "part_of_speech": "root",
            "semantic_class": "temporal_entity",
            "phonological_neighborhood": ["jav", "pavel", "pavim"],
            "rationale": "Complements existing night root 'nivar' for daily literary and narrative cycles.",
            "example_sentence": "Bav da avelen nasel lo.",
            "example_gloss_tr": "Şafak mekana ulaştı.",
            "example_gloss_en": "Dawn arrived at the place.",
            "interlinear": "bav da avel-en nasel lo | dawn PST arrive-VB place LOC",
            "status": "unadopted_candidate_root"
        },
        {
            "id": "PROP-ROOT-004",
            "candidate_spelling": "Tem",
            "ipa": "/tem/",
            "syllables": "tem",
            "syllable_structure": "CVC",
            "stress": "monosyllabic",
            "gloss_tr": "an / lahza",
            "semantic_anchor_en": "moment",
            "part_of_speech": "root",
            "semantic_class": "temporal_entity",
            "phonological_neighborhood": ["lem", "tum", "tenar"],
            "rationale": "Punctual temporal anchor distinct from duration root 'orai'.",
            "example_sentence": "Tem mora da yelen ke avelen.",
            "example_gloss_tr": "Bir an gelebildi.",
            "example_gloss_en": "A single moment could come.",
            "interlinear": "tem mora da yel-en ke avel-en | moment one PST can-VB COMP arrive-VB",
            "status": "unadopted_candidate_root"
        },
        {
            "id": "PROP-ROOT-005",
            "candidate_spelling": "Şul",
            "ipa": "/ʃul/",
            "syllables": "şul",
            "syllable_structure": "CVC",
            "stress": "monosyllabic",
            "gloss_tr": "sessizlik / sükunet",
            "semantic_anchor_en": "silence",
            "part_of_speech": "root",
            "semantic_class": "sensory_state",
            "phonological_neighborhood": ["şel", "sül", "sol"],
            "rationale": "Essential poetic state for contemplation and night scenes in literary Alei.",
            "example_sentence": "Nasel da şuli nivar lo.",
            "example_gloss_tr": "Mekan geceleyin sessizdi.",
            "example_gloss_en": "The place was silent during the night.",
            "interlinear": "nasel da şul-i nivar lo | place PST silence-ADJ night LOC",
            "status": "unadopted_candidate_root"
        },
        {
            "id": "PROP-ROOT-006",
            "candidate_spelling": "Kan",
            "ipa": "/kan/",
            "syllables": "kan",
            "syllable_structure": "CVC",
            "stress": "monosyllabic",
            "gloss_tr": "ezgi / şarkı",
            "semantic_anchor_en": "song",
            "part_of_speech": "root",
            "semantic_class": "cultural_expression",
            "phonological_neighborhood": ["zanar", "len", "koral"],
            "rationale": "Human musical expression, vital for oral poetry, children's songs and literature.",
            "example_sentence": "Ena pira da kanen.",
            "example_gloss_tr": "Çocuk şarkı söyledi.",
            "example_gloss_en": "The child sang.",
            "interlinear": "ena pira da kan-en | person small PST song-VB",
            "status": "unadopted_candidate_root"
        },
        {
            "id": "PROP-ROOT-007",
            "candidate_spelling": "Yan",
            "ipa": "/jan/",
            "syllables": "yan",
            "syllable_structure": "CVC",
            "stress": "monosyllabic",
            "gloss_tr": "yanılgı / hata",
            "semantic_anchor_en": "error",
            "part_of_speech": "root",
            "semantic_class": "epistemic_state",
            "phonological_neighborhood": ["zanar", "yenar", "jav"],
            "rationale": "Resolves Evidence Case C07 (recording an error on stone).",
            "example_sentence": "Mei da yelaren yanan liman lo.",
            "example_gloss_tr": "Hatayı taşa yazdım.",
            "example_gloss_en": "I wrote the error on stone.",
            "interlinear": "mei da yelar-en yan-an liman lo | 1SG PST write-VB error-ACC stone LOC",
            "status": "unadopted_candidate_root"
        },
        {
            "id": "PROP-ROOT-008",
            "candidate_spelling": "Morv",
            "ipa": "/morv/",
            "syllables": "morv",
            "syllable_structure": "CVCC",
            "stress": "monosyllabic",
            "gloss_tr": "düğüm / bağ",
            "semantic_anchor_en": "knot",
            "part_of_speech": "root",
            "semantic_class": "physical_relational",
            "phonological_neighborhood": ["morun", "molir", "toram"],
            "rationale": "Physical and metaphorical binding, agreement, or entanglement.",
            "example_sentence": "Eli da sileven morvan.",
            "example_gloss_tr": "Düğümü bağladı / yaptı.",
            "example_gloss_en": "He made the knot.",
            "interlinear": "eli da silev-en morv-an | 3SG PST make-VB knot-ACC",
            "status": "unadopted_candidate_root"
        },
        {
            "id": "PROP-ROOT-009",
            "candidate_spelling": "Dal",
            "ipa": "/dal/",
            "syllables": "dal",
            "syllable_structure": "CVC",
            "stress": "monosyllabic",
            "gloss_tr": "dal",
            "semantic_anchor_en": "branch",
            "part_of_speech": "root",
            "semantic_class": "botanical_part",
            "phonological_neighborhood": ["pal", "del", "sol"],
            "rationale": "Concrete natural world anchor extending plant taxonomy (savel, yenar).",
            "example_sentence": "Püra da avelen dal lo.",
            "example_gloss_tr": "Kuş dala kondu / geldi.",
            "example_gloss_en": "The bird came onto the branch.",
            "interlinear": "püra da avel-en dal lo | bird PST arrive-VB branch LOC",
            "status": "unadopted_candidate_root"
        },
        {
            "id": "PROP-ROOT-010",
            "candidate_spelling": "Nur",
            "ipa": "/nur/",
            "syllables": "nur",
            "syllable_structure": "CVC",
            "stress": "monosyllabic",
            "gloss_tr": "ışıltı / parıltı",
            "semantic_anchor_en": "radiance",
            "part_of_speech": "root",
            "semantic_class": "visual_quality",
            "phonological_neighborhood": ["nüvil", "tümar", "tum"],
            "rationale": "Subtle, soft luminescence distinct from harsh sunlight/brightness ('pemar').",
            "example_sentence": "Dei ri nur da liren.",
            "example_gloss_tr": "Yıldızın parıltısı görüldü.",
            "example_gloss_en": "The radiance of the star was seen.",
            "interlinear": "dei ri nur da lir-en | star GEN radiance PST see-VB",
            "status": "unadopted_candidate_root"
        }
    ]

    # Validate all proposed roots
    for pr in proposed_roots:
        norm = normalize(pr['candidate_spelling'])
        assert norm not in canonical_roots, f"Collision with canonical root: {norm}"
        val_err = validate(norm)
        assert not val_err, f"Orthography error in {norm}: {val_err}"

    # Write proposed-lexemes.jsonl
    prop_lex_path = ROOT / 'linguistics/lexicon/proposed-lexemes.jsonl'
    with prop_lex_path.open('w', encoding='utf-8') as f:
        for pr in proposed_roots:
            f.write(json.dumps(pr, ensure_ascii=False) + '\n')
    print(f"Wrote {len(proposed_roots)} candidate roots to {prop_lex_path}")

    # 2. Build 100-Concept Priority Inventory across 10 Domains
    # Categorized into A (Existing approved), B (Proposed compound/derivation), C (Proposed root), D (Unresolved gap)
    domains = [
        ("spatial_navigation", [
            ("door", "A", "lüra", "Canonical root lüra (roots:608, door)"),
            ("path_way", "A", "vel", "Canonical root vel (roots:444, direction/path)"),
            ("bridge", "A", "vümar", "Canonical root vümar (roots:501, bridge)"),
            ("place_location", "A", "lem", "Canonical root lem (roots:451, dwelling/place)"),
            ("crossing", "D", "GAP-SPA-01", "Unresolved lexical gap: crossing/passing action"),
            ("opposite_contrary", "C", "Pol", "Proposed root PROP-ROOT-001 (opposite, contrary)"),
            ("direction_vector", "C", "Gor", "Proposed root PROP-ROOT-002 (candidate duplicate of vel)"),
            ("center_middle", "B", "lem-molir", "Compound: center place / circular mid-point"),
            ("threshold_entrance", "B", "lüra-vel", "Compound: door-path / threshold"),
            ("far_distance", "B", "lavar-vel", "Compound: great path / long distance")
        ]),
        ("temporal_aspectual", [
            ("time_occasion", "A", "orai", "Canonical function orai (functions:1062, when/time)"),
            ("night", "A", "mora", "Canonical root mora (roots:455, night)"),
            ("day_morning", "A", "dei", "Canonical root dei (roots:454, day)"),
            ("two_second", "A", "davi", "Canonical numeral davi (functions:1101, two)"),
            ("three_third", "A", "teli", "Canonical numeral teli (functions:1102, three)"),
            ("dawn_morning", "C", "Bav", "Proposed root PROP-ROOT-003 (dawn, daybreak)"),
            ("moment_instant", "C", "Tem", "Proposed root PROP-ROOT-004 (moment, instant)"),
            ("sometimes", "B", "orai-el", "Transparent compound: time-also / occasionally"),
            ("never", "B", "ne-orai", "Compound/phrase: ne ... orai (not once)"),
            ("always_forever", "B", "mora-dei-orai", "Compound: day-and-night / continuously")
        ]),
        ("physical_states_materials", [
            ("opening_action", "A", "fal", "Canonical root fal (roots:516, opening action)"),
            ("open_state", "B", "fali", "Proposed derived stative quality: fal + -i"),
            ("stone_rock", "A", "liman", "Canonical root liman (roots:456, stone)"),
            ("star", "D", "GAP-LEX-STAR", "Unresolved lexical gap: no canonical root for star; Nüra is moon"),
            ("light_brightness", "A", "pemar", "Canonical root pemar (roots:589, brightness/light)"),
            ("tool_instrument", "A", "tüvan", "Canonical noun/root tüvan (book/written instrument/tool)"),
            ("water_liquid", "A", "nemi", "Canonical root nemi (roots:438, water)"),
            ("silence_quiet", "C", "Şul", "Proposed root PROP-ROOT-005 (silence)"),
            ("radiance_glow", "C", "Nur", "Proposed root PROP-ROOT-010 (radiance, luminescence)"),
            ("plant_branch", "C", "Dal", "Proposed root PROP-ROOT-009 (branch, stem)")
        ]),
        ("epistemic_cognitive", [
            ("thinking", "A", "aremen", "Canonical verb aremen (lexemes:757, to think)"),
            ("searching", "A", "hüvaren", "Canonical search verb hüvaren (lexemes:804, to search)"),
            ("computing_counting", "A", "belemen", "Canonical verb belemen (lexemes:769, to compute/count)"),
            ("seeing_perceiving", "A", "liren", "Canonical perception verb liren (lexemes:794, to see)"),
            ("representation_model", "A", "nerav", "Canonical root nerav (roots:681, model, schema)"),
            ("error_mistake", "C", "Yan", "Proposed root PROP-ROOT-007 (error, mistake)"),
            ("learning", "A", "nivaren", "Canonical learning verb nivaren (lexemes:921, to learn)"),
            ("truth_verity", "B", "süli-ves", "Compound: good/accurate word / truth"),
            ("forgetting", "B", "ne-ari", "Negative phrase: without knowledge / having forgotten"),
            ("epistemic_doubt", "D", "GAP-EPI-01", "Explicitly unresolved: epistemic dubitative particle")
        ]),
        ("affective_emotional", [
            ("surprise_awe", "A", "sülar", "Canonical root sülar (roots:708, surprise)"),
            ("surprised_state", "A", "sülari", "Canonical quality sülari (lexemes:909, surprised)"),
            ("goodness_wellness", "A", "sül", "Canonical root sül (roots:478, goodness)"),
            ("good_well", "A", "süli", "Canonical quality süli (lexemes:866, good, well)"),
            ("anger_wrath", "A", "hokar", "Canonical emotion root hokar (roots:487, anger)"),
            ("inner_peace", "A", "norel", "Canonical peace root norel (roots:435, peace)"),
            ("fear_dread", "A", "vürel", "Canonical fear root vürel (roots:502, fear)"),
            ("desire_volition", "A", "nael", "Canonical desire root nael (roots:439, desire)"),
            ("peace_relief", "B", "şul-norel", "Compound: silent peace / tranquility"),
            ("affective_clash", "D", "GAP-AFF-01", "Explicitly unresolved: complex ambivalent affective states")
        ]),
        ("communication_social", [
            ("greeting_hello", "A", "alei", "Official approved language name and greeting (AD-2026-001)"),
            ("speech_word", "A", "ves", "Canonical root ves (roots:445, word, speech)"),
            ("saying_speaking", "A", "vesen", "Canonical verb vesen (lexemes:768, to speak, say)"),
            ("helping", "A", "miraven", "Owner-approved preferred v1.1 help verb (AD-2026-002)"),
            ("friend_companion", "A", "samel", "Canonical root samel (roots:471, friend, companion)"),
            ("song_singing", "C", "Kan", "Proposed root PROP-ROOT-006 (song, melody)"),
            ("gratitude_thanks", "B", "sül-ves", "Compound: good speech / thank you"),
            ("apology_regret", "B", "yan-ves", "Compound: error acknowledgment / apology"),
            ("promise_oath", "B", "morv-ves", "Compound: bound word / promise"),
            ("politeness_register", "D", "GAP-SOC-01", "Explicitly unresolved: formal honorific clitics")
        ]),
        ("actions_transitivity", [
            ("losing_transitive", "A", "nesalen", "Canonical transitive verb nesalen (lexemes:805, to lose)"),
            ("middle_getting_lost", "D", "GAP-VOI-01", "Unadopted proposal: middle voice mechanism for intransitive/reflexive loss"),
            ("entering_arriving", "A", "avelen", "Canonical motion verb avelen (lexemes:755, to go, arrive)"),
            ("returning", "A", "nelaren", "Canonical return verb nelaren (lexemes:889, to return)"),
            ("reaching_arriving", "A", "pürelen", "Canonical arrival verb pürelen (lexemes:754, to reach, come)"),
            ("writing_inscribing", "A", "yelaren", "Canonical verb yelaren (lexemes:795, to write)"),
            ("making_producing", "A", "javen", "Canonical production verb javen (lexemes:784, to make, produce)"),
            ("reading", "A", "sileven", "Canonical reading verb sileven (lexemes:793, to read)"),
            ("closing", "A", "dumen", "Canonical closing verb dumen (lexemes:797, to close; Dum roots:517)"),
            ("binding_knotting", "B", "morven", "Derived verb from proposed root morv")
        ]),
        ("quantity_logic", [
            ("numeral_one", "A", "ena", "Canonical numeral ena (functions:1100, one)"),
            ("numeral_two", "A", "davi", "Canonical numeral davi (functions:1101, two)"),
            ("numeral_three", "A", "teli", "Canonical numeral teli (functions:1102, three)"),
            ("numeral_four", "A", "pora", "Canonical numeral pora (functions:1103, four)"),
            ("numeral_five", "A", "lume", "Canonical numeral lume (functions:1104, five)"),
            ("numeral_six", "A", "şari", "Canonical numeral şari (functions:1105, six)"),
            ("numeral_seven", "A", "növi", "Canonical numeral növi (functions:1106, seven)"),
            ("numeral_eight", "A", "kema", "Canonical numeral kema (functions:1107, eight)"),
            ("numeral_nine", "A", "vüni", "Canonical numeral vüni (functions:1108, nine)"),
            ("numeral_ten", "A", "des", "Canonical numeral des (functions:1109, ten)")
        ]),
        ("daily_life_practicality", [
            ("child_young_person", "A", "pira", "Canonical root pira (roots:474, small, child)"),
            ("shelter_dwelling", "A", "lem", "Canonical root lem (roots:451, shelter, dwelling)"),
            ("earth_soil", "A", "süvar", "Canonical root süvar (roots:488, earth, soil)"),
            ("fruit_food", "A", "meyar", "Canonical root meyar (roots:493, fruit, vegetable)"),
            ("fish", "A", "zanar", "Canonical animal root zanar (roots:495, fish)"),
            ("bird", "A", "püra", "Canonical root püra (roots:494, bird)"),
            ("binding_cord", "C", "Morv", "Proposed root PROP-ROOT-008 (knot, bond)"),
            ("fire_warmth", "B", "pemar-sol", "Compound: light-warmth / fire"),
            ("path_marker", "B", "vel-siman", "Compound: path sign / landmark"),
            ("forest", "A", "nasel", "Canonical root nasel (roots:548, forest)")
        ]),
        ("narrative_poetic", [
            ("sun", "A", "sümei", "Canonical sun root sümei (roots:496, sun)"),
            ("moon", "A", "nüra", "Canonical moon root nüra (roots:497, moon)"),
            ("sky", "A", "siril", "Canonical sky root siril (roots:549, sky)"),
            ("whisper", "B", "pira-vesen", "Compound: small-speech / whispering"),
            ("shadow", "B", "ne-pemar", "Compound: absence of light / shadow"),
            ("reflection_mirror", "B", "nemi-lir", "Compound: water-seeing / reflection in water"),
            ("destiny_path", "B", "sira-vel", "Compound: cause-path / destiny"),
            ("starlight", "B", "siril-pemar", "Compound: sky-light / starlight candidate"),
            ("counterfactual_would", "D", "GAP-NAR-01", "Explicitly unresolved: counterfactual past mood particle"),
            ("vocative_poetic_oh", "D", "GAP-NAR-02", "Explicitly unresolved: formal vocative particle")
        ])
    ]

    concept_priority_records = []
    cid = 1
    for domain_name, items in domains:
        for concept_name, category, alei_expr, notes in items:
            concept_priority_records.append({
                "concept_id": f"CON-{cid:03d}",
                "domain": domain_name,
                "concept": concept_name,
                "category": category,
                "alei_expression": alei_expr,
                "notes": notes,
                "status": "official_canonical" if category == "A" else ("proposed_compound" if category == "B" else ("proposed_root" if category == "C" else "unresolved_gap"))
            })
            cid += 1

    cp_path = ROOT / 'linguistics/lexicon/concept-priority.jsonl'
    with cp_path.open('w', encoding='utf-8') as f:
        for r in concept_priority_records:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    print(f"Wrote {len(concept_priority_records)} priority concepts to {cp_path}")

    # 3. Build Concept Ontology Extension (linguistics/semantics/concepts-vnext-proposal.jsonl)
    ontology_records = [
        {
            "concept_id": "ONT-VNEXT-001",
            "term": "Pol",
            "type": "relational_spatial_primitive",
            "status": "proposal",
            "supertype": "spatial_relation",
            "asserted_attributes": ["reciprocal", "binary_oppositional", "vector_inversion"],
            "typical_attributes": ["distance_preserving", "polar_symmetry"],
            "constraints": {
                "requires_anchor": True,
                "prohibited_roles": ["li", "ze"]
            },
            "relations": [
                {"relation": "contrasts_with", "target": "samel"},
                {"relation": "applies_to", "target": "gor"}
            ]
        },
        {
            "concept_id": "ONT-VNEXT-002",
            "term": "Gor",
            "type": "navigational_primitive",
            "status": "proposal",
            "supertype": "spatial_vector",
            "asserted_attributes": ["directional", "scalar_independent"],
            "typical_attributes": ["forward_facing", "visual_grounding"],
            "constraints": {
                "requires_origin": False,
                "prohibited_roles": ["ze", "ku"]
            },
            "relations": [
                {"relation": "governs", "target": "vel"},
                {"relation": "oriented_by", "target": "pol"}
            ]
        },
        {
            "concept_id": "ONT-VNEXT-003",
            "term": "Şul",
            "type": "sensory_acoustic_state",
            "status": "proposal",
            "supertype": "acoustic_property",
            "asserted_attributes": ["zero_amplitude", "ambient_stillness"],
            "typical_attributes": ["night_associated", "calm_inducing"],
            "constraints": {
                "prohibited_roles": ["ze", "mu"]
            },
            "relations": [
                {"relation": "contrasts_with", "target": "ves"},
                {"relation": "associated_with", "target": "nivar"}
            ]
        },
        {
            "concept_id": "ONT-VNEXT-004",
            "term": "Yan",
            "type": "epistemic_evaluative_primitive",
            "status": "proposal",
            "supertype": "truth_value_state",
            "asserted_attributes": ["non_correspondence", "normative_failure"],
            "typical_attributes": ["correctable", "unintended"],
            "constraints": {
                "prohibited_roles": ["li", "su"]
            },
            "relations": [
                {"relation": "contrasts_with", "target": "sül"},
                {"relation": "inscribable_on", "target": "liman"}
            ]
        },
        {
            "concept_id": "ONT-VNEXT-005",
            "term": "Fali",
            "type": "derived_stative_quality",
            "status": "proposal",
            "supertype": "physical_aperture_state",
            "asserted_attributes": ["accessible", "unblocked", "stative"],
            "typical_attributes": ["door_associated", "passage_enabling"],
            "constraints": {
                "base_root": "fal",
                "derivation_suffix": "-i"
            },
            "relations": [
                {"relation": "derived_from", "target": "fal"},
                {"relation": "typically_predicates", "target": "lüra"}
            ]
        }
    ]

    ont_path = ROOT / 'linguistics/semantics/concepts-vnext-proposal.jsonl'
    with ont_path.open('w', encoding='utf-8') as f:
        for r in ontology_records:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    print(f"Wrote {len(ontology_records)} ontology records to {ont_path}")

if __name__ == '__main__':
    main()

