# ALEI L6 ÖĞRENİCİ DİLBİLGİSİ KILAVUZU
# (Alei Learner's Generative Grammar Manual)

**Sürüm:** L6.0-Experimental (Alei v1.1.0 Uyumlu)  
**Tarih:** Kasım 2026  
**Hedef Kitle:** İnsan yazarlar, öğrenciler, edebiyatçılar ve dil mühendisleri  
**Temel İlke:** Alei, yapay kod dizgeleri için değil; insan zihninin duygularını, soyut düşüncelerini, ilişkilerini ve edebi tahayyüllerini ifade etmek üzere tasarlanmış, üretken ve öğrenilebilir bir insan dilidir.

---

## 1. Ses, Harf ve Söyleyiş (Phonology & Pronunciation)

Alei alfabesi doğrudan Latin temelli olup, her harf tek bir temel fonemi temsil eder.

### 1.1 Ünlüler (Vowels)
Alei yedi temel ünlüye sahiptir:
* **a** [a]: Açık, arka (*Türkçe "araba"daki a gibi*).
* **e** [e]: Yarı-açık ön ünlü (*Türkçe "ev"deki e gibi*).
* **i** [i]: Kapalı ön ünlü (*Türkçe "iz"deki i gibi*).
* **o** [o]: Yarı-kapalı yuvarlak arka ünlü (*Türkçe "orman"daki o gibi*).
* **u** [u]: Kapalı yuvarlak arka ünlü (*Türkçe "uçak"taki u gibi*).
* **ö** [ø]: Yarı-açık yuvarlak ön ünlü (*Türkçe "göz"deki ö gibi*).
* **ü** [y]: Kapalı yuvarlak ön ünlü (*Türkçe "gün"deki ü gibi*).

> **Ahenk Kuralı:** Alei katı bir ünlü uyumuna zorlanmaz; kök morfolojisi berrak ve ezgiseldir.

### 1.2 Ünsüzler (Consonants)
* Patlamalılar: **p, b, t, d, k, g**
* Sürtünmeliler: **f, v, s, z, ş** (ş = [ʃ])
* Akıcılar / Yarı-ünlüler: **l, r, y, m, n, ŋ** (ŋ = [ŋ], nazal ng)

### 1.3 Vurgu (Stress)
Doğal konuşmada vurgu kural olarak **sondan bir önceki hecededir** (paroksiton). Tek heceli çekim ekleri (örneğin nesne eki `-n`) vurguyu genellikle kaydırmaz.

---

## 2. Şahıs, Varlık ve Zamirler (Pronouns & Core Reference)

Alei zamir sistemi son derece yalın ve düzenlidir.

### 2.1 Yalın (Özne) ve Belirtme (Nesne) Zamirleri

| Şahıs | Yalın (Özne) | Belirtme / Yönelme (Nesne) | Anlamı (TR) | Anlamı (EN) |
|---|---|---|---|---|
| **1. Tekil** | **Mei** | **Mein** | Ben / Beni | I / Me |
| **2. Tekil** | **Sai** | **Sain** | Sen / Seni | You / You |
| **3. Tekil** | **Eli** | **Elin** | O / Onu | He/She/It / Him/Her/It |
| **1. Çoğul** | **Meina** | **Meinan** | Biz / Bizi | We / Us |
| **2. Çoğul** | **Saina** | **Sainan** | Siz / Sizi | You (pl.) / You |
| **3. Çoğul** | **Elina** | **Elinan** | Onlar / Onları | They / Them |

> **Kritik Kural (L5 Düzeltmesi):** Alei'de "Meian" veya "Saian" diye zamir formları **yoktur**. Nesne halleri kesin olarak `Mein` ve `Sain`dir.

### 2.2 İyelik ve Aidiyet (Possession)
İyelik, iyelik edatı **ri** ile kurulur:
* `Mei ri samel` → Benim dostum (Friend of mine)
* `Sai ri nave` → Senin şehrin (Your city)
* `Eli ri tüvan` → Onun kitabı (His/Her book)

