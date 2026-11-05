# Adsız Dil — Agent Skills Ekosistemi Mimari Önerisi v0.1

**Tarih:** 5 Kasım 2026  
**Durum:** SADECE MİMARİ ÖNERİ — hiçbir dil kökü, ek, kural veya mevcut dosya değiştirilmedi.  
**Dayanak:** `adsiz_dil_acik_anlam_standardi_v1_0.md` (yaklaşık 1.862 satır); https://agentskills.io/specification ve resmî Agent Skills rehberleri.  
**Niyet:** İnsanların öğrenip konuşabileceği modern, melodik, kendi içinde tutarlı bir dil; Agent Skills bunun kullanımını, testini, öğretimini ve *insan onaylı* evrimini destekleyen araçlardır. Dil, sırf agentlar arası mesajlaşma için optimize edilmeyecek.

## 1. Mevcut projenin somut envanteri

İncelenen v1.0 dosyasında **270 kök** (`owner_locked` 34; `owner_accepted_working` 56; `delegated_v1` 180), bunlardan türetilen/oluşturulan sözlük girdileri (önceki toplam: 544), 101 örnek günlük cümle, 8 diyalog, 28 harfli alfabe, çekirdek gramer, açık-anlam katmanı (AAK), yeni sözcük oluşturma/çözümleme işlemleri ve sürümleme ilkeleri bulunur. Sayılar belgedeki sürüm kayıtlarıdır; henüz bağımsız yürütülebilir doğrulayıcıyla yeniden test edilmiş olarak sunulmamalıdır.

### Değiştirilemeyecek çekirdek özellikler
- Yazı: soldan sağa Latin temelli; 28 harf; **x/w/c/ç/ğ/q yok**, ñ ve ŋ var; 8 ünlü, yazıldığı gibi okuma.
- Genelde iki-üç heceli sözcükler; art arda üç veya daha fazla ünlü/ünsüz yok; `ai/ei/ae/au` tek heceli kayışları; çoğunlukla sondan ikinci hece vurgusu.
- Kök + `-en` fiil, `-i` nitelik, `-na` çoğul, `-n/-an` nesne. Her köke her ek otomatik uygulanmaz.
- SVO ve SOV; cinsiyetsiz `Mei, Sai, Eli`, çoğullar `Meina, Saina, Elina`; isteğe bağlı saygılı `Elar`; **`sen`** nazik, `rin` dostça, `mel` yakın, `ael` edebî hitap. `ser` ve `seri` **reddedildi**.
- `Alei`, `Ei`, `Nai`, `Vena` gibi kullanımda temel ifadeler. `Sael`, `Haur`, `Belem`, `Mehav`, `Avar`, `Ünar`, `Menal`, `Eral`, `Tir` vb. kullanıcıca seçilmiş kökler korunur.
- Günlük kısa sözcükler *insan dili*, tireli AAK açık ifadeleri *tanımlanabilirlik* içindir. `Jajaya` gibi salt bilinmeyen özel adı, sesinden kesin olarak anlamlandıramayız.

