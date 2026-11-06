# Pilot Experiment 01: Five-Stanza Linguistic Audit & Empirical Traceability (Audited L5.2 Edition)

**Experiment Date:** 2026-11-05 / 2026-11-06  
**Language Standard Under Test:** Alei v1.1.0-RC (PR #8 overlay)  
**Agent A (Encoder):** ChatGPT (temporary chat; provided with Alei v1.1.0 standard and original Turkish source; instructed to use canonical vocabulary and report omissions)  
**Agent B (Decoder):** Gemini (independent chat; provided ONLY with the Alei text output of Agent A and Alei v1.1.0 standard; blinded to original Turkish source, notes, and translator omissions)  
**Corpus Scope:** Curated excerpt of 5 stanzas (K1–K5) of an original 10-stanza Turkish poem.  
**Provenance & Integrity Status:** Real empirical observation of ONE limited pilot trial. Stanzas K6–K10, precision pairs M01–M12, and fictional concepts C1–C4 have NO observed decoder output. No missing transcripts are fabricated. Private gold test source is preserved outside public version control.

---

## 1. Executive Summary & Evidence Reality

The purpose of this pilot experiment was to observe how Alei v1.1.0 performs when transmitting complex human literary meaning across independent cognitive models under blind conditions.

### 1.1 Corrected False Claims of the Previous L5.1 Report
The previous L5.1 report conjectured interpretations without the original test source in hand, resulting in several false empirical claims that are now formally retracted:

1. **Retraction on K1 ("City's Seven Gates"):**
   - *Previous false claim:* The report claimed Agent A confused `Nave` (city) with nine, translating "nine doors", and that Gemini echoed "dokuz kapı".
   - *Empirical reality:* The original Turkish source line was *"Şehrin yedi kapısından yalnız üçü açıktı"*. Agent A encoded `Nave ri növi lürana. Teli lüra fal ve.` using canonical `Nave` (roots:476, city), `növi` (functions:1106, seven), and `teli` (functions:1102, three). Gemini correctly back-translated: *"Şehrin yedi kapısı. Üç kapı açık."* Neither model hallucinated "nine doors".
2. **Retraction on K4 ("Fear and Thinking"):**
   - *Previous false claim:* The report claimed Agent A used `vürelen` as "cross" (geçmek) and `aremen` as "return" (dönmek), and that Gemini echoed "geçme" and "dön".
   - *Empirical reality:* The original Turkish source line was *"Bize 'Korkma,' demediler; 'Korksan da düşün,' dediler."* Agent A encoded `Elina ne da vesen: “Ne vürelen!” Elina da vesen: “Şe Sai vürelen, aremen!”` using canonical `vürelen` (roots:502, fear) and `aremen` (roots:434, think). Gemini correctly back-translated: *"Onlar 'Korkma!' demedi. Onlar 'Eğer korkarsan, düşün!' dedi."* Neither model hallucinated "crossing" or "returning".
3. **Retraction on K4.2 ("Learning"):**
   - *Previous false claim:* The report claimed `Meina da nivaren` was interpreted as "gece bekledik" (nightwatch).
   - *Empirical reality:* The original Turkish source was *"Cesaretin, korkunun yokluğu olmadığını öğrendik."* Agent A encoded `Meina da nivaren.` and Gemini correctly translated *"Biz öğrendik."* (`nivaren` = learn).
4. **Retraction on "Mutual Lexical Hallucination":**
   - The models did NOT engage in a mutual hallucinatory echo chamber regarding canonical vocabulary. Both ChatGPT and Gemini correctly understood and translated canonical roots: `Nave` (city), `vürelen` (fear), `aremen` (think), and `nivaren` (learn).

### 1.2 Genuine Observed Shortcomings in the Pilot Trial
While basic lexical recognition succeeded for attested roots, the pilot revealed four severe structural and communicative failures:

1. **Catastrophic Encoder Information Omission (The Lexical Bottleneck):**
   Because Alei v1.1 lacked words for common literary, relational, and adverbial concepts, Agent A dropped entire clauses and modifiers rather than explaining them:
   - In K1.3, the entire patient ("yıldızları saymadım; sönmüş olanı") was omitted (`Mei ne da belemen. Mei da hüvaren.`), leaving Gemini with unexpressed objects.
   - In K1.4, four critical elements ("kaybolan", "bazen", "yön", "göstermek") were dropped (`Sira pemar el da yelen ke miraven.`).
   - In K5.4, an entire complex antithetical clause (*"Bir harita doğruydu, fakat yanlış bir yeri gösteriyordu"*) was reduced to `Ena nerav.` (A model), discarding over 85% of the proposition!
2. **Uncanonical Vocabulary Inventions by Agent A:**
   When unable to find words, Agent A coined unapproved terms directly in the test output:
   - `miŋ` (sound/voice) in K4 (`Sira miŋ ne Meina ri miŋ.`).
   - `dumen` (extinguish/close) in K5 (`Şe Sai dumen...`).
3. **Grammatical Underspecification & Valency Clash:**
   - In K5.1, `vel ne va nesalen` placed the Theme/Patient in subject position with transitive verb `nesalen`, producing a valency clash. Gemini detected this ambiguity, noting *"yol kaybolmayacak (kaybetmeyecek)"*.
   - In K1.1 and K4.3, stative predicates were expressed via action noun + postposition (`lüra fal ve`), obscuring aspectual distinctions.
   - In K4.1, concessive "Korksan da" was collapsed into simple conditional `şe` ("Eğer korkarsan").
4. **Poorly Calibrated Model Confidence:**
   Gemini reported subjective self-confidence of 95–99% while translating strings that had lost massive portions of the source poem's semantic content.

---

## 2. Complete 20-Line Empirical Alignment Table (K1–K5)

The following table documents every observed line across the pilot trial, aligning original Turkish source, Agent A's Alei encoding, and Agent B's natural Turkish decoding:

| ID | Orijinal Türkçe Kaynak | Agent A (Alei Çıktısı) | Agent B (Gemini Doğal Türkçe) | Kaynak Önerme (Proposition) | Encoder Bilgi Koruma | Decoder Bilgi Koruma | Sözlük ve Gramer Kanıtı | Belirsizlik ve Notlar |
|---|---|---|---|---|---|---|---|---|
| **K1.1** | Şehrin yedi kapısından yalnız üçü açıktı, | `Nave ri növi lürana. Teli lüra fal ve.` | Şehrin yedi kapısı. Üç kapı açık. | Şehre ait 7 kapı; yalnız 3'ü açık durumda. | `Nave` (şehir), `növi` (7), `lüra` (kapı), `teli` (3) korundu. "Yalnız" (partitif odak) düştü. | Şehrin 7 kapısı ve 3 açık kapı doğru aktarıldı. | `Nave` (roots:476), `növi` (functions:1106), `teli` (functions:1102), `fal` (roots:32). | `fal ve` durum calque'ı. |
| **K1.2** | Dördüncüde bir çocuk, hiç görmediği sabahı bekledi. | `Ena pira da lüfaren deiran. Eli ne da liren deiran.` | Bir çocuk sabahı bekledi. O, sabahı görmedi. | 4. kapıda çocuk; ömründe görmediği sabahı bekleyiş. | `ena pira` (çocuk), `deiran` (sabah/gün), `ne da liren` (görmedi). "Dördüncüde" ve deneyimsel bitmişlik düştü. `lüfaren` (düşmek) eklendi. | "Bir çocuk sabahı bekledi. O sabahı görmedi." | `ena pira` (küçük insan), `dei` (roots:454, gün/sabah), `liren` (roots:514, görmek). | Gemini "bekledi" anlamını bağlamdan çıkardı; `lüfaren deiran` gramer dışı. |
| **K1.3** | Ben yıldızları saymadım; sönmüş olanı aradım, | `Mei ne da belemen. Mei da hüvaren.` | Ben hesaplamadım. Ben aradım. | Konuşucu yıldızları saymadı; söneni aradı. | `Mei ne da belemen` (saymadım), `Mei da hüvaren` (aradım). **"Yıldız" ve "sönen" nesnesi tamamen atıldı!** | "Ben hesaplamadım. Ben aradım." (Nesneler eksik). | `belemen` (roots:446), `hüvaren` (roots:524). "Yıldız" kanonda yoktur (sözlük açığı). | Sıfır-anafor; nesne yokluğu sebebiyle anlamsal boşluk. |
| **K1.4** | Çünkü kaybolan ışık da bazen yön gösterebilirdi. | `Sira pemar el da yelen ke miraven.` | Çünkü parlaklık da yardım edebildi. | Kaybolan ışık da ara sıra yön göstermeye yardım edebilirdi. | `sira` (çünkü), `pemar` (ışık), `el` (de/da), `miraven` (yardım etmek). **"kaybolan", "bazen", "yön", "göstermek" düştü.** | "Çünkü parlaklık da yardım edebildi." | `sira` (functions:1074), `pemar` (roots:589), `miraven` (AD-2026-002). | Ciddi bilgi kaybı; 4 kritik kavram dilde kök olmadığı için atıldı. |
| **K2.1** | Dün verdiğim sözü bugün geri alamam, dedim; | `Mei da davelen vesan Dora. Dena Mei ne yelen ke avaren vesan. Mei da vesen.` | Dün sözü verdim. Bugün sözü alamıyorum. Konuştum. | Dün verilen sözün bugün geri alınamayacağının söylenmesi. | `davelen vesan Dora` (dün söz verdim), `Dena... ne yelen ke avaren` (bugün alamam), `Mei da vesen` (dedim). | "Dün sözü verdim. Bugün sözü alamıyorum. Konuştum." | `Dora` (roots:485, dün), `Dena` (roots:481, bugün), `davelen` (roots:527), `avaren` (roots:459). | Kanonik zaman kökleri `Dora` ve `Dena` başarıyla kodlandı ve çözüldü. |
| **K2.2** | Oysa sözün sahibi ben değil, onu duyanlardı. | `Lia Mei ne mehaven vesan. Elina da tiren vesan.` | Ama söz elimde değil (söze sahip değilim). Onlar sözü duydu. | Sözün sahibi konuşucu değil, dinleyenler. | `Lia` (ama), `Mei ne mehaven` (sahip değilim), `Elina da tiren` (onlar duydu). | "Ama söz elimde değil. Onlar sözü duydu." | `lia` (functions:1073), `mehaven` (roots:438, sahip olmak), `tiren` (roots:449, duymak). | Başarılı anlamsal aktarım. |
| **K2.3** | Bir taşın üstüne adımı değil, hatamı yazdım, | `Mei ne da yelaren Mei ri siman liman lo. Mei da yelaren liman lo.` | Benim adımı taşa yazmadım. Taşa yazdım. | Taşa adını değil, hatasını yazma eylemi. | `Mei ne da yelaren Mei ri siman` (adımı yazmadım). **"Hata" sözcüğü atıldı!** İkinci cümlede sadece taşa yazdım dendi. | "Benim adımı taşa yazmadım. Taşa yazdım." | `yelaren` (roots:509, yazmak), `siman` (roots:457, işaret/ad), `liman` (roots:456, taş). | "Hata" kökü v1.1'de olmadığı için Encoder nesneyi düşürdü. |
| **K2.4** | Yağmur adı sildi; hata taşta kaldı. | `Nuşa da nüselen siman. Liman lo.` | Yağmur adı temizledi. Taşta. | Yağmurun adı silmesi; hatanın taşta kalması. | `Nuşa da nüselen siman` (yağmur adı sildi), `Liman lo` (taşta). "Hata kaldı" önermesi atıldı. | "Yağmur adı temizledi. Taşta." | `nuşa` (roots:517, yağmur), `nüselen` (roots:538, temizlemek). | `Liman lo.` eksiltili parça. |
| **K3.1** | İki dost, aynı köprüye ayrı uçlardan vardı; | `Davi samel da pürelen vümar ta.` | İki dost köprüye geldi. | İki dostun aynı köprüye zıt uçlardan ulaşması. | `davi samel` (iki dost/aynı), `pürelen vümar ta` (köprüye vardı). **"ayrı uçlardan" vektörü atıldı.** | "İki dost köprüye geldi." | `davi` (functions:1101), `samel` (roots:440), `pürelen` (roots:431), `vümar` (roots:501). | Karşıtlık kökü eksikliği sebebiyle yön vektörü kayboldu. |
| **K3.2** | Biri geçmek istedi, öteki köprüyü onarmak. | `Ena samel da naelen ke avelen; ena samel da naelen ke lümalen vümaran.` | Bir dost gitmek istedi; bir dost köprüyü onarmak istedi. | Biri geçmek istedi; diğeri köprüyü onarmak. | `avelen` (gitmek), `lümalen vümaran` (köprüyü onarmak) tam korundu. | "Bir dost gitmek istedi; bir dost köprüyü onarmak istedi." | `naelen` (roots:439, istemek), `avelen` (roots:432), `lümalen` (roots:667, onarmak). | Yüksek doğruluk; `lümalen` tam çözüldü. |
| **K3.3** | “Önce beni dinle,” dedi en sessiz kalan, | `“Tiren Mein!” Eli da vesen.` | “Beni duy (dinle)!” dedi o. | En sessiz olanın "Önce beni dinle" demesi. | `Tiren Mein!` (Beni dinle!), `Eli da vesen` (dedi o). "Önce" ve "en sessiz kalan" atıldı. | "“Beni duy (dinle)!” dedi o." | `tiren` (roots:449, duymak/dinlemek), `mein` (1SG.ACC), `vesen` (söylemek). | Üstünlük derecesi ve zaman zarfı atıldı. |
| **K3.4** | Ve ikisi de ilk kez cevap vermeden durdu. | `Elina da şürelen. Elina ne da revalen.` | Onlar ayakta durdu (ayağa kalktı). Onlar yanıtlamadı. | İkisinin de ilk kez yanıt vermeden durması. | `şürelen` (ayakta durdu), `ne da revalen` (yanıtlamadı). "İlk kez" ve "ikisi de" atıldı. | "Onlar ayakta durdu. Onlar yanıtlamadı." | `şürelen` (roots:659, ayakta durmak), `revalen` (roots:443, yanıtlamak). | Kanonik kökler tam eşleşti. |
| **K4.1** | Bize “Korkma,” demediler; “Korksan da düşün,” dediler. | `Elina ne da vesen: “Ne vürelen!” Elina da vesen: “Şe Sai vürelen, aremen!”` | Onlar “Korkma!” demedi. Onlar “Eğer korkarsan, düşün!” dedi. | "Korkma" denmediği; "Korksan bile düşün" dendiği. | `vürelen` (korkmak) ve `aremen` (düşünmek) tam korundu. Ödünleyici "korksan da" koşula (`şe`) indirgendi. | "Onlar 'Korkma!' demedi. Onlar 'Eğer korkarsan, düşün!' dedi." | `vürelen` (roots:502, korkmak), `aremen` (roots:434, düşünmek). | **Kanonik anlamlar korundu.** Şart/ödünleme ayrımı belirsizleşti. |
| **K4.2** | Cesaretin, korkunun yokluğu olmadığını öğrendik. | `Meina da nivaren.` | Biz öğrendik. | Cesaretin korkunun yokluğu olmadığının öğrenilmesi. | `Meina da nivaren` (öğrendik). **Tüm nesne yan tümcesi ("cesaretin...") atıldı!** | "Biz öğrendik." | `nivaren` (roots:721, öğrenmek). | **Gemini doğru çevirdi ("öğrendik").** Aşırı içerik kaybı. |
| **K4.3** | Üçüncü gece kapı açıldı, fakat içeri girmedik, | `Lüra fal ve. Lia Meina ne da avelen.` | Kapı açık. Ama biz gitmedik. | 3. gece kapının açılması ama içeri girilmemesi. | `Lüra fal ve` (kapı açık), `Lia... ne da avelen` (ama girmedik). "Üçüncü gece" zamanı atıldı. | "Kapı açık. Ama biz gitmedik." | `lüra` (kapı), `fal` (açılma), `ve` (ile), `avelen` (gitmek). | Zamansal çapa eksikliği; `fal ve` durum calque'ı. |
| **K4.4** | Çünkü içerideki ses bize ait değildi. | `Sira miŋ ne Meina ri miŋ.` | Çünkü ses, bizim sesimiz değil. | İçerideki sesin konuşuculara ait olmaması. | `sira` (çünkü), `miŋ` (uydurma: ses), `ne Meina ri miŋ` (bizim sesimiz değil). "İçerideki" atıldı. | "Çünkü ses, bizim sesimiz değil." | `miŋ` kanonda yoktur (Agent A tarafından uyduruldu). | Kanon dışı sözcük sızıntısı. |
| **K5.1** | Eğer son lambayı söndürürsen, yol yine kalır; | `Şe Sai dumen, vel ne va nesalen.` | Eğer kapatırsan, yol kaybolmayacak (kaybetmeyecek). | Son lamba söndürülse bile yolun kalacağı. | `şe Sai dumen` (kapatırsan), `vel ne va nesalen` (yol kaybetmeyecek/kaybolmayacak). "Son lamba" atıldı. | "Eğer kapatırsan, yol kaybolmayacak (kaybetmeyecek)." | `dumen` (kanon dışı/karanlık kökünden), `nesalen` (roots:525, geçişli). | **Gemini valans çatışmasını tespit etti: "(kaybetmeyecek)".** |
| **K5.2** | Ama kimse birbirinin yüzünü seçemeyebilir. | `Lia Elina ne yelen ke liren.` | Ama onlar göremiyor. | Kimsenin diğerinin yüzünü seçememe olasılığı. | `Lia Elina ne yelen ke liren` (ama onlar göremiyor). "Kimse", "birbirinin yüzü" atıldı. | "Ama onlar göremiyor." | `lia` (ama), `elina` (3PL), `yelen` (ebilmek), `liren` (görmek). | Ağır basitleştirme. |
| **K5.3** | Yol kaybolduğunda değil, adı değiştiğinde şaşırdık; | `Vel ri sima da yümalen. Meina da sülari.` | Yolun adı değişti. Biz şaşkındık (şaşırdık). | Şaşkınlığın yol kaybolunca değil, adı değişince yaşanması. | `Vel ri sima da yümalen` (yolun adı değişti), `Meina da sülari` (şaşırdık). "Yol kaybolduğunda değil" atıldı. | "Yolun adı değişti. Biz şaşkındık (şaşırdık)." | `siman` (ad), `yümalen` (düzeltilmek/değişmek), `sülari` (roots:482, şaşkın). | Zıtlık yan tümcesi atıldı; `sima` imla kusuru. |
| **K5.4** | Bir harita doğruydu, fakat yanlış bir yeri gösteriyordu. | `Ena nerav.` | Bir model (temsil). | Haritanın doğru olduğu ama yanlış bir yeri gösterdiği. | `Ena nerav.` (Bir model/temsil). **Cümlenin %85'i ("doğruydu, fakat yanlış yeri gösteriyordu") atıldı!** | "Bir model (temsil)." | `ena` (functions:1100), `nerav` (roots:681, model/yapı). | **En vahim encoder kaybı.** Harita ve mekansal doğruluk terimleri eksik. |

---

## 3. Ek Kanonik Hataların Düzeltilmesi: Yıldız ve Ay Ayrımı

### 3.1 `Nüra` Kökünün Hakiki Kanonik Anlamı: "Ay / Gök Cismi" (Moon)
- `data/roots.jsonl` (satır 61, `roots:497`):
  ```json
  {"canonical_spelling": "Nüra", "gloss_tr": "ay, gök cismi", "id": "roots:497", "semantic_anchor_en": "moon", "status": "owner_accepted_working", "version": "1.0"}
  ```
- Önceki L5.1 taslağında `Nüra` kökünün sessizce "yıldız" yerine ikame edilmesi **kabul edilemez bir metodolojik hatadır**.
- `Nüra` kökünün İngilizce anlamsal çapası kesinlikle **`moon` (ay)**'dır. Türkçe gloss'undaki "gök cismi" ibaresi genel astronomik gök cisimlerini kapsasa da, doğrudan "yıldız" (star) anlamına gelmez.

### 3.2 Yıldız (Star) İçin Doğrulanmış Sözlük Açığı (`GAP-LEX-STAR`)
- Bütün v1.0 standardı, `roots.jsonl`, `lexemes.jsonl` ve `functions.jsonl` tarandığında:
  - `Sümei` (`roots:496`): Güneş (Sun)
  - `Nüra` (`roots:497`): Ay (Moon)
  - `Siril` (`roots:549`): Gökyüzü (Sky)
  - `Pemar` (`roots:589`): Parlaklık / Işık (Brightness / Light)
  - **Yıldız (Star) için kanonik bir kök BULUNMAMAKTADIR.**
- Bu durum resmi olarak **`GAP-LEX-STAR`** sözlük açığı olarak kayda geçirilmiştir.
- Kanonu bozmadan yıldız kavramını karşılamak için iki meşru yol vardır:
  1. **Şeffaf Kanonik Bileşik:** `siril-pemar` (gökyüzü ışığı) veya `siril-nüra` (gökyüzü gök cismi).
  2. **Aday Kök Önerisi:** Dil sahibinin onayına sunulmak üzere candidate root önerisi (örn. `Sir` veya `Pik`).

---

## 4. Dönüşlü/Edilgen Çatı Stratejilerinin Kapsamlı Karşılaştırması

### 4.1 Çakışma Analizi: `se` ve `ro` Parçacıklarının Durumu
Önceki taslaklarda dönüşlü çatı için önerilen parçacıkların ikisi de mevcut dilde çakışma üretmiştir:
1. **`se` Çakışması:** `functions:1080` (§8.6) gereği `se`, kanonik **vasıta/araç edatıdır** (`tüvan se` = aletle). Fiil önünde çatı parçacığı olarak kullanılması yapısal çakışma yaratır.
2. **`ro` Çakışması:** Standart v1.0 §5.4 ve `data/semantic-roles.json` gereği `ro`, Şeffaf Anlambilim (AAK) katmanında **`source_from` (kaynak)** rolüdür (`meyar-ro-nasel` = ormandan gelen meyve). Bu morfemin dilbilgisi parçacığı yapılması katmanlar arası çakışma üretir.

### 4.2 Dört Alternatif Çatı Stratejisinin Değerlendirme Matrisi

| Kriter | Strateji 1: Yeni Analitik Parçacık (örn. `vo` / `ko`) | Strateji 2: Özel Çatı Eki (örn. `-il-` / `-in-`) | Strateji 3: Çevresel/Dönüşlü Yapı (`samel` / `avelen`) | Strateji 4: Bağlamsal Valans Geçişliliği (Ergatif/Akuzatif Değişimi) |
|---|---|---|---|---|
| **Tanım** | Fiilden önce gelen yeni bir CV parçacığı (`Vel ne va vo nesalen`). | Fiil kökü ile mastar eki arasına gelen çatı eki (`nesal-il-en`). | Dönüşlü zamir veya yardımcı fiil ile analitik ifade (`vel da nesalen samel lo`). | Cansız özne ve nesnesiz kullanımda fiilin otomatik dönüşlü yorumlanması. |
| **Öğrenilebilirlik** | Yüksek (ayrık morfem). | Çok Yüksek (Türkçe -il/-in mantığına benzer). | Yüksek (mevcut sözcükleri kullanır). | Orta (örtük kural yükü). |
| **Çakışma Riski** | Düşük (boşta kalan `vo` gibi bir hece seçilirse). | **SIFIR (Kök ve ek yapısı tamamen yalıtılmış).** | **SIFIR (Sıfır yeni sözcük).** | **SIFIR (Morfolojik değişiklik yok).** |
| **Bileşik Saydamlığı** | Orta | Yüksek | Çok Yüksek | Düşük (belirsizlik riski). |
| **Geriye Uyumluluk** | v1.0 gramerine yeni fonksiyon sözcüğü ekler. | Morfoloji ayrıştırıcısına ek kuralı ekler. | **%100 Geriye Uyumlu (Hiçbir ek/kök gerektirmez).** | **%100 Geriye Uyumlu.** |
| **Ayrıştırıcı Karmaşıklığı** | Düşük | Orta | Çok Düşük | Yüksek (özne anlambilimini denetlemeli). |
| **Öneri ve Statü** | RFC Adayı | **En Güçlü Morfolojik Aday (RFC-2026-001)** | **Mevcut Kanonla Hemen Kullanılabilir** | Kural Belirsizliği Yaratır |

> [!IMPORTANT]
> Hiçbir yeni çatı eki veya parçacığı otomatik olarak kanonlaştırılmamıştır. Dil sahibi kararına kadar `src/alei_language/grammar.py` ve `valency.py` dosyalarında bu yapılar deneysel modda tutulmaktadır.

---

## 5. Türetim Anlambilimi Denetimi: `fal -> fali` ve `şe-el`

### 5.1 `fal -> fali` Türetiminin Durumsal Sınırları
Alei v1.0 §8.2, `-i` ekinin ad köklerinden niteleme sıfatı türettiğini belirtir (`sül` iyilik -> `süli` iyi). Bu kuralın eylem köklerine uygulanmasında anlamsal sınırlar netleştirilmiştir:

1. **Ayrım:**
   - *Açılmayla ilgili:* `fal-tüvan` (açma aygıtı).
   - *Açılır / Açılabilir:* `fal-yel` (açılabilir nitelik).
   - *Şu an açık (Durum Nitelik):* `fali` (Lüra fali = Kapı açık).
   - *Açılmış (Sonuçsal Olay):* `da fa falen` (Lüra da fa falen = Kapı açıldı/açılmış bulunuyor).
   - *Açılmakta olan (Süreç):* `du falen` (Lüra du falen = Kapı açılıyor).
2. **Kural Sınırı:**
   `-i` ile durum sıfatı türetimi **yalnızca fiziksel konfigürasyon ve tersinir durum bildiren eylem köklerinde** semantik olarak lisanslıdır (`fal` açılma -> `fali` açık). Süreç ve iletişim eylemlerinde (`ves` konuşma -> `*vesi`, `nivar` öğrenme -> `*nivari`) sonuçsal durum sıfatı türetilemez; bu köklerde `-i` failin karakter niteliğini türetir (`arem` düşünce -> `aremi` düşünceli).

### 5.2 `şe-el` Karşıt-Ödünleyici Bağlacı
- `şe` ("eğer", functions:1072) ve `el` ("dahi/bile", functions:1071) birleşimiyle oluşan `şe-el`:
  $$\mathbf{şe\text{-}el} + \text{Koşul Yan Tümcesi} + [,] + \text{Ana Tümce}$$
- **Anlamsal İşlev:** Ana tümcenin gerçekleşmesini koşulun gerçekleşme ihtimalinden bağımsız kılar.
- **Minimal Çift:**
  - *Koşul:* `Şe Sai vürelen, aremen.` (Eğer korkarsan düşün — korkmayabilirsin, ama korkarsan düşün).
  - *Ödünleme:* `Şe-el Sai vürelen, aremen!` (Korksan bile düşün — korku gelse dahi düşünmeyi bırakma!).
  - Örtük mantıksal varsayım uydurmaz; tamamen iki kanonik parçacığın bileşiminden oluşur.

---

## 6. Sonuç ve Önerilen Adımlar

Pilot Deney 01'in dürüst ve kanıta dayalı analizi göstermiştir ki:
1. Modeller kanonik kelime köklerini (`Nave`, `vürelen`, `aremen`, `nivaren`) doğru algılamaktadır.
2. Temel sorun "halüsinasyon" değil, **Alei'nin kelime haznesindeki aşırı darlık sebebiyle Encoder'ın bilgiyi sansürleyip atmasıdır**.
3. Bu nedenle öncelik, mevcut köklerin anlamlarını bozmadan şeffaf bileşikleri ve öncelikli yeni kökleri (`Pol`, `Bav`, `Tem`, `Şul`, `Yan`) disiplinli biçimde genişletmektir.