### 2.3 Dönüşlülük (Reflexive Co-reference)
Kendine dönük eylemlerde fazladan kafa karıştırıcı parçacık gerekmez. Özne ile uyumlu nesne zamiri doğrudan dönüşlülük bildirir:
* `Mei da miraven mein.` → Kendime yardım ettim. (I helped myself.)
* `Sai du liren sain.` → Kendini görüyorsun / aynaya bakıyorsun. (You see yourself.)
* `Eli da liren elin.` → O kendini gördü. (He saw himself.)

*(Not: `Samel` kelimesi "kendi" değil, "dost/arkadaş" anlamına gelir; dönüşlülük için asla kullanılmaz).*

---

## 3. Cümle İskeleti: Zaman, Görünüş ve Durum (TAM & Sentence Core)

Alei temel sözdizimi **SVO** (Özne - Fiil - Nesne) sırasını izler.

### 3.1 Zaman ve Görünüş Parçacıkları

Eylem kökleri daima mastar/çekimli halde `-en` eki taşır (`falen` = açmak, `dumen` = kapatmak, `pürelen` = gelmek). Eylemin zamanı ve tarzı, yüklem önüne gelen parçacıklarla belirlenir:

| Parçacık | İşlev | Örnek | Anlamı (TR) |
|---|---|---|---|
| *(Eksiz)* | Geniş / Şimdiki Zaman | `Mei miraven sain.` | Sana yardım ederim / ediyorum. |
| **da** | Geçmiş Zaman (Punctual Past) | `Mei da miraven sain.` | Sana yardım ettim. |
| **va** | Gelecek Zaman (Expectation/Future) | `Mei va miraven sain.` | Sana yardım edeceğim. |
| **du** | Süreklilik Görünüşü (Progressive) | `Lüra du falen.` | Kapı açılmakta / açılıyor. |
| **fa** | Tamamlanmışlık (Resultative / Perfect) | `Lüra fa falen.` | Kapı açılmış bulunuyor / açıldı. |
| **ne** | Olumsuzluk (Negation) | `Mei ne da miraven.` | Yardım etmedim. |

### 3.2 Durum ve Sıfat Yüklemleri (Zero-Copula Statives)
Alei'de nitelik bildiren sıfatlar `-i` ile biter (`süli` = iyi, `fali` = açık, `dumi` = kapalı). Ek eylem gerekmeksizin doğrudan yüklem olabilirler:
* `Lüra fali.` → Kapı açıktır. (The door is open - Durum/State).
* `Lüra du falen.` → Kapı açılıyor. (The door is opening - Dinamik Olay/Event).
* `Lüra fa falen.` → Kapı açılmış durumda. (The door is opened - Sonuç/Result).

---

## 4. Eyleyen, Etkilenen ve Alan: Çatı ve İstem (Valency & Voice)

### 4.1 İki Nesneli Eylemler ve Yönelme (`ta`)
Verme (`davelen`), söyleme (`vesen`) gibi eylemlerde nesne doğrudan nesne eki (`-an/-en`) alırken, alıcı / muhatap **ta** edatıyla işaretlenir:
* `Mei da davelen tüvanan sain ta.`  
  *Glos:* Ben [GEÇMİŞ] vermek kitap-[BELİRTME] sen [YÖNELME].  
  *Anlamı:* Kitabı sana verdim. (I gave the book to you.)

### 4.2 Edilgen Çatı (Passive Voice: `-il-`)
Geçişli bir eylemin dış failini kaldırıp etkileneni özne konumuna taşımak için fiil gövdesine düzenli **-il-** eki girer:
* `Lüra da falen tüvanan.` *(Etken: Birisi kitabı açtı)*
* `Tüvan da falilen.` *(Edilgen: Kitap açıldı)*
* `Vel ne va nesalilen.` *(Edilgen: Yol kaybedilmeyecek / yitirilmeyecektir)*

### 4.3 Dönüşlü / Orta Çatı (Middle Voice: `vo`)
Eylem dış bir failden ziyade kendi kendine cereyan ediyorsa analitik **vo** parçacığı kullanılır:
* `Vel ne va vo nesalen.` → Yol (kendi kendine) kaybolmaz.

### 4.4 Başlama ve Değişim (Inchoative: `avelen [Sıfat]`)
Bir duruma girme veya dönüşme, `avelen` (olmak/gelmek) fiili ve sıfatla karşılanır:
* `Lüra da avelen fali.` → Kapı açık hale geldi / açıldı.

---