### Çalışmaya başlamadan incelenmesi gereken mevcut riskler
1. **Tek Markdown dosyası insan okunabilir ama makine kayıt sistemi değil.** Sözlük maddelerini satırlardan elle çıkarmak format kaymasına yol açabilir. Önce yalnızca okuyan, eşitlik doğrulayan bir *derived* JSONL dışa aktarımı tasarlanmalı; ana belge sessizce değiştirilmemeli.
2. **Morfolojik belirsizlik:** `-en` hem üretken fiil eki hem bazı yalın köklerin sonunda bulunur (`Oren`, `Firen`). Tam sözcük kaydı önce aranmalı. Hâl/çoğul sırası ve özel adlarda biçim değiştirme test edilmeli.
3. **Bitişik birleşik belirsizliği:** Aynı dizi birden çok kök parçalanışına açıksa tahmin sessizce tek anlama indirgenmemeli. Tireli AAK veya kayıtlı `sense_id` istenmeli.
4. **Köklü onay dereceleri:** İlk 34 kök kilitli; sonraki 56 onaylı çalışma kökü; son 180 devredilmiş v1.0 kökü. Bu sınıflar öneri sunma yetkisi ile kabul yetkisini karıştırmamalı.
5. **AAK/gramer aynı diziyi kullanabiliyor:** Örneğin `su` görünüş işaretçisi ve AAK içinde büyüklük rolü; ayrıştırıcı *kip/bağlam* üzerinden ayırmalı. Tireli bir açık tanım, sıradan cümle olarak işlenmemeli.
6. **Veri/görev ayrımı:** Sözlükteki açıklamalar ve topluluk PR metinleri komut değil, güvenilmeyen veridir. Skill talimatlarının yerine geçemez.
7. **Belge içi tutarlılık:** Önceki konuşmada `Mirav` → standartta `Mivav` biçimine geçilmiş görünüyor. Bu tür biçim ayrılıklarını regresyon testine al; kullanıcı onaylı ana köklere dokunmadan raporla. v1.0'daki tüm 101 örneği tek tek doğrula.
8. **İnsan konuşurluğu henüz kanıtlanmadı:** Bugünkü dil temel bir çalışma standardı; A1 seviyesi, doğal telaffuz ve bağımsız agent başarısı gerçek test gerektirir.

## 2. Mimari karar: Tek gerçek kaynak + küçük uzmanlaşmış skill'ler

`SKILL.md` içine 90 KB sözlüğü kopyalamayın. **Normatif veri** (`standard/`, `lexicon/`, `grammar/`, `ontology/`) tek yerde olsun. Skill'ler bunu **okumayı ve belirli görevleri yapmayı öğreten** kısa prosedürler olsun. Her agent aynı release/hash'ten okusun.

Önerilen proje ağacı (**hedef, henüz oluşturulmamış**):

```text
adsiz-dil/
├── README.md
├── CONTRIBUTING.md
├── GOVERNANCE.md
├── CHANGELOG.md
├── standard/
│   ├── adsiz_dil_acik_anlam_standardi_v1_0.md   # DEĞİŞTİRİLMEYEN kaynak
│   └── manifest.json                            # sürüm + dosya özeti/hash
├── data/                                        # kaynakla denetlenmiş türev kayıtlar
│   ├── roots.jsonl
│   ├── lexemes.jsonl
│   ├── grammar.json
│   ├── semantic-roles.json
│   └── concepts.jsonl
├── schemas/
│   ├── lexeme.schema.json
│   └── proposal.schema.json
├── corpus/
│   ├── reference-sentences.jsonl
│   ├── dialogues.jsonl
│   └── minimal-pairs.jsonl
├── proposals/
│   └── README.md                                # yalnızca öneri kayıtları
├── tests/
│   ├── test_orthography.py
│   ├── test_morphology.py
│   ├── test_semantics.py
│   ├── test_roundtrip.py
│   ├── test_governance.py
│   └── test_examples.py
├── tools/
│   ├── read_dictionary.py
│   ├── parse_word.py
│   ├── propose_lexeme.py
│   └── validate_proposal.py
└── .agents/skills/
    ├── adsiz-speak/SKILL.md
    ├── adsiz-translate/SKILL.md
    ├── adsiz-literary/SKILL.md
    ├── adsiz-tutor/SKILL.md
    ├── adsiz-research/SKILL.md
    ├── adsiz-propose/SKILL.md
    └── adsiz-audit/SKILL.md
```

`.agents/skills/` pek çok istemci için ortak yol tercihidir; Agent Skills standardı **belirli bir kurulum dizinini zorunlu kılmaz**. Başka istemciye bağlamak gerekirse aynı klasörleri istemcinin desteklediği dizine kopyalama/symlink veya paketleme kullanılabilir.

## 3. Yedi skill'in sorumlulukları

