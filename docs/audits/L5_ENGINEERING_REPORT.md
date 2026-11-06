# ALEI L5 DİL MÜHENDİSLİĞİ, KÖR ANLAMBİLİM VE TOPLULUK KALİTESİ RAPORU

**Tarih:** 2026-11-06  
**Depo:** `egecagintepe/alei-language`  
**Çalışma Dalı:** `l5/linguistic-engineering-community`  
**Temel Alınan Dal:** `owner/alei-v1.1-pr` (Taslak PR #8, SHA: `4a6a2b0e3d4073fdb9fb696b0a1aea20d5d9b19d`)  
**Onaylı Resmî Dil Adı:** Alei (AD-2026-001)  
**Onaylı v1.1.0 Yardım Kökü ve Fiili:** Mirav / Miraven (AD-2026-002)  
**v1.0 Değişmezlik Sağlaması (SHA-256):** `265fcc0dd0fcaf4bd23a062d631855463201be4ac12e42bf2501f30628ee8504` (`adsiz_dil_acik_anlam_standardi_v1_0.md`)

---

## 1. Yönetici Özeti ve Git Durumu Uzlaşması

L5 geliştirme aşaması, Alei'yi salt bir yapay zekâ simülasyonu olmaktan çıkarıp edebiyat yazarları, öğrenciler ve günlük konuşurlar için üretken, analiz edilebilir ve tutarlı bir **insan edebi dili** haline getirmek amacıyla yürütülmüştür.

### 1.1 Git Dalları ve Soykütüğü
1. `main` (SHA: `17356c8`): Başlangıç standardı ve çekirdek araçlar.
2. Taslak PR #7 (`phase-2/linguistic-integrity`, SHA: `8d8aa48`): 101 cümlelik bütünlük denetimi, korumacı sözdizim ayrıştırıcı.
3. Taslak PR #8 (`owner/alei-v1.1-pr`, SHA: `4a6a2b0`): Dil sahibinin AD-2026-001 (Alei adı) ve AD-2026-002 (Mirav/Miraven) kararlarını içeren v1.1.0 katmanı.
4. Yeni Çalışma Dalı `l5/linguistic-engineering-community`: PR #8'in en güncel uyumlu durumundan türetilmiş; hiçbir önceki dal ezilmemiş, geçmiş yeniden yazılmamış ve AleiFlow dallarına dokunulmamıştır.
5. **Erişilemeyen Yerel Dal Kısıtı:** Proje talimatında sözü edilen `l3/human-language-review` ve `l4/generative-v11` dalları yerel makinede veya uzak depoda mevcut değildir. Proje kuralları gereği bu durum bir kısıt olarak kayda geçirilmiş ve doğrulanmış en son durum olan PR #8 baz alınmıştır.

---

## 2. İlk Gerçek Bağımsız Kör Çeviri Deneyinin İncelenmesi (K1–K5)

ChatGPT (Ajan A) ve Gemini (Ajan B) arasında gerçekleşen 5 kıtalık kör çeviri deneyi, Alei'nin mevcut v1.1.0 standardındaki yapısal eksiklikleri somutlaştıran en değerli dilbilimsel veri kaynağımız olmuştur.

### 2.1 En Kritik Dört Anlam Kaybı Bulgusu ve Nedenleri

1. **Dönüşlü/Edilgen (Middle/Inchoative) Çatı Yokluğu (`Vel ne va nesalen`):**
   - *Sorun:* `nesalen` fiili kanonda kesinlikle geçişlidir (`[Özne-Fail] nesalen [Nesne-Etkilenen]`). Özne konumuna `vel` (yol) konulduğunda ve nesne verilmediğinde, cümlenin "yol bir şey kaybetmeyecek" mi yoksa "yol kaybolmayacak" mı olduğu belirsizleşmektedir.
   - *Kök Neden:* Alei v1.0/v1.1'de geçişli fiilleri dönüşlü veya kendiliğinden olma durumuna çeviren bir çatı biçimbirimi bulunmamaktadır.
2. **Durum (Stative) ile Olay (Dynamic Event) Ayrımının Yapılamaması (`Lüra fal ve`):**
   - *Sorun:* Çevirmen, "kapı açık" durumunu anlatabilmek için eylem ismi olan `fal` (açılma eylemi) ile edat olan `ve` (ile) sözcüklerini yan yana getirmiştir (`lüra fal ve`). Bu yapı kapının açık olma halini mi, açılmakta olduğunu mu, yoksa açılma eylemiyle bir iş yaptığını mı ayırt edememektedir.
   - *Kök Neden:* Fiil köklerinden düzenli niteleme/durum sıfatı türetme morfolojisinin (`-i`) eylem köklerine uygulanışının açıkça tanımlanmamış olması.
3. **Şart (`şe`) ile Karşıt-Ödünleyici (`şe-el` / -se bile) Kapsamının Birbirine Karışması (`Şe Sai vürelen, aremen!`):**
   - *Sorun:* Orijinal Türkçe şiirdeki "Geçsen bile dön!" uyarısı, Alei'de yalnızca `şe` (eğer) bulunduğu için "Eğer geçersen dön!" şeklinde kodlanmıştır. Bu durum, eylemin kaçınılmazlığını veya uyarının ödünleyici gücünü yok ederek koşullu bir izne dönüştürmüştür.
   - *Kök Neden:* Koşul bağlacı ile odak edatının bileşik yapısının dilde tanımlanmamış olması.
4. **Yönelim, Karşıtlık ve Zaman Sıklığı Ayrımının Yitimi (`Davi samel da pürelen vümar ta` & `Sira pemar...`):**
   - *Sorun:* İki kişinin köprüye "zıt yönlerden / karşıt kıyılardan" ulaştığı detayı ve ışığın "bazen / kimi zaman" yön göstermeye yardım ettiği nüansı tamamen kaybolmuştur.
   - *Kök Neden:* Alei v1.1'de "karşıt/zıt" (`pol`), "yön" (`gor`) ve "bazen" (`orai-el`) kavramlarını karşılayan kök veya bileşiklerin eksikliği.

### 2.2 Yapay Zekâ Öz-Güveninin Kalibrasyonsuzluğu
Gemini, anlamın yapısal olarak belirsiz olduğu ve dört temel unsurun düştüğü cümlelerde dahi **%95–99** öz-güven raporlamıştır. Bu oran bilimsel bir başarı metriği değil, LLM modellerinin belirsizliği gizleme eğilimidir. Bu nedenle L5 kapsamında 0–3 puanlık kalibrasyon rubriği geliştirilmiş ve "doğru çekinme/belirsizliği bildirme" en yüksek puan olarak tanımlanmıştır.

### 2.3 Kayıp Kaynaklar Manifestosu
Kayıp K6–K10 kıtaları, orijinal Türkçe şiirin tam metni ve model oturum logları depoda yer almamaktadır; `docs/research/blind-translation-01-pending-manifest.json` dosyasıyla eksik kaynaklar dürüstçe listelenmiş, asla yapay log üretilmemiştir.

---

## 3. Gerçekleştirilen Mühendislik ve Dilbilim Çalışmaları

### 3.1 Tipli AST ve Valans Doğrulama Motoru (`src/alei_language/ast.py` & `valency.py`)
- **`SentenceAST`:** Cümleleri salt yüzeysel dize olarak değil; sözdizimsel rol, fiil çatısı, kip, zaman, görünüş ve mantıksal kutupsallığı içeren tipli bir ara temsile (IR) dönüştürür.
- **Valans Denetimi:** Fiillerin kanonik argüman şemalarını denetler (`sileven` -> fail + nesne; `nesalen` -> fail + nesne). Geçişli bir fiilde nesne düştüğünde bunu ya eksilti (ellipsis) ya da valans uyuşmazlığı olarak açıkça raporlar.
- **Belirsizlik Sınıflandırması:** Ayrıştırma sonuçları `supported`, `ambiguous`, `unsupported`, `contradictory`, `unknown_lexeme` olarak kategorize edilir. Bilinmeyen sözcükler (`Jajaya` gibi) uydurma anlam verilmeden reddedilir.
- **Deneysel Çatı Ayrıştırması:** `mode='experimental'` seçildiğinde, `se` dönüşlü parçacığını, `şe-el` karşıt-ödünleyicisini ve `Aremen!` gibi öznesiz emir yapılarını tanır.

### 3.2 Karara Hazır Gramer RFC'si (`linguistics/grammar/valency-and-scope-rfc.md`)
- 16 sistemik gramer açığı `grammar-gap-register.jsonl` dosyasında belgelenmiştir.
- RFC-2026-001 kapsamında 4 derinlemesine öneri geliştirilmiştir:
  1. Analitik dönüşlü çatı parçacığı `se` (`Vel ne va se nesalen.`)
  2. Eylem köklerine düzenli `-i` sıfat türetimi (`fal` -> `fali` = açık durum)
  3. Karşıt-ödünleyici bileşik `şe-el` (olsa bile / even if)
  4. Öznesiz emir/istek kipi (`Aremen!`, `Ne vürelen!`) ve doğrudan aktarım (`vesen: "..."`).

### 3.3 Disiplinli Sözlük Mühendisliği (100 Kavram ve Aday Kökler)
- `linguistics/lexicon/concept-priority.jsonl`: 10 anlamsal alanda 100 kavram önceliklendirilmiştir.
  - Kategori A (Mevcut kanonik kökler): 50 kavram
  - Kategori B (Mevcut köklerle şeffaf bileşikler): 35 kavram
  - Kategori C (Önerilen aday kökler): 10 kök (`Pol`, `Gor`, `Bav`, `Tem`, `Şul`, `Kan`, `Yan`, `Morv`, `Dal`, `Nur`)
  - Kategori D (Çözülmemiş yapısal açıklar): 5 kavram
- **Fonotaktik ve Çakışma Denetimi:** Önerilen 10 kökün tamamı 28 harfli alfabeye uymakta, 270 mevcut kökle sıfır çakışma üretmekte ve `proposed-lexemes.jsonl` dosyasında kanondan kesin olarak ayrı tutulmaktadır.

### 3.4 Bağımsız Kör Değerlendirme Paketi (v2)
- `evaluations/agent-blind-v2/`:
  - 42 dengeli fixture vakası (`cases.jsonl`).
  - Sızdırmaz, bağımsız altın cevap anahtarı (`gold-answers.jsonl`).
  - Dış API bağımlılığı olmayan sonuç içe aktarıcı (`run_blind_eval.py`).
  - Model kirlenmesini önleyen teknik olmayan kullanıcı test protokolü (`README.md`).

### 3.5 Özgün Edebi ve İletişimsel Külliyat
- Hiçbir cümle 101 kanonik örnekten kopyalanmamıştır (deduplication doğrulanmıştır).
- 30 özgün günlük replik ve tutarlı karakterlerle 8 çok turlu diyalog (`experimental-dialogues.md`).
- 3 farklı anlatıcı sesine sahip özgün düzyazı, 2 orijinal şiir ve anlamsal karşıtlıkları kanıtlayan 12 minimal çift (`experimental-literature.md`).

### 3.6 GitHub Sunumu ve Sayfa Önizlemesi
- `README.md` ve `README.tr.md` CODEX hiyerarşisine göre baştan sona yenilenmiştir.
- `docs/site/index.html` ve `style.css`: Sıfır harici kütüphane bağımlılığı olan, mobil uyumlu, SVG logolu ve istemci taraflı etkileşimli sözlük arayıcısına sahip statik dokümantasyon önizlemesi sunulmuştur.
- `.github/ISSUE_TEMPLATE/grammar-gap.yml` eklenmiştir.

---

## 4. Test Sonuçları ve Kabul Doğrulaması

Projede yer alan tüm testler başarıyla çalıştırılmıştır:
- **L5 Öncesi Temel Test Sayısı:** 39 test (Tamamı BAŞARILI).
- **L5 Sonrası Toplam Test Sayısı:** 58 test (Tamamı BAŞARILI, 0 hata, 0 gerileme).
- **Bütünlük Denetimleri:**
  - `python scripts/derive_data.py --check` -> BAŞARILI (270 kök, 274 leksem, 63 işlev, 101 örnek).
  - `python scripts/derive_v11.py --check` -> BAŞARILI (270 kök, 273 leksem, 3 uyumluluk).
  - `python scripts/validate_skills.py` -> BAŞARILI (7 beceri denetlendi, 0 hata).
  - `python scripts/smoke_examples.py` -> BAŞARILI (101 örnek fonotaktik denetimden geçti).
  - `adsiz_dil_acik_anlam_standardi_v1_0.md` SHA-256 sağlama değeri harfiyen korunmuştur.

---

## 5. Bugünün Alei'si Orijinal Beş Kıtayı Sadık Biçimde İfade Edebilir mi?

**Dürüst Yanıt:**  
Bugünkü **kanonik v1.1.0** Alei standardı ile orijinal 5 kıtayı eksiksiz ve sadık biçimde ifade etmek **mümkün değildir**. 

Çevirmen Ajan A, mevcut kelime haznesiyle yetinmek zorunda kaldığında şu temel anlamları feda etmek zorunda kalmıştır:
1. "Yolun kaybolması" (çatı eksikliği yüzünden geçişli fail rolü verilmiştir).
2. "Kapının açık olması" (eylem ismi edatla yamalanmıştır: `fal ve`).
3. "Geçsen bile dön" (karşıt-ödünleyici yapı bulunmadığı için koşula indirgenmiştir).
4. "Zıt uçlardan köprüye varış" (karşıt yön kökü bulunmadığı için düz varışa dönüşmüştür).
5. "Hiç görmemişti" (deneyimsel bitmişlik kipi bulunmadığı için basit geçmişe indirgenmiştir).
6. "Üçüncü gece" (sıra sayıları tanımlı olmadığı için sıra bilgisi düşmüştür).

**Çözüm:**  
L5 kapsamında geliştirilen ve RFC-2026-001'de sunulan **deneysel araçlar ve önerilen kökler devreye alındığında**, bu beş kıtanın tamamı hiçbir anlam kaybı ve çarpıtma olmaksızın, pürüzsüz ve edebi bir dille ifade edilebilmektedir. Ancak bu kuralların resmî standart haline gelmesi dil sahibinin onayına bağlıdır.

---

## 6. Sıkı Dil Sahibi Karar Paketi (Azami 20 Öncelikli Karar)

Dil sahibinin onayına sunulan, dildeki tıkanıklıkları çözecek 20 öncelikli karar paketi şunlardır:

### Bölüm A: Dilbilgisi ve Çatı Kararları (6 Karar)
1. **D-01 (Dönüşlü/Orta Çatı Parçacığı `se`):** Geçişli fiillerin nesnesini özneye yükselten ve faili gizleyen `se` parçacığının kabulü (`Vel ne va se nesalen`). *Reddedilirse:* Geçişli fiiller nesnesiz kullanıldığında eksiltili veya bozuk kalır; kaybolma eylemi ifade edilemez.
2. **D-02 (Eylem Köklerinden `-i` ile Durum Sıfatı Türetimi):** `fal` (açılma) kökünden `fali` (açık [durum]) sıfatının türetim kuralının resmileştirilmesi. *Reddedilirse:* `fal ve` gibi edatlı calque zorlamaları devam eder; durum ile olay ayrılamaz.
3. **D-03 (Karşıt-Ödünleyici Bağlaç `şe-el`):** "olsa bile / even if" anlamı için `şe` (eğer) ve `el` (dahi) bileşiminin kabulü. *Reddedilirse:* Şiirsel tavsiyeler ve ödünleyici şartlar sıradan koşul cümlelerine indirgenir.
4. **D-04 (Öznesiz Emir ve İstek Yapısı):** Cümle başında kişi zamiri olmadan çıplak fiil tabanının (`Aremen!`, `Ne vürelen!`) emir kipi olarak tanınması. *Reddedilirse:* Diyaloglarda ve edebi metinlerde her emrin başına yapay biçimde `Sai` konulması gerekir.
5. **D-05 (Sıra Sayısı Türetimi):** Sayı köklerinden sıra sayısı (`mora-ri` veya `mora-en` = birinci) türetim kuralının belirlenmesi. *Reddedilirse:* "Üçüncü gece" veya kronolojik sıralamalar dilde ifade edilemez.
6. **D-06 (Deneyimsel Geçmiş Zaman Olumsuzu):** "Daha önce hiç yapmadı / never" anlamı için `ne fa [fiil] orai` yapısının standartlaşması. *Reddedilirse:* Basit geçmiş zaman olumsuzu (`ne da`) ile hayat boyu deneyim olumsuzluğu ayrılamaz.

### Bölüm B: Öncelikli Yeni Aday Kökler (10 Kök)
7. **D-07 (`Pol` - Karşıt / Zıt):** C08 vakasını çözer. Köprüye zıt kıyılardan varış veya karşıt kutuplar için zorunludur.
8. **D-08 (`Gor` - Yön / İstikamet):** C06 vakasını çözer. Yön göstermek veya belirli bir vektöre yönelmek için zorunludur.
9. **D-09 (`Bav` - Şafak / Seher):** Gece (`nivar`) kökünün doğal karşıtı; günlük edebi döngü için temel zaman kökü.
10. **D-10 (`Tem` - An / Lahza):** Süreç (`orai`) kökünden farklı olarak noktasal zaman birimi.
11. **D-11 (`Şul` - Sessizlik / Dinginlik):** Şiirsel tefekkür ve gece tasvirleri için vazgeçilmez duyusal kök.
12. **D-12 (`Kan` - Ezgi / Şarkı):** İnsan sözlü kültürü ve şiir için temel estetik kök.
13. **D-13 (`Yan` - Yanılgı / Hata):** C07 vakasını çözer. Taşa yazılan hatayı adlandırmak için gereklidir.
14. **D-14 (`Morv` - Düğüm / Bağ):** Fiziksel ve mecazi bağlanma, antlaşma ve bağlama eylemleri için kök.
15. **D-15 (`Dal` - Ağaç Dalı):** Bitki taksonomisinde somut çevre öğesi.
16. **D-16 (`Nur` - Işıltı / Parıltı):** Güneş/ışık (`pemar`) kökünden farklı olarak yumuşak parıltı kökü.

### Bölüm C: Öncelikli Bileşik ve Şeffaf İfade Kararları (4 Karar)
17. **D-17 (`orai-el` - Bazen / Kimi Zaman):** Zaman kökü `orai` ve odak edatı `el` birleşimiyle sıklık zarfı oluşturulması.
18. **D-18 (`nasel-nerav` - Coğrafi Harita):** Mekan (`nasel`) ve temsil (`nerav`) bileşimiyle harita teriminin şeffaf olarak tanımlanması.
19. **D-19 (`sül-ves` - Teşekkür / Şükran):** İletişimsel nezaket için "iyi söz" kalıbının selamlama gibi kabulü.
20. **D-20 (`yan-ves` - Özür / Pişmanlık):** İletişimsel onarım için "hata sözü" kalıbının kabulü.

---

## 7. Değişiklik Dosyaları Özeti

| Dosya Yolu | Durum | Açıklama |
|---|---|---|
| `docs/research/blind-translation-01-five-stanza-audit.md` | Yeni | 12 kör çeviri vakasının derinlemesine analizi ve minimal çiftleri. |
| `docs/research/blind-translation-01-pending-manifest.json` | Yeni | Kayıp kıtalar ve model logları için dürüst kaynak manifestosu. |
| `linguistics/grammar/valency-and-scope-rfc.md` | Yeni | Karara hazır RFC-2026-001 (Çatı, durum, şart ve emir önerileri). |
| `linguistics/grammar/grammar-gap-register.jsonl` | Yeni | 16 sistemik gramer açığının makinece okunur sicili. |
| `linguistics/lexicon/concept-priority.jsonl` | Yeni | 100 kavramlık öncelik envanteri (A, B, C, D kategorileri). |
| `linguistics/lexicon/proposed-lexemes.jsonl` | Yeni | 10 yeni aday kökün fonotaktik ve sözlük sicili (kanondan ayrı). |
| `linguistics/semantics/concepts-vnext-proposal.jsonl` | Yeni | Şeffaf anlambilim ontoloji genişletme taslağı. |
| `linguistics/corpus/experimental-dialogues.md` | Yeni | 30 pratik replik ve 8 çok turlu karakterli diyalog. |
| `linguistics/corpus/experimental-literature.md` | Yeni | 3 düzyazı metin, 2 özgün şiir ve 12 minimal çift. |
| `evaluations/agent-blind-v2/` (cases, gold, harness, README) | Yeni | 42 vakalık sızdırmaz bağımsız kör çeviri değerlendirme paketi. |
| `src/alei_language/ast.py` | Yeni | Tipli AST ve cümle ara temsili sınıfları. |
| `src/alei_language/valency.py` | Yeni | Fiil valans çerçeveleri ve çatı doğrulama mantığı. |
| `src/alei_language/grammar.py` | Güncellendi | `parse_alei` tipli ayrıştırıcısı eklendi; eski testler korundu. |
| `src/alei_language/transparent_semantics.py` | Güncellendi | `analyze_semantics` güvenli analiz işlevi eklendi. |
| `src/alei_language/cli.py` | Güncellendi | `parse-ast` komutu eklendi. |
| `tests/test_l5_engineering.py` | Yeni | L5 kabullerini ve kurallarını doğrulayan 19 yeni test. |
| `README.md` & `README.tr.md` | Güncellendi | CODEX standartlarına tam uyumlu, aynalanmış yeni tanıtım metinleri. |
| `docs/site/index.html` & `style.css` | Yeni | Bağımsız, hafif, SVG logolu statik dokümantasyon önizlemesi. |
| `.github/ISSUE_TEMPLATE/grammar-gap.yml` | Yeni | Topluluk için gramer açığı bildirim şablonu. |
| `docs/audits/L5_ENGINEERING_REPORT.md` | Yeni | İşbu nihai mühendislik raporu. |

