# ALEI L5, L5.1 & L5.2 DİL MÜHENDİSLİĞİ, DİLBİLİMSEL DOĞRULUK VE BİLİMSEL DÜRÜSTLÜK RAPORU

**Tarih:** 2026-11-06  
**Depo:** `egecagintepe/alei-language`  
**Çalışma Dalı:** `l5/linguistic-engineering-community`  
**Temel Alınan Dal:** `owner/alei-v1.1-pr` (Taslak PR #8, SHA: `4a6a2b0`)  
**Onaylı Resmî Dil Adı:** Alei (AD-2026-001)  
**Onaylı v1.1.0 Yardım Kökü ve Fiili:** Mirav / Miraven (AD-2026-002)  
**v1.0 Değişmezlik Sağlaması (SHA-256):** `265fcc0dd0fcaf4bd23a062d631855463201be4ac12e42bf2501f30628ee8504` (`adsiz_dil_acik_anlam_standardi_v1_0.md`)  
**CI ve Test Durumu:** 66/66 test BAŞARILI, tüm türetim denetimleri ve beceri doğrulayıcıları eksiksiz YEŞİL.

---

## 1. Yönetici Özeti ve Git Durumu Uzlaşması

L5, L5.1 ve L5.2 geliştirme aşamaları, Alei'yi yapay zekâ simülasyonlarının ötesinde edebiyat yazarları, öğrenciler ve günlük konuşurlar için üretken, analiz edilebilir ve tutarlı bir **insan edebi dili** haline getirmek ve ana hatta (`main`) güvenle entegre edilebilecek akademik/mühendislik olgunluğuna ulaştırmak amacıyla yürütülmüştür.

L5.2 aşamasında temel odak noktamız, **bilimsel dürüstlük (research integrity)** ve **kanonik dilbilimsel gerçeklik** olmuştur. Önceki L5.1 aşamasında kaynak metin elde olmadan yapılan ve modellerin karşılıklı sözlük uydurduğunu varsayan hatalı çıkarımlar, `ALEI_L5_2_KANIT_PAKETI` üzerinden kelime kelime doğrulanarak resmen düzeltilmiş; kanonik sözlükteki kritik boşluklar ve çakışmalar matematiksel ve dilbilimsel kesinlikle belgelenmiştir.

### 1.1 Git Dalları ve Bağımlılık Envanteri (Soykütüğü)
1. `main` (SHA: `17356c8`): Başlangıç standardı ve temel sözlük/gramer araçları. Koruma altında (GH006 kuralı devrede).
2. Taslak PR #7 (`phase-2/linguistic-integrity`, SHA: `8d8aa48`): 101 cümlelik bütünlük denetimi, korumacı sözdizim ayrıştırıcı.
3. Taslak PR #8 (`owner/alei-v1.1-pr`, SHA: `4a6a2b0`): Dil sahibinin AD-2026-001 (Alei adı) ve AD-2026-002 (Mirav/Miraven) kararlarını içeren v1.1.0 katmanı.
4. `l5/linguistic-engineering-community`: PR #8'in en güncel durumundan türetilmiş; L5 mühendisliğini, L5.1 dilbilimsel denetimini ve L5.2 bilimsel dürüstlük düzeltmelerini içeren konsolide ana hat aday dalı.
5. **Yedek Etiketler:** Entegrasyon öncesinde hiçbir yerel commit veya referansın kaybolmaması için geri dönüş sağlama etiketleri oluşturulmuştur:
   - `backup/main-17356c8`
   - `backup/pr7-8d8aa48`
   - `backup/pr8-4a6a2b0`
   - `backup/l5-6670741`
6. **Erişilemeyen Harici Commitler:** Görev tanımında bahsi geçen `d8bc722` (L3) ve `174ee0b` (L4) commitleri mevcut klonda ve uzak depoda yer almamaktadır; harici dizin taramasında bulunamamış ve dürüstçe kurtarılamayan harici çalışmalar olarak kayda geçirilmiştir.

---

## 2. L5.2 Bilimsel Dürüstlük: Pilot Kör Çeviri Deneyinin Hakiki Rekonstrüksiyonu

`ALEI_L5_2_KANIT_PAKETI` (Orijinal Türkçe kaynak metin, ChatGPT'nin Alei çıktıları ve Gemini'nin Türkçe geri çevirileri) doğrultusunda, Pilot Deney 01 baştan sona yeniden incelenmiştir.

### 2.1 L5.1 Raporundaki Hatalı İddiaların Geri Çekilmesi (Formal Retractions)
Önceki raporda orijinal Türkçe kaynak metin incelenemediği için yapılan hatalı iddialar resmen tekzip edilmiş ve geri çekilmiştir:

1. **K1 ("Şehrin Yedi Kapısı") Tekzibi:**
   - *Önceki Hatalı İddia:* Rapor, ChatGPT'nin `Nave` (şehir) kelimesini 9 sandığını ("dokuz kapı"), Gemini'nin de bunu "dokuz kapı" olarak yankıladığını iddia etmişti.
   - *Hakiki Ampirik Gerçek:* Orijinal Türkçe kaynak *"Şehrin yedi kapısından yalnız üçü açıktı"* şeklindedir. ChatGPT `Nave ri növi lürana. Teli lüra fal ve.` yazmıştır (`Nave` = şehir, `növi` = 7, `teli` = 3). Gemini bunu *"Şehrin yedi kapısı. Üç kapı açık."* olarak geri çevirmiştir. İki model de "dokuz kapı" uydurmamıştır; `Nave` kökünü doğru bilmişlerdir.
2. **K4 ("Korkma ve Düşün") Tekzibi:**
   - *Önceki Hatalı İddia:* Rapor, ChatGPT'nin `vürelen` fiilini "geçmek" ve `aremen` fiilini "dönmek" sandığını, Gemini'nin de bunu "geçme" ve "dön" olarak çevirdiğini iddia etmişti.
   - *Hakiki Ampirik Gerçek:* Orijinal Türkçe kaynak *"Bize 'Korkma,' demediler; 'Korksan da düşün,' dediler."* şeklindedir. ChatGPT `Elina ne da vesen: "Ne vürelen!" Elina da vesen: "Şe Sai vürelen, aremen!"` kodlamıştır. Gemini bunu *"Onlar 'Korkma!' demedi. Onlar 'Eğer korkarsan, düşün!' dedi."* olarak çevirmiştir. Her iki model de `vürelen` kökünü "korkmak" ve `aremen` kökünü "düşünmek" olarak doğru anlamıştır.
3. **K4.2 ("Öğrenmek") Tekzibi:**
   - *Önceki Hatalı İddia:* `Meina da nivaren` ifadesinin "gece nöbeti tutmak" olarak çevrildiği iddia edilmişti.
   - *Hakiki Ampirik Gerçek:* Orijinal Türkçe kaynak *"Cesaretin, korkunun yokluğu olmadığını öğrendik."* cümlesidir. ChatGPT `Meina da nivaren.` üretmiş, Gemini bunu *"Biz öğrendik."* olarak çevirmiştir (`nivaren` = öğrenmek). Geceleme veya nöbet iddiası asılsızdır.
4. **"Karşılıklı Halüsinasyon Yankılanması" Teorisinin Reddi:**
   - Modeller kanonik sözlük köklerinde (`Nave`, `vürelen`, `aremen`, `nivaren`) karşılıklı halüsinasyon veya uydurma anlam yankılanması yaşamamıştır; mevcut kelimeleri doğru tanımışlardır.

### 2.2 Pilot Deneyde Gözlemlenen Hakiki Yapısal Kusurlar
Sözlük kökleri doğru tanınmış olsa da deney şu kritik yapısal sorunları somut olarak ortaya koymuştur:

1. **Ağır Encoder Bilgi Budaması (Information Omission):**
   Alei v1.1'deki sözcük kısıtları sebebiyle Encoder (ChatGPT), aktaramadığı kavramları çevresel olarak açıklamak yerine tümce ve sıfatları tamamen metinden atmıştır:
   - K1.3'te nesne ("yıldızları saymadım; sönmüş olanı") tamamen atılmış (`Mei ne da belemen. Mei da hüvaren.`), Decoder nesnesiz bırakılmıştır.
   - K1.4'te dört temel öge ("kaybolan", "bazen", "yön", "göstermek") atılmıştır.
   - K5.4'te *"Bir harita doğruydu, fakat yanlış bir yeri gösteriyordu"* önermesi `Ena nerav.` (Bir model) düzeyine indirgenerek ana karşıt yan tümce ve doğruluk koşulu atılmıştır.
2. **Kanonik Köklerin Bağlam Dışı Genişletilmesi:**
   Sözlükte bulamadığı kavramlar karşısında ChatGPT, mevcut kanonik kökleri aşırı genişleterek kullanmıştır:
   - K4'te `Miŋ` (roots:448, "ses titreşimi" / sound vibration): Uydurma değil kanoniktir; ancak fiziksel titreşimden iç insan sesine genişletilmiştir (`Sira miŋ ne Meina ri miŋ.`).
   - K5'te `Dumen` (roots:517 `Dum`, lexemes:797 "kapatmak" / to close): Uydurma değil kanoniktir; ancak cihaz/kapı kapatma eylemi lamba söndürme için kullanılmıştır (`Şe Sai dumen...`).
3. **Gramer ve Valans Uyuşmazlığı:**
   - K5.1'de `vel ne va nesalen` ifadesinde geçişli fiil olan `nesalen` nesnesiz ve yönsüz bırakılmış, Gemini yolun mu kaybolduğu yoksa bir şeyi mi kaybettiği konusundaki ikilemi doğru tespit etmiştir (*"yol kaybolmayacak (kaybetmeyecek)"*).
   - K4.1'de "Korksan da" ödünleyici yapısı (concessive) `şe` şart edatına indirgenmiş ve Gemini tarafından "Eğer korkarsan" olarak anlaşılmıştır.
4. **Encoder ve Decoder Sorumluluklarının Ayrıştırılması:**
   - Gemini (Ajan B), Türkçe kaynak metinden tamamen habersiz olup sadece Ajan A'nın Alei çıktısını almıştır.
   - Gemini'nin yüzeydeki Alei metnini çözme başarısı yüksektir (`Meina da nivaren.` -> "Biz öğrendik").
   - Ajan A'nın kaynak metinden attığı bilgileri (örn. yıldızlar, haritanın doğruluğu) Gemini'nin bilmesi beklenemez; dolayısıyla Gemini'nin öznel güven skoru, görmediği kaynak metin üzerinden kusurlu olarak nitelendirilemez.

### 2.3 Metodolojik Sınırlılık Notu
Bu çalışma, çok merkezli, istatistiksel genelleme iddiası taşıyan bir bilimsel makale deneyi değil; sistemin eksiklerini gösteren **tekil bir pilot denemedir (single pilot trial)**. Gelecek akademik yayınlar bu sınır gözetilerek kurgulanmalıdır. Ayrıca orijinal Türkçe altın kaynak (`01_SOURCE_ORIGINAL_TURKISH.md`), test güvenliği ve telif gereği git deposu dışında güvenli yerel alanda tutulmuştur.

---

## 3. L5.1 & L5.2 Dilbilimsel Hata Düzeltme ve Sözlük Denetimi Matrisi

| No | İncelenen Unsur | Kanonik Durum ve Gerçek Anlam | Hatalı İddia / Önceki Durum | Etkilenen Alanlar | Yapılan Düzeltme ve Bilimsel Durum |
|---|---|---|---|---|---|
| **1** | **`se` parçacığı** | `functions:1080` (§8.6): **Vasıta/Araç edatı** ("araçla/vasıtayla"). | "Boşta duran dönüşlü çatı (middle voice) parçacığı". | RFC, `grammar.py`, `valency.py`, testler | `se`'nin kanonik araç edatı olduğu belgelendi. Dönüşlü çatı için çakışma uyarısı eklendi. |
| **2** | **`Arem / Aremen`** | `roots:434`: "düşünce"; `lexemes:757`: **"düşünmek"**. Geri dönüş: `roots:656` `Nelar`. | "Dönmek / geri gelmek". | Edebiyat, diyaloglar, testler | Kanonik anlam "düşünmek" olarak sabitlendi. |
| **3** | **`Vürel / Vürelen`** | `roots:502`: "korku"; `lexemes:787`: **"korkmak"**. | "Geçmek / aşmak". | Edebiyat, diyaloglar, RFC | Kanonik anlam "korkmak" olarak sabitlendi. |
| **4** | **`Mora`** | `roots:455`: **"gece"** (night). Bir (1) sayısı: `functions:1100` **`Ena`**. | "Bir sayısı / tekil an". | Edebiyat, diyaloglar, sözlük | Gece anlamı korundu; sayı için `ena` getirildi. |
| **5** | **`Dei`** | `roots:454`: **"gün"** (day). | "Yıldız" (Star). | Edebiyat, diyaloglar, testler | Kanonik anlam gün olarak sabitlendi. |
| **6** | **`Nüra`, `Siril` ve Yıldız Boşluğu** | `roots:497`: **"ay, gök cismi"** (moon). `roots:549` `Siril`: **"gökyüzü"** (sky). Kanonda yıldız kökü **YOKTUR**. | "Nüra yıldızdır" veya "Siril yıldız parıltısıdır" iddiaları. | `concept-priority.jsonl`, `proposed-lexemes.jsonl`, testler | `Nüra` "ay", `Siril` "gökyüzü" olarak sabitlendi. Yıldız kavramı **`GAP-LEX-STAR`** olarak tescillendi; `siril-pemar` (gök ışığı) betimsel bileşiktir. |
| **7** | **`ro` ve Şeffaf Semantik Katmanı** | Standart §5.4 (`data/semantic-roles.json`): `ro` kökü zaten **`source_from`** rolüdür. | Dönüşlü çatı için `ro` parçacığının önerilmesi. | RFC, sözlük, semantik katmanı | `ro`'nun anlamsal rolde kullanıldığı belgelendi; çatı için çakışmasız 4 strateji matrisi hazırlandı. |
| **8** | **`Samel` Reddi** | `roots:471`: **"dost, arkadaş"** (friend). | "Aynı / kendi (self/same)" iddiası ve dönüşlü yapı önerisi. | RFC, edebiyat, diyaloglar, sözlük | `samel`'in arkadaş olduğu sabitlendi. Dönüşlü ve özdeşlik kullanımları tamamen iptal edildi. |
| **9** | **Nesne Zamirleri** | Standart §4.1/§4.2: Ünlüyle biten zamirler nesnede `-n` alır: **`mein`, `sain`, `elin`**. | `Meian`, `Saian` formları. | README, README.tr, site, diyaloglar | README dosyalarındaki ve belgelerdeki tüm `Meian`/`Saian` kullanımları `mein`/`sain` olarak düzeltildi. |
| **10** | **`Nasel`** | `roots:548`: **"orman"** (forest). Mekan: `lem`. | "Genel mekan / yer". | Edebiyat, diyaloglar, sözlük | Mekan için `lem lo` getirildi; `nasel` orman olarak korundu. |
| **11** | **`Nemi` ve Su** | `roots:438`: **"su"** (water). | Kanon dışı `sel` sözcüğü. | Edebiyat, diyaloglar, sözlük | Su kavramı kanonik `nemi` köküne iade edildi. |
| **12** | **`Nivar / Nivaren`** | `roots:721`: "öğrenme"; `lexemes:921`: **"öğrenmek"**. | "Gece beklemek / gecelemek". | Edebiyat, diyaloglar | Öğrenmek anlamı sabitlendi. |
| **13** | **`Silev / Sileven`** | `roots:508`: "okuma"; `lexemes:793`: **"okumak"**. Yapmak: `roots:447` `Jav`. | "Yapmak / kapı/düğüm üretmek". | Altın cevaplar, diyaloglar, sözlük | Okuma anlamı korundu; yapma için `javen` kullanıldı. |
| **14** | **`-ra` Durum Eki** | Standart §8.6: Ayrılma hali edatla yapılır (**`fi`** edatı). | `-ra` uydurma durum eki. | Gramer motoru, edebiyat | `-ra` kaldırıldı; kanonik `fi` getirildi. |
| **15** | **`fal -> fali` Türetimi** | `-i` durum sıfatı eki sadece fiziksel durum / konfigürasyon köklerine uygulanabilir. | Bilişsel/süreç köklerine kontrolsüz statif sıfat türetme. | RFC, sözdizim motoru | Semantik sınır kuralı getirildi: Yalnızca fiziksel konfigürasyon kökleri durum sıfatı lisanslar. |

---

## 4. Çatı Kategorileri ve 4 Stratejili Değerlendirme Matrisi (Voice Strategies Matrix)

Gramer mimarisinde üç temel işlev kesin olarak ayrıştırılmıştır:
1. **Orta/Edilgen (Middle/Passive):** Nesne/Tema özneye yükseltilir, fail geri plana itilir (`lüra da falen` = kapı açıldı).
2. **Dönüşlü (Reflexive):** Fail ile nesne özdeştir (`Mei miraven mein`).
3. **Kendi Kendine Oluş (Inchoative/Decausative):** Dış etki olmaksızın durum değişimi (`fali avelen` = açık hale gelmek).

Kanonik `se` (vasıta edatı), semantik roldeki `ro` (`source_from`) ve `samel` (dost/arkadaş) durumları ışığında 4 strateji değerlendirilmiştir:

1. **Strateji A (Ayrık Analitik Parçacık, örn. `vo`):**
   - *Tanım:* Fiilden önce bağımsız bir parçacık (`Vel ne va vo nesalen`).
   - *Değerlendirme:* Öğrenilebilirliği çok yüksek, v1.0 kökleriyle uyumlu, fonolojisi temiz. Ancak yeni bir fonksiyonel morfem gerektirir (Unadopted RFC Adayı).
2. **Strateji B (Bağlı Morfolojik Ek, örn. `-il-`):**
   - *Tanım:* Kök ile mastar arasına ekleme (`nes-il-en`).
   - *Değerlendirme:* Ayrıştırması deterministik, çakışma riski sıfır. Ancak v1.0 kök yapısına ekleme gerektirir (Unadopted RFC Adayı).
3. **Strateji C (Açık Çevresel / İki Fiilli Yapı):**
   - *Tanım:* Durumu kanonik yardımcı eylemler veya sıfatlarla ifade etme (`fali avelen`).
   - *Değerlendirme:* %100 kanonikle ifade edilir; sıfır dilbilgisi müdahalesi gerektirir.
4. **Strateji D (Bağlamsal / Sıfır Morfem Alternasyonu):**
   - *Tanım:* Cansız öznede geçişli fiilin bağlamdan dönüşlü/orta çatılı yorumlanması.
   - *Değerlendirme:* Sıfır yeni kural; ancak yüksek belirsizlik riski taşır.

*Hiçbir çatı eki veya parçacığı otomatik benimsenmemiştir; hepsi dil sahibinin onayına sunulmuştur.*
   - *Tanım:* Nesne almayan geçişli fiilin bağlamdan dönüşlü/orta çatılı yorumlanması.
   - *Değerlendirme:* Sıfır yeni kural. Ancak yüksek belirsizlik ve model tereddüdü yaratır.

*Dil sahibinin kararına kadar hiçbir strateji kanonlaştırılmamış, RFC seviyesinde tutulmuştur.*

---

## 5. Güçlendirilmiş Test ve Doğrulama Sonuçları

`tests/test_l5_engineering.py` ve tüm test takımı baştan sona çalıştırılmış ve tam başarı elde edilmiştir:

```text
Ran 66 tests in 3.812s
OK (66 passed, 0 failures, 0 errors)

python scripts/derive_data.py --check -> OK (roots: 270, lexemes: 274, functions: 63, example-sentences: 101)
python scripts/derive_v11.py --check  -> OK (roots: 270, lexemes: 273, compatibility: 3)
python scripts/validate_skills.py     -> OK (7 skills checked; 0 errors)
python scripts/smoke_examples.py      -> OK (101 sentence rows checked; 0 flagged tokens)
```

Tüm testler:
- `test_canonical_moon_vs_star_lexical_gap`: `Nüra`'nın ay olduğunu ve dilde yıldız kökü bulunmadığını kilitler.
- `test_transparent_semantics_role_ro_collision`: `ro`'nun semantik rol katmanında `source_from` olduğunu belgeler.
- `test_actual_pilot_evidence_consistency`: Orijinal K1 (7 kapı) ve K4 (korkmak ve düşünmek) ampirik gerçekliğini doğrular.

---

## 6. Güvenli Ana Hat Entegrasyon Planı (Mainline Integration Plan)

`main` dalının GH006 koruma kuralı aktif olduğundan, doğrudan zorla push yapılamaz. Entegrasyon şu adımlarla tamamlanacaktır:

1. **Adım 1:** PR #7 (`phase-2/linguistic-integrity`) `main` dalına merge edilir.
2. **Adım 2:** PR #8 (`owner/alei-v1.1-pr`) güncellenmiş `main` üzerine merge edilir (AD-2026-001 Alei adı ve AD-2026-002 Mirav/Miraven resmileşir).
3. **Adım 3:** İşbu `l5/linguistic-engineering-community` dalı için GitHub üzerinden PR açılır ve tüm testler yeşil olduğunda `main` dalına merge edilir.
4. **Adım 4:** Entegrasyon tamamlandıktan sonra eski PR dalları güvenle silinebilir; `backup/*` etiketleri kalıcı güvence olarak saklanır.

---

## 7. Dil Sahibinin Onayına Sunulan Güncellenmiş Karar Paketi

1. **Karar AD-2026-003 (Dönüşlü Çatı Stratejisi):** `se` ve `ro` çakışmaları ışığında 4 stratejiden birinin (Analitik `vo`, Ek `-il-`, Çevresel `samel`, Bağlamsal) resmi olarak seçilmesi.
2. **Karar AD-2026-004 (Eylem Köklerinden Sıfat Türetimi):** `fal` -> `fali` gibi yalnızca fiziksel konfigürasyon köklerine `-i` ile durum sıfatı türetme kuralının onayı.
3. **Karar AD-2026-005 (Karşıt-Ödünleyici Bağlaç `şe-el`):** "olsa bile / even if" anlamı için şeffaf `şe-el` bağlacının kabulü.
4. **Karar AD-2026-006 (Doğrudan Alıntı Çerçevesi):** `vesen: "..."` iki nokta ve tırnak işaretli doğrudan aktarım yapısının biçimsel kabulü.
5. **Karar AD-2026-007 (Aday Kökler Ön İncelemesi):** Mükerrer `Gor` adayının geri çekilmesi; `Pol`, `Bav`, `Tem`, `Şul`, `Kan`, `Yan`, `Morv`, `Dal`, `Nur` köklerinin aday statüsünde tutulması.
6. **Karar AD-2026-008 (`GAP-LEX-STAR` Sözlük Açığı Çözümü):** Dilde yıldız kökü bulunmadığının resmi tescili; yeni kök teklifi (`Siril` vb.) veya şeffaf bileşik yapısının karara bağlanması.