| Skill | Ne zaman çalışır? | Girdi → Çıktı | Yetki |
| --- | --- | --- | --- |
| `adsiz-speak` | Adsız Dil'de konuş / cümle çöz / düzelt | Sürüm + metin → anlamlı, doğal yanıt; bilinmeyene uyarı | **Salt-okunur** |
| `adsiz-translate` | Türkçe/İngilizce ↔ Adsız Dil | Metin + hedef üslup → çeviri, gloss, belirsizlik | **Salt-okunur** |
| `adsiz-literary` | Roman diyaloğu, şiir, hitap ve üslup | Tür + bağlam → edebî metin, ifade tercihleri | **Salt-okunur** |
| `adsiz-tutor` | Dil öğretimi, alıştırma, düzeltme | Seviye + hedef → aşamalı ders, cevap anahtarı | **Salt-okunur** |
| `adsiz-research` | Korpus incelemesi / sözlük boşluğu tespiti | İzinli konuşma korpusu + sürüm → kanıtlı ihtiyaç raporu | **Salt-okunur** |
| `adsiz-propose` | Yeni sözcük/ek/terim öner | Kavram → açık-anlam ayrıştırma + kısa ad + şema uyumlu PR taslağı | **Yalnızca `proposals/`** |
| `adsiz-audit` | Öneri ve eski sürümü doğrula | Sürüm + değişiklik → fonoloji/gramer/anlam/regresyon raporu | **Salt-okunur** |

**Neden yedi ayrı skill?** Konuşmanın güvenilirliği ile yeni kelime türetmenin yaratıcı serbestliği birbirinden ayrılır. Korpus araştırmacısı otomatik sözlük editörü değildir. Denetçi öneriyi yazan agent'tan ayrı çalışabilir. İlerde iki skill'in aynı görevi sürekli yaptığını ölçersek birleştiririz; sırf sayı artsın diye skill üretmeyiz.

**Pasif araştırma gerçek işleyişi:** Skill tek başına arka planda çalışmaz. Otomasyon, CI tetikleyicisi veya kullanıcının çalıştırdığı oturum, yalnızca izinli/metinden arındırılmış korpusu `adsiz-research`e verirse eksik ifade kayıtları oluşur. Hiçbir sohbet gizlice toplanmaz; kullanıcı veri rızası ve silme politikası olmalıdır.

## 4. Agent Skills standardına uygunluk

Her skill asgari `SKILL.md` taşır: YAML frontmatter + Markdown gövdesi. `name` 1–64 karakter, küçük ASCII harf/sayı/tire; klasör adıyla aynı, `description` 1–1024 karakter. İsteğe bağlı `license`, `compatibility`, `metadata`, `allowed-tools` vardır; `allowed-tools` deneysel ve tüm istemcilerde aynı izin anlamına gelmeyebilir.

**Örnek yalnızca taslak frontmatter:**

```yaml
---
name: adsiz-speak
description: Use this skill when a user asks to speak, interpret, correct, or explain sentences in the Adsız Dil constructed language. Load the pinned language standard; preserve approved roots, morphology, honorifics, pronunciation and uncertainty rules. Do not coin new official vocabulary.
metadata:
  language-standard: "1.0"
---
```

`SKILL.md` kısa, açık amaçlı ve prosedürel olmalı: **ne zaman etkinleşir → hangi manifest'i okur → hangi işlemleri yapar → bilinmeyen durumda ne der → hangi kayıtları asla değiştirmez → hangi testleri çağırır**. Ayrıntılı sözlük `references/` veya ortak veride kalsın. Resmî yönerge küçük skill gövdeleri, göreve göre açılan `references/` ve `scripts/` kullanımını önerir. Doğrulama: `skills-ref validate <skill-directory>` (aracı ortamda önceden kurup sürüm sabitle).

## 5. Normatif veri şeması ve kısa adın güvenilirliği

Önerilen **kavram kimliği** (`concept_id`) ile **sözcük biçimi** (`lexeme_id`) farklı tutulur. Bir sözcük birden fazla anlama gelebilir; iki sözcük aynı kavrama referans verebilir. Karışıklığı önlemek için `sense_id` zorunlu.