## 5. Karşılaştırma ve Üstünlük Dereceleri (Comparison)

Karşılaştırma ayrılma edatı **fi** ("-den/-dan") ile yapılır:

### 5.1 Üstünlük Kıyası (Comparative)
* `Eli süli Mei fi.` → O benden daha iyidir. (He is better than me.)
* `Nave dori nave-ri fi.` → Şehir, köyden daha büyüktür.

### 5.2 Pekiştirmeli Kıyas (Intensified Comparative)
* `Eli lavar süli Mei fi.` → O benden çok daha iyidir.

### 5.3 En Üstünlük (Superlative: `sam fi`)
Evrensel nicelik bildiren `sam` (bütün/hepsi) kelimesi ile `fi` birleştiğinde "hepsinden daha" yani "en" anlamı doğar:
* `Eli süli sam fi.` → O en iyisidir (hepsinden daha iyidir).
* `So vel dori sam fi.` → Bu yol en genişidir.

---

## 6. Karmaşık Cümleler, İlgiler ve Şartlar (Complex Syntax)

### 6.1 İlgi Tümceleri (Relative Clauses: `ke`)
Bir ismi niteleyen sıfat cümleciği, ismin hemen ardından **ke** bağlacı getirilerek kurulur:
* `Lera ke da avelen samel ve.`  
  *Anlamı:* Gelen kişi (o kişi ki geldi) bir dosttur. (The person who arrived is a friend.)
* `Tüvan ke Sai da liren süli ve.`  
  *Anlamı:* Okuduğun/gördüğün kitap iyidir.

### 6.2 Koşul Cümleleri (Conditionals: `şe`)
* `Şe Sai avelen, Mei süli.` → Eğer gelirsen, ben iyiyim.

### 6.3 Ödün / Karşıt Koşul (Concessives: `şe-el`)
* `Şe-el Sai vürelen, aremen!` → Korksan bile, düşün! (Even if you fear, think!)
* `Şe-el vel dumi, Mei va pürelen.` → Yol kapalı olsa bile geleceğim.

### 6.4 Karşı-Olgusal / İrrealis Şart (Counterfactuals: `şe da ... da va`)
Geçmişte gerçekleşmemiş fakat gerçekleşseydi ne olacağını anlatan varsayımsal yapı:
* `Şe Sai da avelen, Mei da va miraven sain.`  
  *Anlamı:* Eğer gelmiş olsaydın, sana yardım etmiş olurdum. (If you had come, I would have helped you.)

### 6.5 Nicelik ve Olumsuzluk Kapsamı (Quantifier Scope)
* `Sam lera da avelen.` → Bütün insanlar geldi. (All people arrived.)
* `Ne sam lera da avelen.` → Bütün insanlar gelmedi / Herkes gelmedi. (Not all people arrived - Kısmi olumsuzluk).
* `Ne ena lera da avelen.` → Tek bir insan dahi gelmedi / Hiç kimse gelmedi. (Nobody arrived - Tam olumsuzluk).

---

## 7. Günlük Konuşma Kalıpları (Everyday Dialogues)

### Diyalog 1: Karşılaşma ve Hal Hatır (Meeting a Friend)
* **A:** *Süli dei, samel! Sai süli le?*  
  (İyi günler dostum! İyi misin?)
* **B:** *Süli dei! Mei süli, davelen tevaran sain ta. Sai süli le?*  
  (İyi günler! İyiyim, sana teşekkürlerimi sunarım. Sen nasılsın?)
* **A:** *Mei süli ve nivaren du avelen.*  
  (Ben de iyiyim ve öğrenmeye devam ediyorum.)

### Diyalog 2: Yardım İsteme ve Dayanışma (Asking for Help)
* **A:** *Samel, Sai naelen miraven mein le?*  
  (Dostum, bana yardım edebilir misin?)
* **B:** *Ve! Mei va miraven sain. Miva da avelen?*  
  (Elbette! Sana yardım edeceğim. Ne oldu?)
* **A:** *Vel dumi ve Mei ne liren lüran.*  
  (Yol kapalı ve kapıyı göremiyorum.)
* **B:** *Ne vürelen! Meina va falen lüran.*  
  (Korkma! Kapıyı birlikte açacağız.)

---

## 8. Edebi Anlatı: "Köprü ve Ay" (Vel-kür ve Nüra)

