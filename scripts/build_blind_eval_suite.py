"""Build leak-resistant held-out evaluation suite for Agent-to-Agent Blind Protocol v2.

Generates 42 test fixtures with strictly separated cases and private gold answers.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    cases = []
    gold = []

    # Track 1: Fixed-Lexicon Encoding (12 cases)
    t1_data = [
        ("BLIND-T1-001", "literal", "Mei da liren püsel meharan.", "I saw the sweet fruit.", "Gördüm tatlı meyveyi.", "Direct perception transitive clause."),
        ("BLIND-T1-002", "literal", "Sai tüvanan va sileven.", "You will make the tool.", "Sen aleti yapacaksın.", "SOV object-focus transitive."),
        ("BLIND-T1-003", "logical", "Mei ne da belemen tüvanan.", "I did not count the tools.", "Aletleri saymadım.", "Simple past negation with overt patient."),
        ("BLIND-T1-004", "logical", "Şe Sai avelen, Mei va aremen.", "If you come, I will return.", "Eğer sen gelirsen, ben döneceğim.", "Pure conditional sentence."),
        ("BLIND-T1-005", "spatial", "Eli lem lo.", "He is in the dwelling.", "O evin içindedir / yerindedir.", "Locative postposition lo."),
        ("BLIND-T1-006", "spatial", "Meina da avelen vümar ta.", "We arrived at the bridge.", "Köprüye vardık.", "Directional postposition ta."),
        ("BLIND-T1-007", "aspectual", "Mei du yelaren liman lo.", "I am writing on stone.", "Taşın üzerine yazmaktayım.", "Progressive aspect du."),
        ("BLIND-T1-008", "aspectual", "Eli fa avelen lem ta.", "He has arrived at the dwelling.", "Eve varmış bulunuyor.", "Completed aspect fa."),
        ("BLIND-T1-009", "social", "Alei, Sai süli le?", "Hello, are you well?", "Merhaba, iyi misin?", "Greeting and polar question."),
        ("BLIND-T1-010", "social", "Mei naelen ke miraven Saian.", "I want to help you.", "Sana yardım etmek istiyorum.", "Volition verb + ke + miraven."),
        ("BLIND-T1-011", "minimal_pair_a", "Mei da sileven tüvanan.", "I made the tool.", "Aleti yaptım.", "Affirmative past."),
        ("BLIND-T1-012", "minimal_pair_b", "Mei ne da sileven tüvanan.", "I did not make the tool.", "Aleti yapmadım.", "Negative past.")
    ]

    for cid, ctype, alei, gold_en, gold_tr, notes in t1_data:
        cases.append({
            "case_id": cid,
            "track": "track_1_fixed_lexicon",
            "category": ctype,
            "input_alei": alei,
            "blinded_prompt": f"Translate the following Alei sentence into natural Turkish and English using only canonical Alei v1.1 rules:\n\n{alei}"
        })
        gold.append({
            "case_id": cid,
            "track": "track_1_fixed_lexicon",
            "gold_translation_en": gold_en,
            "gold_translation_tr": gold_tr,
            "critical_semantic_features": {
                "subject": alei.split()[0],
                "polarity": "negative" if "ne " in alei else "affirmative",
                "tense": "past" if "da " in alei else ("future" if "va " in alei else "unmarked"),
                "aspect": "progressive" if "du " in alei else ("completed" if "fa " in alei else "unmarked")
            },
            "rubric_notes": notes
        })

    # Track 2: Productive Form Decoding (10 cases)
    t2_data = [
        ("BLIND-T2-001", "transparent_compound", "orai-el", "sometimes / occasionally", "bazen / kimi zaman", "orai (time) + el (also)"),
        ("BLIND-T2-002", "transparent_compound", "nasel-nerav", "map / place-model", "harita / mekan temsili", "nasel (place) + nerav (model)"),
        ("BLIND-T2-003", "transparent_compound", "dei-pemar", "starlight", "yıldız ışığı", "dei (star) + pemar (light)"),
        ("BLIND-T2-004", "derived_quality", "fali", "open (stative)", "açık (durum)", "fal (open action) + -i (quality)"),
        ("BLIND-T2-005", "transparent_compound", "lüra-vel", "threshold / doorway", "kapı eşiği / giriş yolu", "lüra (door) + vel (path)"),
        ("BLIND-T2-006", "transparent_compound", "pira-vesen", "whisper / murmur", "fısıldamak / alçak sesle konuşmak", "pira (small) + vesen (say)"),
        ("BLIND-T2-007", "transparent_compound", "süli-ves", "truth / honest word", "doğru söz / hakikat", "süli (good) + ves (word)"),
        ("BLIND-T2-008", "transparent_compound", "ne-pemar", "shadow / darkness", "gölge / ışıksızlık", "ne (neg) + pemar (light)"),
        ("BLIND-T2-009", "derived_verb", "morven", "to tie / bind", "bağlamak / düğümlemek", "morv (knot) + -en (verb)"),
        ("BLIND-T2-010", "transparent_compound", "sira-vel", "destiny / ordained path", "kader / yolun gayesi", "sira (cause) + vel (path)")
    ]

    for cid, ctype, form, gold_en, gold_tr, notes in t2_data:
        cases.append({
            "case_id": cid,
            "track": "track_2_productive_decoding",
            "category": ctype,
            "input_alei": form,
            "blinded_prompt": f"Analyze the following productive Alei expression using standard morphological decomposition. State its root components, syntactic class, and plausible semantic meaning:\n\n{form}"
        })
        gold.append({
            "case_id": cid,
            "track": "track_2_productive_decoding",
            "gold_translation_en": gold_en,
            "gold_translation_tr": gold_tr,
            "morphological_breakdown": notes,
            "acceptable_semantic_fields": [gold_en, gold_tr],
            "rubric_notes": "Credit given for correct component identification and plausible semantic category; exact wording not required."
        })

    # Track 3: Open-Semantic Description Decoding (10 cases)
    t3_data = [
        ("BLIND-T3-001", "valid_transparent", "meyar-li-reş-ze-selim", "valid", "A fruit that is typically black/dark and typically sweet.", "Standard attested example."),
        ("BLIND-T3-002", "valid_transparent", "len-pe-belem-di-liman", "valid", "A dwelling whose purpose is computing/calculation and made of stone.", "Attested functional roles."),
        ("BLIND-T3-003", "valid_transparent", "savel-ge-nasel", "valid", "A plant associated with the location.", "Attested location role."),
        ("BLIND-T3-004", "valid_transparent", "melir-sa-püra", "valid", "An animal subtype: bird.", "Attested taxonomy role."),
        ("BLIND-T3-005", "valid_novel", "meyar-li-lüven-ze-koral", "valid", "A fruit that is typically green and typically bitter/sour.", "Novel combination of valid classes."),
        ("BLIND-T3-006", "ambiguous_duplicate", "meyar-li-reş-li-lüven", "ambiguous", "Fruit described with conflicting colors (black and green).", "Multiple values for role li; warning expected."),
        ("BLIND-T3-007", "invalid_type_clash", "meyar-li-hokar", "invalid", "REJECTED: Emotion 'hokar' assigned to color role 'li'.", "Negative control: must be rejected."),
        ("BLIND-T3-008", "invalid_unknown_role", "meyar-no-reş", "invalid", "REJECTED: Role 'no' is unknown/disabled in canon.", "Negative control: disabled role."),
        ("BLIND-T3-009", "invalid_unknown_root", "jajaya-li-reş", "invalid", "REJECTED: Head 'jajaya' is an unrecorded root.", "Negative control: unknown root."),
        ("BLIND-T3-010", "abstention_target", "famel-sa-melir", "valid", "An organism subtype: animal.", "Valid taxonomic specification.")
    ]

    for cid, ctype, expr, validity, gold_en, notes in t3_data:
        cases.append({
            "case_id": cid,
            "track": "track_3_open_semantics",
            "category": ctype,
            "input_alei": expr,
            "blinded_prompt": f"Evaluate the semantic validity of this hyphenated Alei description. State whether it is well-formed, ambiguous, or invalid according to transparent semantic type constraints:\n\n{expr}"
        })
        gold.append({
            "case_id": cid,
            "track": "track_3_open_semantics",
            "expected_validity": validity,
            "gold_interpretation": gold_en,
            "rubric_notes": notes
        })

    # Track 4: Definition Learning and Transfer (10 cases)
    t4_data = [
        ("BLIND-T4-001", "transfer_pol", "Pol", "Davi ena da pürelen pol-ra.", "Two people arrived from opposite sides.", "İki kişi zıt yönlerden ulaştı."),
        ("BLIND-T4-002", "transfer_pol", "Pol", "Mei da liren pol velan.", "I saw the opposite/contrary path.", "Karşıt yolu gördüm."),
        ("BLIND-T4-003", "transfer_gor", "Gor", "Sai da yelaren goran.", "You wrote the direction.", "Yönü yazdın."),
        ("BLIND-T4-004", "transfer_gor", "Gor", "Eli va avelen samel gor ta.", "He will come to the same direction.", "Aynı istikamete gelecek."),
        ("BLIND-T4-005", "transfer_bav", "Bav", "Bav da avelen nasel lo.", "Dawn arrived at the place.", "Şafak mekana vardı."),
        ("BLIND-T4-006", "transfer_tem", "Tem", "Eli da nivaren tem mora.", "He waited for a single moment.", "Tek bir an bekledi."),
        ("BLIND-T4-007", "transfer_şul", "Şul", "Nasel da şuli nivar lo.", "The place was silent at night.", "Mekan geceleyin sessizdi."),
        ("BLIND-T4-008", "transfer_kan", "Kan", "Ena pira da kanen.", "The child sang.", "Çocuk şarkı söyledi."),
        ("BLIND-T4-009", "transfer_yan", "Yan", "Mei da yelaren yanan liman lo.", "I wrote the error on stone.", "Hatayı taşa yazdım."),
        ("BLIND-T4-010", "transfer_morv", "Morv", "Eli da sileven morvan.", "He tied the knot.", "Düğümü bağladı.")
    ]

    definitions_block = (
        "NEW EXPERIMENTAL DEFINITIONS FOR THIS TRACK ONLY:\n"
        "- Pol (root): opposite, contrary, reverse (karşıt, zıt)\n"
        "- Gor (root): direction, vector, aim (yön, istikamet)\n"
        "- Bav (root): dawn, daybreak (şafak, seher)\n"
        "- Tem (root): moment, instant (an, lahza)\n"
        "- Şul (root): silence, quietness (sessizlik)\n"
        "- Kan (root): song, melody (ezgi, şarkı)\n"
        "- Yan (root): error, mistake (yanılgı, hata)\n"
        "- Morv (root): knot, bond (düğüm, bağ)\n"
    )

    for cid, ctype, target_root, sentence, gold_en, gold_tr in t4_data:
        cases.append({
            "case_id": cid,
            "track": "track_4_definition_transfer",
            "category": ctype,
            "target_root": target_root,
            "input_alei": sentence,
            "definitions_supplied": definitions_block,
            "blinded_prompt": f"Given the experimental definitions below, translate the novel Alei sentence into English and Turkish:\n\n{definitions_block}\nSentence to translate: {sentence}"
        })
        gold.append({
            "case_id": cid,
            "track": "track_4_definition_transfer",
            "target_root": target_root,
            "gold_translation_en": gold_en,
            "gold_translation_tr": gold_tr,
            "rubric_notes": f"Tests one-shot transfer of root '{target_root}' in an unseen grammatical sentence."
        })

    # Write cases.jsonl
    cases_path = ROOT / 'evaluations/agent-blind-v2/cases.jsonl'
    with cases_path.open('w', encoding='utf-8') as f:
        for c in cases:
            f.write(json.dumps(c, ensure_ascii=False) + '\n')
    print(f"Wrote {len(cases)} evaluation cases to {cases_path}")

    # Write gold-answers.jsonl
    gold_path = ROOT / 'evaluations/agent-blind-v2/gold-answers.jsonl'
    with gold_path.open('w', encoding='utf-8') as f:
        for g in gold:
            f.write(json.dumps(g, ensure_ascii=False) + '\n')
    print(f"Wrote {len(gold)} private gold references to {gold_path}")

if __name__ == '__main__':
    main()