```json
{
  "proposal_id": "draft-0001",
  "status": "proposal",
  "proposed_form": "yemali",
  "category": "noun",
  "concept_id": null,
  "sense_id": null,
  "definition_tr": "Açık tanım örneği; kesin elma kimliği iddia edilmez",
  "transparent_form": "meyar-ro-yenar-li-reş-ze-selim-mu-molir",
  "semantic_strength": "typical",
  "dictionary_snapshot": "1.0",
  "phonotactic_validation": "pending",
  "collision_validation": "pending",
  "evidence": [],
  "proposer": "agent",
  "reviewer": null,
  "approved_by_human": false
}
```

**Kritik semantik ayrım:** `meyar-ro-yenar-li-reş-ze-selim-mu-molir` genel meyve sınıfını ve bazı *tipik* nitelikleri açıklar; **özgül elma kimliğini kanıtlamaz**. Tanımlar doğrulanmamış veya yaklaşık ise olasılık seviyesi saklanır. `Jajaya` gibi bilinmeyen kısa ad, açıklama veya ortak sözlük olmadığı sürece bilinmiyor kabul edilir. Nitelik → kimlik kestirimi `confidence`/`uncertainty` ile birlikte raporlanır.

### Çözümleme sırası (`adsiz-speak` / `adsiz-translate`)
1. Normalizasyon: NFC, Türkçe ı/i kuralları, kanonik yazım; istemsiz toplu dönüştürme yok.
2. Manifest sürümü ve sözlük hash'i uyumlu mu?
3. Tam biçim + anlam eşleşmesi varsa onu kullan.
4. Çekim/türetim varsa kök-ek çözümlemesi; *kayıtsız üretimi kesin anlam diye sunma*.
5. Tireli AAK ifadelerinde baş sınıf + rol/değer ilişkileri; tip denetimi.
6. Kayıtsız bitişik birleşikte çoklu çözüm varsa adayları ayrı göster.
7. Sözlük dışı kısa biçime kesin anlam verme; gerekirse açıklama iste.

## 6. İnsan onaylı değişiklik akışı

```text
KULLANIM / İZİNLİ KORPUS
       ↓
Eksik kavram/ifade tespiti (`adsiz-research`)
       ↓
AAK tanımı + önerilen kısa ad (`adsiz-propose`)
       ↓
Otomatik validator + ayrı agent incelemesi (`adsiz-audit`)
       ↓
Pull request: gerekçe / olası çakışmalar / örnekler / geri dönük uyum
       ↓
İNSAN ONAYI (gerekiyorsa dil sahibi; kilitli çekirdekte daima)
       ↓
Sürüm, değişiklik günlüğü, veri/skill sürümü senkronizasyonu
       ↓
Kabul edilmiş sözcükler sonraki agent oturumlarında kullanılabilir
```

**Yetki ilkeleri:** 
- `owner_locked` anlamını, imlasını veya telaffuzunu değiştirmek yalnızca dil sahibinin açık onayıyla.
- `owner_accepted_working` için anlam değişikliği/onay mercii tanımlanmalı; bu kurulmadan otomatik kabul yok.
- `delegated_v1` dâhil mevcut standardın kayıtlı biçimleri sessizce yeniden tanımlanmaz. Yeni öneriler ayrı versiyonlanır; yanlış kayıt için *deprecation + gerekçe + göç yolu*.
- `proposal` hiçbir zaman resmî sözlük veya yayımlanmış kitap çevirisinde sanki kesin sözcükmüş gibi gösterilmez.
- AI'nın PR açabilmesi, PR birleştirebilmesi demek değildir. Varsayılan olarak agentların ana dala yazma ve release yayımlama yetkisi yoktur.
- Lisans politikası ayrı seçilmeli: betikler için MIT/Apache-2.0 aday, açıklayıcı metin/korpus için CC BY 4.0 aday; kullanım hakları ve katkı şartları yayın öncesi açıkça belirlenmeli. Dilin kendisinin mülkiyetini bu öneri otomatik olarak tanımlamaz.