Bu kısa anlatı, Alei'nin edebi ahengini, duygu derinliğini ve L6 sözdizimi kurallarını sergilemektedir.

### Orijinal Metin (Alei)
1. *Mora lo, siril dumi ve nüra selin du liren nave-lo.*  
2. *Eli da şürelen vel-kür lo, ve arem da avelen dori.*  
3. *Şe-el mora dumi, nüra-pemar ne va nesalilen.*  
4. *Eli da vesen sain ta: "Şe Mei da va nesalen velan, samel va pürelen mein ta."*  
5. *Den eli fa dumen liren-lerin, ve vürel da nelaren peme ta.*

### Cümle Cümle Çözümleme ve Anlamı
1. **Mora lo, siril dumi ve nüra selin du liren nave-lo.**  
   *Glos:* Gece [BULUNMA], gökyüzü kapalı ve ay sessiz [GÖRÜNÜŞ-SÜREKLİ] bakmak şehir-[BULUNMA].  
   *TR:* Gece vakti, gök kapalıydı ve ay sessizce şehre bakmaktaydı.  
   *EN:* At night, the sky was closed and the moon looked quietly upon the city.

2. **Eli da şürelen vel-kür lo, ve arem da avelen dori.**  
   *Glos:* O [GEÇMİŞ] durmak yol-köprü [BULUNMA], ve düşünce [GEÇMİŞ] olmak büyük.  
   *TR:* Köprünün üzerinde durdu ve düşünceleri derinleşti (büyüdü).  
   *EN:* He stood upon the bridge, and his thoughts grew profound.

3. **Şe-el mora dumi, nüra-pemar ne va nesalilen.**  
   *Glos:* [ÖDÜN-ŞART] gece kapalı, ay-ışık [OLUMSUZ] [GELECEK] [EDİLGEN]-kaybolmak.  
   *TR:* Gece kapalı (karanlık) olsa bile, ayın ışığı yitip gitmeyecektir.  
   *EN:* Even if the night is overcast, the moonlight will not be lost.

4. **Eli da vesen sain ta: "Şe Mei da va nesalen velan, samel va pürelen mein ta."**  
   *Glos:* O [GEÇMİŞ] söylemek kendi [YÖNELME]: "[ŞART-KARŞI-OLGUSAL] Ben [GEÇMİŞ] [GELECEK] kaybetmek yol-[BELİRTME], dost [GELECEK] gelmek ben [YÖNELME]."  
   *TR:* Kendi kendine fısıldadı: "Yolumu kaybetseydim bile, dostum bana gelirdi."  
   *EN:* He whispered to himself: "Even if I were to lose the way, a friend would come to me."

5. **Den eli fa dumen liren-lerin, ve vürel da nelaren peme ta.**  
   *Glos:* Sonra o [BİTMİŞLİK] kapatmak göz-çoğul-[BELİRTME], ve korku [GEÇMİŞ] dönmek ışık [YÖNELME].  
   *TR:* Sonra gözlerini yumdu ve korku yerini aydınlığa bıraktı (ışığa geri döndü).  
   *EN:* Then he closed his eyes, and fear turned back into light.

---

## 9. Temel Sözcük ve Ek Dizini (L6 Quick Reference)

### Çekim Ekleri ve Edatlar
* **-n / -an / -en:** Belirtme durumu (Accusative).
* **ta:** Yönelme / Alıcı edatı (Dative / Recipient / Goal).
* **lo:** Bulunma edatı (Locative).
* **fi:** Kıyas / Ayrılma edatı (Ablative / Than).
* **ri:** İyelik edatı (Genitive / Possessive).
* **-il-:** Edilgen çatı iç-eki (Passive infix: `falilen`).
* **vo:** Orta çatı parçacığı (Middle particle: `vo nesalen`).
* **ke:** İlgi tümcesi / Tamlayan bağlacı (Relative pronoun / Complementizer).
* **şe:** Şart bağlacı (If).
* **şe-el:** Ödün şart bağlacı (Even if / Concessive).
* **den:** Zaman dizimi (Then / Afterwards).
* **pür:** Sebep-sonuç bağlacı (Therefore / Hence).
* **le:** Soru parçacığı (Sentence-final polar interrogative).
