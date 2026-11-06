# ALEI L5 & L5.1 DİL MÜHENDİSLİĞİ, DİLBİLİMSEL DOĞRULUK VE ANA HAT RAPORU

**Tarih:** 2026-11-06  
**Depo:** `egecagintepe/alei-language`  
**Çalışma Dalı:** `l5/linguistic-engineering-community`  
**Temel Alınan Dal:** `owner/alei-v1.1-pr` (Taslak PR #8, SHA: `4a6a2b0`)  
**Onaylı Resmî Dil Adı:** Alei (AD-2026-001)  
**Onaylı v1.1.0 Yardım Kökü ve Fiili:** Mirav / Miraven (AD-2026-002)  
**v1.0 Değişmezlik Sağlaması (SHA-256):** `265fcc0dd0fcaf4bd23a062d631855463201be4ac12e42bf2501f30628ee8504` (`adsiz_dil_acik_anlam_standardi_v1_0.md`)  
**CI ve Test Durumu:** 64/64 test BAŞARILI, tüm türetim denetimleri ve beceri doğrulayıcıları eksiksiz YEŞİL.

---

## 1. Yönetici Özeti ve Git Durumu Uzlaşması

L5 ve L5.1 geliştirme aşamaları, Alei'yi salt bir yapay zekâ simülasyonu olmaktan çıkarıp edebiyat yazarları, öğrenciler ve günlük konuşurlar için üretken, analiz edilebilir ve tutarlı bir **insan edebi dili** haline getirmek ve ana hatta (`main`) güvenle entegre edilebilecek akademik/mühendislik olgunluğuna ulaştırmak amacıyla yürütülmüştür.

### 1.1 Git Dalları ve Bağımlılık Envanteri (Soykütüğü)
1. `main` (SHA: `17356c8`): Başlangıç standardı ve temel sözlük/gramer araçları. Koruma altında (GH006 kuralı devrede).
2. Taslak PR #7 (`phase-2/linguistic-integrity`, SHA: `8d8aa48`): 101 cümlelik bütünlük denetimi, korumacı sözdizim ayrıştırıcı.
3. Taslak PR #8 (`owner/alei-v1.1-pr`, SHA: `4a6a2b0`): Dil sahibinin AD-2026-001 (Alei adı) ve AD-2026-002 (Mirav/Miraven) kararlarını içeren v1.1.0 katmanı.
4. `l5/linguistic-engineering-community` (SHA: `a8ae062` ve devamı): PR #8'in en güncel uyumlu durumundan türetilmiş; doğrusal commit zincirini koruyan, L5 mühendisliği, L5.1 dilbilimsel denetimi ve akademik araştırma altyapısını içeren konsolide dal.
5. **Yedek Etiketler:** Entegrasyon öncesinde hiçbir yerel commit veya referansın kaybolmaması için geri dönüş sağlama etiketleri oluşturulmuştur:
   - `backup/main-17356c8`
   - `backup/pr7-8d8aa48`
   - `backup/pr8-4a6a2b0`
   - `backup/l5-6670741`
6. **Erişilemeyen Harici Commitler:** Görev tanımında bahsi geçen `d8bc722` (L3) ve `174ee0b` (L4) commitleri mevcut klonda ve uzak depoda yer almamaktadır; harici dizin taramasında bulunamamış ve dürüstçe kurtarılamayan harici çalışmalar olarak kayda geçirilmiştir.

---

## 2. L5.1 Bağımsız Dilbilimsel Doğruluk Denetimi (Linguistic Correctness Gate)

Python testlerinin geçmesi, üretilen sözcüklerin veya çevirilerin kanonik gramere uygun olduğunu tek başına kanıtlamaz. Bu ilkeyle hareket edilerek, L5 kapsamında üretilen RFC, sözlükler, diyaloglar, edebi metinler ve değerlendirme dosyaları `adsiz_dil_acik_anlam_standardi_v1_0.md`, `data/roots.jsonl`, `data/functions.jsonl` ve `data/lexemes.jsonl` kaynaklarına karşı kelime kelime denetlenmiş; **11 kritik dilbilimsel hata ve yanlış atıf** tespit edilerek tamamen düzeltilmiştir:

### 2.1 Tespit Edilen 11 Kritik Dilbilimsel Hata ve Düzeltme Matrisi

| No | İncelenen Unsur | Kanonik Durum ve Gerçek Anlam | L5 Taslağındaki Hatalı İddia | Etkilenen Dosyalar | Karşı Örnek / Kanıt | Yapılan Düzeltme ve Durum |
|---|---|---|---|---|---|---|
| **1** | **`se` parçacığı** | `functions:1080` (§8.6): **Vasıta/Araç edatı** ("araçla/vasıtayla", örn: `tüvan se` = aletle). | "Dilde boşta duran, çakışmasız dönüşlü çatı (middle voice) parçacığı". | RFC-2026-001, `grammar.py`, `valency.py`, testler | `Mei da sileven tüvan se` = Aletle okudum. `se` dönüşlü yapılırsa araç anlamı çöker. | `se`'nin kanonik araç edatı olduğu belgelendi. Dönüşlü çatı için çakışma uyarısı eklendi; alternatif olarak `ro` önerildi. |
| **2** | **`Arem / Aremen`** | `roots:434`: "düşünce, zihinsel değerlendirme"; `lexemes:757`: **"düşünmek"**. Kanonik geri dönüş kökü: `roots:656` `Nelar` -> `Nelaren`. | "Dönmek / geri gelmek" (Return). | Kör çeviri denetimi, diyaloglar, edebi külliyat, valans motoru | `Sai da aremen` kanonik olarak "Düşündün" demektir, "Döndün" değil! | Geri dönme anlamı için `nelaren` getirildi; `aremen` düşünülen bağlamlarda "düşünmek" olarak korundu. |
| **3** | **`Vürel / Vürelen`** | `roots:502`: "korku"; `lexemes:787`: **"korkmak"**. Kanonda "geçmek" (cross) anlamında `vür` kökü yoktur! | "Geçmek / aşmak" (Cross / Pass). | Kör çeviri denetimi, RFC, diyaloglar, edebi külliyat | `Ne vürelen!` kanonik olarak **"Korkma!"** demektir, "Geçme!" değil! | `vürelen` korkmak olarak düzeltildi. "Korkma demediler; korksan bile düşün dediler!" şiirsel dürüstlükle kanona kavuşturuldu. |
| **4** | **`Mora`** | `roots:455`: **"gece"** (night; `Dei` gününün zıttı). Kanonik bir (1) sayısı: `functions:1100` **`Ena`**. | "Bir (1) sayısı / tekil" (`tem mora` = bir an; `mora ena` = bir kişi). | `proposed-lexemes.jsonl`, diyaloglar, edebiyat | `Mora da avelen` = "Gece geldi" demektir, "Bir geldi" değil. | Sayı anlamındaki yerlerde `ena` getirildi; `mora` kesinlikle gece olarak sabitlendi. |
| **5** | **`Dei`** | `roots:454`: **"gün"** (day). Kanonik gök cismi/yıldız: `roots:497` **`Nüra`** / `nüra-pemar`. | "Yıldız" (Star; `dei-pemar` = yıldız ışığı). | Kör çeviri denetimi, diyaloglar, edebiyat, `cases.jsonl` | `Dei lo` = gündüz vakti / gün içinde. | Yıldız anlamı için `nüra` ve şeffaf `nüra-pemar` getirildi; `dei` gün olarak korundu. |
| **6** | **Nesne Zamirleri** | Standart §4.1/§4.2: Ünlüyle biten zamirler nesne durumunda `-n` alır: **`mein`, `sain`, `elin`**. Ünsüzle bitenler `-an` alır (`tüvanan`). | `Meian`, `Saian` gibi uydurma biçimler. | `experimental-dialogues.md`, `cases.jsonl` | Standart §4.2: `Mei saelen sain.` `*Mei saelen Saian` kural dışıdır. | Tüm `Meian` ve `Saian` biçimleri kanonik `mein` ve `sain` ile değiştirildi; ayrıştırıcıya ret kuralı eklendi. |
| **7** | **`Nasel`** | `roots:548`: **"orman"** (forest). Genel mekan kökü: `lem` (barınak/yer) veya bulunma edatı `lo`. | "Genel mekan / yer" (place). | `proposed-lexemes.jsonl`, diyaloglar, edebiyat | `Nasel lo` = ormanda. | Mekan anlamı için `lem lo` getirildi; orman bağlamlarında `nasel` korundu. |
| **8** | **`Nivar / Nivaren`** | `roots:721`: "öğrenme"; `lexemes:921`: **"öğrenmek"**. Kanonik gece: `roots:455` `Mora`. | "Gecelemek / gece beklemek" (Nightwatch). | Kör çeviri denetimi, diyaloglar, edebiyat, kavram öncelikleri | `Mei da nivaren` = "Öğrendim" demektir, "Gece nöbeti tuttum" değil. | Gece bekleme anlamı için `varen mora lo` getirildi; `nivar` öğrenme olarak kanona iade edildi. |
| **9** | **`Silev / Sileven`** | `roots:508`: "okuma eylemi"; `lexemes:793`: **"okumak"**. Üretmek/yapmak kökü: `roots:447` `Jav` -> `Javen`. | "Yapmak / üretmek" (Make/produce, kapı/düğüm yapmak). | `proposed-lexemes.jsonl`, diyaloglar, altın cevaplar | Standart §4.2 ve Cümle 50: `Mei du sileven tüvanan` = "Kitabı okuyorum". | Okuma anlamı `sileven` olarak korundu; yapma/üretme için kanonik `javen` kullanıldı. |
| **10** | **`-ra` eki** | Standart §8.6 (`functions:1078`): Ayrılma (-den/-dan) **`fi`** edatıyla yapılır (`nasel fi` = ormandan). | Uydurma ayrılma durum eki `-ra` (`pol-ra`, `nasel ra`). | `grammar.py`, diyaloglar, edebiyat, aday kökler | Standart §8.6 ayrılmayı edatla tanımlar; Alei'de `-ra` eki yoktur. | Ayrıştırıcıdan `ra` silindi, tüm kullanımlar kanonik `fi` edatına dönüştürüldü (`pol fi`, `lavar vel fi`). |
| **11** | **Aday Kök `Gor`** | `roots:444`: **`Vel`** zaten "yön, yol" anlamındadır. | `Gor` kökünün "dilde yön kavramı olmadığı" iddiasıyla önerilmesi. | `proposed-lexemes.jsonl`, `concept-priority.jsonl` | `roots:444` `Vel` yön vektörünü karşılamaktadır. | `Gor`'un gereksiz çiftleme (duplicate) olduğu RFC'de açıkça belgelendi; kanonik `Vel` önceliklendirildi. |
| **12** | **Öznesiz Emirler** | Standart v1.0 §4.1 açıkça izin verir: *"Kişi zamiri varsayılan olarak söylenir; kısa cevaplarda ve yönü çok açık emirlerde atılabilir."* | Öznesiz emirlerin yeni ve kanon dışı bir dil uzantısı gibi sunulması. | `valency-and-scope-rfc.md`, `grammar.py` | Standart metni §4.1. | Öznesiz emirlerin (`Aremen!`) kanonik v1.0 kuralı olduğu tescillendi; `parse_alei` standart modda destekler hale getirildi. |

---

## 3. İlk Gerçek Bağımsız Kör Çeviri Deneyinin (ChatGPT → Gemini) Derinlemesine Analizi

ChatGPT (Ajan A) ve Gemini (Ajan B) arasında gerçekleşen 5 kıtalık kör çeviri deneyi, dilbilimsel denetimimiz ışığında olağanüstü bir bilimsel gerçeği açığa çıkarmıştır:

### 3.1 Karşılıklı Halüsinasyon Yankılanması (Hallucinatory Echo Chamber)
Ajan A, kanonik sözlüğü çalışma anında dinamik olarak sorgulayamadığı için:
- `vürelen` fiilini "geçmek" (korkmak yerine),
- `aremen` fiilini "dönmek" (düşünmek yerine),
- `nave` sözcüğünü "dokuz" (şehir yerine; dokuz = `vüni`),
- `dei` sözcüğünü "yıldız" (gün yerine; yıldız = `nüra`),
- `nivaren` fiilini "gece nöbeti tutmak" (öğrenmek yerine) zannetmiştir.

Daha da vahimi, Türkçe kaynak metinden tamamen habersiz olan Ajan B (Gemini), bu uydurma sözlük anlamlarını hiçbir sözlük denetimine tabi tutmadan "tahmin etmiş" ve **%98 güvenle** Türkçe geri çevirisinde "geçme", "dön", "dokuz kapı", "yıldız" olarak geri üretmiştir!
Bu bulgu, **salt LLM çıktısına dayalı kör çevirilerin deterministik sözlük ve AST denetimi olmadan birer "karşılıklı halüsinasyon yankılanması" ürettiğini** ispatlamaktadır.

### 3.2 Orijinal 9. Kıtanın Hakiki Kanonik Yorumu
Ajan A'nın ürettiği:
```text
Elina ne da vesen: "Ne vürelen!"
Elina da vesen: "Şe-el Sai vürelen, aremen!"
```
Cümlesi, kanonik Alei sözlüğüne göre kelimesi kelimesine şudur:
$$\mathbf{Onlar\ "Korkma!"\ demediler;\ "Korksan\ bile\ düşün!"\ dediler.}$$
*(They did not say: "Do not fear!" They said: "Even if you fear, think!")*

Bu felsefi derinlik, Ajan A'nın hatalı "geçmek/dönmek" eşleştirmesinden katbekat daha güçlü ve Alei'nin kurucu mantığına daha uygundur.

---

## 4. Akademik Araştırma Altyapısı (Research Foundation)

Alei'nin gelecekte ACL, EMNLP veya CoNLL konferanslarında bağımsız, tekrarlanabilir bir bilimsel yayın haline gelmesi için `research/` dizininde eksiksiz bir araştırma temeli kurulmuştur:

1. **`research/literature-survey.md`:** ConlangCrafter (ACL 2026), COGS, SCAN, EMNLP 2025 MT çalışmaları ve morfolojik kompozisyonellik üzerine 10+ sayfalık kapsamlı literatür taraması.
2. **`research/benchmark-design.md`:** 6 Alei test boyutu:
   - Görülmemiş bileşik sözcük yorumlama (Zero-shot compositional interpretation).
   - Yeni morfolojik kombinasyonlar.
   - Modeller arası çapraz aktarım ve iletişimsel doğruluk.
   - Belirsizlik kalibrasyonu ve çekinme (Disciplined epistemic abstention).
   - Bilgi koruma ve kayıpsız aktarım.
   - İnsan öğrenilebilirliği ve bilişsel yük.
3. **`research/paper-outline.md`:** 9 bölümlük akademik makale iskeleti (uydurma sonuç içermeyen, metodolojiye odaklı).
4. **`research/roadmap.md`:** L5.1'den hakemli yayına uzanan 6 aşamalı araştırma yol haritası.

---

## 5. Güçlendirilmiş Test ve Doğrulama Sonuçları

`tests/test_l5_engineering.py` dosyasına 11 denetim bulgusunun tamamını kapsayan regresyon testleri eklenmiştir:
- **`TestL5LinguisticAuditRegressions`:**
  - `test_canonical_lexical_provenance`: `Arem`, `Nelar`, `Vürel`, `Mora`, `Ena`, `Dei`, `Nüra`, `Nave`, `Vüni`, `Silev`, `Jav`, `Nasel`, `Nivar` köklerinin gerçek anlamlarını kilitler.
  - `test_canonical_postpositions_and_rejected_invented_suffixes`: `se` ve `fi` edatlarını doğrular; uydurma `-ra` ekini reddeder.
  - `test_pronoun_accusative_forms`: `mein`, `sain`, `elin` doğrular; `Meian` / `Saian` girişlerini reddeder.
  - `test_middle_voice_collision_warning`: Deneysel `se` kullanımında kanonik araç edatı çakışma uyarısı fırlatıldığını doğrular.
  - `test_subjectless_imperative_standard_compliance`: `Aremen!` cümlesinin v1.0 standardı §4.1 gereği standart modda da geçerli olduğunu kanıtlar.
- **`TestL5CorpusUniqueness`:** Cümleleri salt JSON satırı olarak değil, normalleştirilmiş metin düzeyinde kelime kelime karşılaştırarak külliyatın %100 özgün olduğunu garanti eder.

### Test Çıktısı:
```text
Ran 64 tests in 3.776s
OK (64 passed, 0 failures, 0 errors)

python scripts/derive_data.py --check -> OK (roots: 270, lexemes: 274, functions: 63, example-sentences: 101)
python scripts/derive_v11.py --check  -> OK (roots: 270, lexemes: 273, compatibility: 3)
python scripts/validate_skills.py     -> OK (7 skills checked; 0 errors)
python scripts/smoke_examples.py      -> OK (101 sentence rows checked; 0 flagged tokens)
```

---

## 6. Güvenli Ana Hat Entegrasyon Planı (Mainline Integration Plan)

`main` dalının GH006 koruma kuralı aktif olduğundan, doğrudan zorla push yapılamaz ve yapılmamalıdır. Entegrasyon şu güvenli sırayla tamamlanmalıdır:

1. **Adım 1:** PR #7 (`phase-2/linguistic-integrity`) `main` dalına squash/rebase olmaksızın merge edilir.
2. **Adım 2:** PR #8 (`owner/alei-v1.1-pr`) güncellenmiş `main` üzerine merge edilir (AD-2026-001 ve AD-2026-002 resmileşir).
3. **Adım 3:** İşbu `l5/linguistic-engineering-community` dalı için GitHub üzerinden PR açılır ve tüm testler yeşil olduğunda `main` dalına merge edilir.
4. **Adım 4:** Entegrasyon tamamlandıktan sonra eski PR dalları silinebilir; ancak oluşturduğumuz `backup/*` etiketleri kalıcı olarak saklanır.

---

## 7. Dil Sahibinin Onayına Sunulan Karar Paketi (Decision Packet)

Dil sahibinin değerlendirmesi ve resmi onayı için hazırlanan karar maddeleri:

1. **Karar AD-2026-003 (Dönüşlü Çatı Parçacığı Seçimi):** `se` parçacığının araç edatıyla (`functions:1080`) çakışması sebebiyle, ya konumsal ayrıştırma kuralı kabul edilecek ya da çakışmasız alternatif bir parçacık (`ro`) seçilecektir.
2. **Karar AD-2026-004 (Eylem Köklerinden Sıfat Türetimi):** `fal` -> `fali` (açık durum) gibi semantik olarak lisanslı eylem köklerine `-i` ekiyle durum sıfatı türetme kuralının kabulü.
3. **Karar AD-2026-005 (Karşıt-Ödünleyici Bağlaç `şe-el`):** "olsa bile / even if" anlamı için şeffaf `şe-el` bileşiğinin kabulü.
4. **Karar AD-2026-006 (Doğrudan Alıntı ve Noktalama Çerçevesi):** `vesen: "..."` iki nokta ve tırnak işaretli doğrudan aktarım yapısının biçimsel kabulü.
5. **Karar AD-2026-007 (Aday Kökler Ön İncelemesi):** `Pol` (karşıt), `Bav` (şafak), `Tem` (an), `Şul` (sessizlik), `Kan` (şarkı), `Yan` (hata), `Morv` (düğüm), `Dal` (dal), `Nur` (parıltı) köklerinin aday statüsünde tutulmaya devam edilmesi (`Gor` kökü kanonik `Vel` ile çiftlendiği için geri çekilebilir).