## 7. Doğrulama matrisi

| Kategori | Başarı testi | Kritik hata |
| --- | --- | --- |
| Skill biçimi | Her `SKILL.md` resmî validator'ı geçiyor | Geçersiz frontmatter, yanlış klasör adı |
| Skill tetiklenmesi | Konuşma sorusunda `adsiz-speak`, çeviride `adsiz-translate`, yeni terimde `adsiz-propose` | Alakasız skill'in tetiklenmesi |
| Kaynak tutarlılığı | 34 kilitli kökün ve `sen` hitabının değişmediğini doğrula | `seri`/`ser` gibi reddedilmiş biçimin standartlaştırılması |
| Yazım | Yalnızca 28 harf, uygun birleşimler, vurgu | 3+ bitişik ünlü/ünsüz, yanlış karakter |
| Morfoloji | `Sael → Saelen`, `Lera → Lerana`, `Sai → Sain` ve kök istisnaları | `Oren` gibi kökü sahte fiil diye okuma |
| Cümle | SVO/SOV aynı roller, doğru nesne işareti; zaman ve olumsuzluk | Nesne/özne karıştırma |
| Anlam/ontoloji | `meyar` meyve, `yenar` ağaç; `produced_by` ile `is-a` ayrımı | Meyveyi ağaç alt sınıfı sayma |
| Belirsizlik | `Jajaya` bilinmiyor; açık tanım elma garantilemiyor | Uydurma kesin karşılık |
| Geri çevrim | Yapısal tanım → AAK → yapısal tanım aynı rol kümesi | Sessiz rol kaybı |
| Ses estetiği | Anadil konuşur/dil öğrenicisi okumaları, ritim puanı | Mekanik, boğumlaması zor terimler |
| Yetki | `adsiz-propose` sadece `proposals/` yazabiliyor | Onaysız standart değişikliği |
| Sürüm | Pinned manifest hash'i; yeni v1.1 kullanan agent ile eski v1.0 farkı açık | Ajanlar arası sessiz sözlük ayrışması |
| Güvenlik | PR açıklamalarındaki komutlar veri olarak kalıyor | Prompt injection, gizli veri sızıntısı |

Önerilen ilk *golden* örnekler: `Mei saelen sain.`, `Mei sain saelen.`, `Alei, Elora sen!`, `Meina va avelen.`, `Mei ri lem.`, `Mei da fa sileven tüvanan.`, `Jajaya` (bilinmiyor), `meyar-ro-yenar-li-reş-ze-selim-mu-molir` (meyve, elma kesin değil).

Testleri şu şekilde bölün: (1) deterministik Python doğrulayıcı, (2) agent with/without skill değerlendirmesi, (3) konuşurlarla ses ve doğallık değerlendirmesi. İlk ikisi başarılmış olsa bile üçüncünün başarılı olduğu varsayılmaz.

## 8. Sürüm ve dağıtım

- Dil standardı (`language_version`) ile skill paketi (`skills_version`) **ayrı sürümlenir**. Örn. `language_version=1.0`, `skills_version=0.1.0`.
- `manifest.json` her verinin sürümünü ve SHA-256 özetini tutar; bütün skill'ler aynı snapshot'ı okur.
- Dokümantasyon/uyumlu yazım düzeltmesi → patch; geriye uyumlu yeni sözcük/sözcük anlamı → minor; mevcut sözcük anlamını veya grameri bozan değişiklik → major ve insan onayı. Bu sınıflandırma proje politikasıdır, Agent Skills standardının zorunluluğu değildir.
- Canlı agent konuşmasında sürüm bilgisi sabit kalır; güncelleme geldiğinde oturum ortasında gizli sözlük değiştirilmez. Sonraki oturumda uyum kontrolü.
- Halihazırdaki `v1.0.md` **değiştirilmeden** `standard/` içine alınır; yeni şemalar `data/` altında *türev* olarak tutulur. Her dönüştürme karşılaştırma raporu üretir.
- Skills'in kendisi otomatik arka plan takip servisi değildir. Korpus analizini otomatikleştirmek için ayrıca kullanıcı izinli CI/job ve etkin tetikleyici gerekir.

## 9. Ölçülebilir aşamalar (henüz uygulanmıyor)

**Aşama 0 — Salt-okunur envanter:** v1.0 dosyası ve eski kararların korunma envanteri, risk/çelişki raporu; hiçbir gramer değişikliği yok.

**Aşama 1 — Veri ve doğrulama:** deterministik sözlük/veri dışa aktarımı, JSON Schema, CLI doğrulama ve 101 örnek cümle regresyonu; normatif kaynak değişmez.

**Aşama 2 — İlk 2 skill:** `adsiz-speak` ve `adsiz-translate`, farklı agentlarda temiz bağlamla test; yanlış anlamayı ve uydurmayı ölç.

**Aşama 3 — Öneri / denetim:** `adsiz-research`, `adsiz-propose`, `adsiz-audit`; PR taslakları, *merge yetkisi olmadan*.

**Aşama 4 — İnsan dili kalitesi:** `adsiz-literary`, `adsiz-tutor`; telaffuz/üslup korpusu, A1 benzeri insan kullanımı deneyleri, *gerçek kullanıcı değerlendirmesi*.

**Aşama 5 — Topluluk:** açık katkı kılavuzu, sürümlü release, açık değerlendirme raporları, çakışma çözüm kurulu, köklü değişikliklerde sahibin son sözü.

## 10. Agent'a verilecek geliştirilmiş inceleme talimatı

> Bu bölüm uygulama izni değil, başka bir geliştirme agentına gönderilecek **salt-okunur inceleme brief'i**dir.

**ROL:** Dilbilim, morfoloji, fonoloji, bilgisayarlı dilbilim, veri şeması ve Agent Skills mühendisliği uzmanı.  
**GÖREV:** Önce `adsiz_dil_acik_anlam_standardi_v1_0.md` dosyasını ve projedeki diğer mevcut kaynakları oku. Sonra resmî `https://agentskills.io/specification` ve ilgili rehberlerle uygunluğu doğrula. Amaç agentlar arası kapalı protokol değil; insanların ilk dili olabilecek nitelikte gelişmeye açık modern bir insan dili.  
**KIRMIZI ÇİZGİLER:** Onaylı kökler, 28 harfli alfabe, ses/vurgu ilkeleri, `-en`, `-na`, SVO/SOV, cinsiyetsiz zamirler, `sen/mel/rin/ael`, sürümlü AAK asla sessizce değiştirilmesin. `ser`/`seri` reddedilmiştir.  
**İLK TESLİM:** (a) mevcut envanter ve belge içi tutarlılık raporu, (b) skill sorumluluk matrisi, (c) tek kaynak ve veri şeması taslağı, (d) insan onaylı PR akışı, (e) güvenlik/kalite matrisi, (f) aşamalı uygulama planı.  
**İZİN SINIRI:** Ana dile, kayıtlı sözlüğe, `SKILL.md` kurulumuna veya Git ana dalına yazma. Gerekirse yalnızca `proposal` raporu üret. Değişiklik için önce insan onayı iste.  
**KALİTE KOŞULU:** Kanonik kaynağı göster, resmi standardı referans ver, belirsiz anlamı kesinleştirme, gerçekten çalıştırılmamış test için 'pass' deme, gerçek konuşurluğu varsayma.

## Kaynaklar

- Mevcut dil standardı: `adsiz_dil_acik_anlam_standardi_v1_0.md` (5 Kasım 2026)
- Agent Skills Specification: https://agentskills.io/specification
- Best practices: https://agentskills.io/skill-creation/best-practices
- Evaluating skills: https://agentskills.io/skill-creation/evaluating-skills
- Optimizing descriptions: https://agentskills.io/skill-creation/optimizing-descriptions
- Client implementation: https://agentskills.io/client-implementation/adding-skills-support
