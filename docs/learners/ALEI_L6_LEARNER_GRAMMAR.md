# ALEI L6.1 ÖĞRENİCİ DİLBİLGİSİ KILAVUZU
# (Alei Learner's Generative Grammar Manual)

**Sürüm:** L6.1-Corrected (Alei v1.1.0 Uyumlu)  
**Tarih:** Kasım 2026  
**Hedef Kitle:** İnsan yazarlar, öğrenciler, edebiyatçılar ve dilbilimciler  
**Temel İlke:** Alei; mekanik kod formülleri için değil, insan zihninin duygularını, soyut düşüncelerini, karşılıklı ilişkilerini ve edebi tahayyüllerini ifade etmek üzere tasarlanmış, üretken, berrak ve öğrenilebilir bir insan dilidir.

---

## 1. Ses, Harf ve Söyleyiş (Phonology & Pronunciation)

Alei alfabesi 28 harften oluşur. Her harf tek bir temel fonemi temsil eder.

### 1.1 Ünlüler (8 Vowels)
Alei sekiz ünlüye sahiptir (`VOWELS = set('aeıioöuü')`):
* **a** [a]: Açık, arka (*Türkçe "araba"daki a gibi*).
* **e** [e]: Yarı-açık ön (*Türkçe "ev"deki e gibi*).
* **ı** [ɯ]: Kapalı arka düz (*Türkçe "ılık"taki ı gibi*).
* **i** [i]: Kapalı ön düz (*Türkçe "iz"deki i gibi*).
* **o** [o]: Yarı-kapalı yuvarlak arka (*Türkçe "orman"daki o gibi*).
* **ö** [ø]: Yarı-açık yuvarlak ön (*Türkçe "göz"deki ö gibi*).
* **u** [u]: Kapalı yuvarlak arka (*Türkçe "uçak"taki u gibi*).
* **ü** [y]: Kapalı yuvarlak ön (*Türkçe "gün"deki ü gibi*).

### 1.2 Ünsüzler (20 Consonants)
`CONSONANTS = set('bdfghjklmnñŋprsştvyz')`
* Patlamalılar: **p, b, t, d, k, g**
* Sürtünmeliler: **f, v, s, z, ş** (ş = [ʃ])
* Akıcılar ve Yarı-ünlüler: **l, r, y, m, n, ñ, ŋ** (ŋ = [ŋ], nazal ng)

### 1.3 Vurgu (Stress)
Doğal konuşmada vurgu kural olarak **sondan bir önceki hecededir** (paroksiton).

---

## 2. Şahıs, Varlık ve Zamirler (Pronouns & Core Reference)

### 2.1 Yalın (Özne) ve Belirtme (Nesne) Zamirleri

| Şahıs | Yalın (Özne) | Belirtme / Yönelme (Nesne) | Anlamı (TR) | Anlamı (EN) |
|---|---|---|---|---|
| **1. Tekil** | **Mei** | **Mein** | Ben / Beni | I / Me |
| **2. Tekil** | **Sai** | **Sain** | Sen / Seni | You / You |
| **3. Tekil** | **Eli** | **Elin** | O / Onu | He/She/It / Him/Her/It |
| **1. Çoğul** | **Meina** | **Meinan** | Biz / Bizi | We / Us |
| **2. Çoğul** | **Saina** | **Sainan** | Siz / Sizi | You (pl.) / You |
| **3. Çoğul** | **Elina** | **Elinan** | Onlar / Onları | They / Them |

> **Kritik Kural:** Alei'de "Meian" veya "Saian" diye biçimler **kesinlikle yoktur**. Nesne halleri kesin olarak `Mein` ve `Sain`dir.

### 2.2 İyelik ve Aidiyet (Possession)
İyelik, iyelik edatı **ri** ile kurulur:
* `Mei ri lem` → Benim evim (My home)
* `Sai ri lem` → Senin evin (Your home)
* `Eli ri tüvan` → Onun kitabı (His/Her book)

### 2.3 Dönüşlülük (Reflexive Co-reference)
Kendine dönük eylemlerde fazladan yapay parçacık gerekmez. Özne ile uyumlu nesne zamiri doğrudan dönüşlülük bildirir:
* `Mei da miraven mein.` → Kendime yardım ettim. (I helped myself.)
* `Sai du liren sain.` → Kendini görüyorsun / aynaya bakıyorsun. (You see yourself.)
* `Eli da liren elin.` → O kendini gördü. (He saw himself.)

*(Önemli Not: `Samel` kelimesi "kendi" değil, **"dost / arkadaş"** anlamına gelir; dönüşlülük için asla kullanılmaz).*

---

## 3. Cümle İskeleti: Zaman, Görünüş ve Durum (TAM & Sentence Core)

Alei temel sözdizimi **SVO** (Özne - Fiil - Nesne) sırasını izler.

### 3.1 Zaman ve Görünüş Parçacıkları

| Parçacık | İşlev | Örnek | Anlamı (TR) |
|---|---|---|---|
| *(Eksiz)* | Geniş / Şimdiki Zaman | `Mei miraven sain.` | Sana yardım ederim / ediyorum. |
| **da** | Geçmiş Zaman (Past) | `Mei da miraven sain.` | Sana yardım ettim. |
| **va** | Gelecek Zaman (Future) | `Mei va miraven sain.` | Sana yardım edeceğim. |
| **du** | Süreklilik Görünüşü (Progressive) | `Lüra du falen.` | Kapı açılıyor / açılmakta. |
| **fa** | Tamamlanmışlık (Resultative / Perfect) | `Lüra fa falen.` | Kapı açılmış bulunuyor / açıldı. |
| **ne** | Olumsuzluk (Negation) | `Mei ne da miraven.` | Yardım etmedim. |

### 3.2 Durum ve Sıfat Yüklemleri (Zero-Copula Statives)
Nitelik bildiren sıfatlar `-i` eki ile biter (`süli` = iyi, `fali` = açık, `dumi` = kapalı, `lavari` = büyük). Ek eyleme ihtiyaç duymadan doğrudan yüklem olurlar:
* `Lüra fali.` → Kapı açıktır. (State / Durum).
* `Lüra du falen.` → Kapı açılıyor. (Dynamic Event / Olay).
* `Lüra fa falen.` → Kapı açılmış durumda. (Resultative / Sonuç).

---

## 4. Eyleyen, Etkilenen ve Alan: Çatı ve İstem (Valency & Voice)

### 4.1 İki Nesneli Eylemler ve Yönelme (`ta`)
Verme (`davelen`), söyleme (`vesen`) gibi eylemlerde nesne doğrudan nesne eki (`-an/-n`) alırken, muhatap / alıcı **ta** edatıyla işaretlenir:
* `Mei da davelen tüvanan sain ta.`  
  *Anlamı:* Kitabı sana verdim. (I gave the book to you.)

### 4.2 Edilgen Çatı (Passive Voice: `-il-`)
Geçişli bir eylemin dış failini kaldırıp etkileneni (Patient) özne konumuna taşımak için fiil gövdesine düzenli **-il-** eki girer:
* `Lüra da falen tüvanan.` *(Etken: Birisi kitabı açtı)*
* `Tüvan da falilen.` *(Edilgen: Kitap açıldı)*
* `Vel ne va nesalilen.` *(Edilgen: Yol kaybedilmeyecektir)*

*(Not: `-il-` iç-eki yalnızca geçişli eylemlere uygulanabilir; `şürelen` gibi geçişsiz eylemlere uygulanamaz).*

### 4.3 Orta Çatı (Middle Voice: `vo`)
Eylem dış bir failden ziyade kendi kendine, spontane cereyan ediyorsa analitik **vo** parçacığı kullanılır:
* `Vel ne va vo nesalen.` → Yol (kendi kendine) kaybolmaz.

### 4.4 Başlama ve Değişim (Inchoative: `avelen [Sıfat]`)
Bir duruma girme veya dönüşme, `avelen` fiili ve sıfatla karşılanır. Burada özne eyleyen değil, dönüşüme uğrayan Temadır (Theme):
* `Lüra da avelen fali.` → Kapı açık hale geldi / açıldı. (The door became open).

---

## 5. Karşılaştırma Sistemi: Kanonik `peli ... nera`

Alei standardında karşılaştırma sistemi **peli** ("daha") ve **nera** ("-den kıyasla") ile kurulur (§4.9 & §8.6).

> **Kritik Kural:** Son-edat **fi**, ayrılma edatıdır ("-den/-dan", çıkma hâli). Kıyas için kullanılamaz. Kıyas daima `peli ... nera` ile yapılır!

### 5.1 Tam Karşılaştırma (Full Comparative)
* `Eli peli süli Mei nera.` → O benden daha iyidir. (He is better compared with me.)
* `Mei ri lem peli lavari Sai ri lem nera.` → Benim evim seninkinden daha büyüktür. (Standart §4.9 kanıt cümlesi).

### 5.2 Kısa Karşılaştırma (Short Comparative)
* `Eli peli süli.` → O daha iyidir.
* `Eli ri lem peli lavari.` → Onun evi daha büyüktür. (Standart Örnek 44).

---

## 6. Bağlaçlar, İlgiler ve Karmaşık Tümceler (Complex Syntax)

### 6.1 Kanonik Bağlaçlar
* **ya:** "ve" (Katkı bağlacı / Additive conjunction). Cümleleri bağlamak için **ya** kullanılır!
  * `Mei da lümalen lüran ya Sai da falen elin.` → Ben kapıyı onardım ve sen onu açtın.
* **ve:** Son-edat! Sadece **"ile / beraber"** (comitative) anlamına gelir; asla cümle bağlacı ("ve") olarak kullanılamaz!
  * `Mei avelen Sai ve.` → Seninle (beraber) gidiyorum.
* **lia:** "ama / fakat" (Adversative conjunction).
* **sira:** "çünkü" (Causal conjunction).
* **şe:** "eğer" (Conditional conjunction).

### 6.2 İlgi Tümceleri (`ke` Disambiguation)
Alei'de `ke` üç farklı yapıda kullanılır:
1. **Tümleç Cümlesi (Verb Complement):** Bilişsel/iletişim eylemlerinden sonra:
   * `Eli da vesen ke tüvan süli.` → Kitabın iyi olduğunu söyledi.
2. **Özne İlgi Tümcesi (Subject Relative):** İsmin ardından doğrudan eylem gelir:
   * `Lera ke sileven tüvanan da avelen.` → Kitabı okuyan kişi geldi.
3. **Nesne İlgi Tümcesi (Object Relative):** İsmin ardından özne + geçişli eylem gelir:
   * `Tüvan ke lera sileven fali.` → İnsanın okuduğu kitap açıktır.

### 6.3 Koşul ve Karşı-Olgusal (Counterfactuals)
* **Gerçek Koşul:** `Şe Sai avelen, Mei va miraven sain.` → Gelirsen sana yardım edeceğim.
* **Ödün Koşulu (`şe-el`):** `Şe-el Sai vürelen, aremen!` → Korksan bile, düşün!
* **Karşı-Olgusal Geçmiş (`şe da ... da va`):**  
  `Şe Sai da avelen, Mei da va miraven sain.`  
  *Anlamı:* Eğer gelmiş olsaydın, sana yardım etmiş olurdum. (Geçmişte gerçekleşmemiş durum).
* **Gelecek-Geçmiş (Future-in-the-Past):** Şart öncülü olmaksızın yalın `da va` dizilimi karşı-olgusal değil, niyet/plan bildirir:  
  `Mei da va avelen.` → Gelecektim / gelme niyetindeydim.

### 6.4 Nicelik ve Mantıksal Olumsuzluk Kapsamı (Quantification)
* `Ne ena lera da avelen.` → Tek bir insan bile gelmedi / Hiç kimse gelmedi. (`∀x ¬` - Tam olumsuzluk / NONE).
* `Ne sam lera da avelen.` → Herkes gelmedi. (`¬∀x` - Kısmi olumsuzluk / NOT ALL; en az bir kişinin geldiğini mantıksal olarak kanıtlamaz).
* *(Not: `sam` deneysel bir evrensel nicelik teklifidir; kanonik standartta henüz resmi kök değildir).*

---

## 7. Günlük Konuşma Kalıpları (Everyday Dialogues)

### Diyalog 1: Karşılaşma ve Hal Hatır (Meeting a Friend)
* **A:** *Süli dei, samel! Sai süli le?*  
  (İyi günler dostum! İyi misin?)
* **B:** *Süli dei! Mei süli, Elai! Sai süli le?*  
  (İyi günler! İyiyim, teşekkür ederim! Sen nasılsın?)
* **A:** *Mei süli ya nivaren du avelen.*  
  (Ben de iyiyim ve öğrenmeye devam ediyorum.)

### Diyalog 2: Yardım İsteme ve Dayanışma (Asking for Help)
* **A:** *Samel, Sai naelen miraven mein le?*  
  (Dostum, bana yardım edebilir misin?)
* **B:** *Ei! Mei va miraven sain. Miva da avelen?*  
  (Evet! Sana yardım edeceğim. Ne oldu?)
* **A:** *Vel dumi ya Mei ne liren lüran.*  
  (Yol kapalı ve kapıyı göremiyorum.)
* **B:** *Ne vürelen! Meina va falen lüran.*  
  (Korkma! Kapıyı birlikte açacağız.)

---

## 8. Edebi Anlatı: "Köprü ve Ay" (Vel-kür ya Nüra)

Tümüyle doğrulanmış kanonik kökler ve L6.1 kurallarıyla yazılmış edebi parça:

### Orijinal Metin (Alei)
1. *Mora lo, siril dumi ya nüra selini du liren nave lo.*  
2. *Eli da şürelen vel-kür lo ya arem da avelen lavari.*  
3. *Şe-el mora dumi, nüra ri pemar ne va nesalilen.*  
4. *Eli da vesen sain ta: "Şe Mei da va nesalen velan, samel va pürelen mein ta."*  
5. *Eli fa dumen liren-lerin ya vürel da nelaren peme ta.*

### Cümle Cümle Çözümleme ve Anlamı
1. **Mora lo, siril dumi ya nüra selini du liren nave lo.**  
   *Glos:* Gece [BULUNMA], gök kapalı ve ay sessiz [GÖRÜNÜŞ] bakmak şehir [BULUNMA].  
   *TR:* Gece vakti, gökyüzü kapalıydı ve ay sessizce şehre bakmaktaydı.

2. **Eli da şürelen vel-kür lo ya arem da avelen lavari.**  
   *Glos:* O [GEÇMİŞ] durmak yol-köprü [BULUNMA] ve düşünce [GEÇMİŞ] olmak büyük.  
   *TR:* Köprünün üzerinde durdu ve düşünceleri derinleşti (büyüdü).

3. **Şe-el mora dumi, nüra ri pemar ne va nesalilen.**  
   *Glos:* [ÖDÜN] gece kapalı, ay [İYELİK] aydınlık [OLUMSUZ] [GELECEK] [EDİLGEN]-kaybolmak.  
   *TR:* Gece karanlık olsa bile, ayın ışığı yitip gitmeyecektir.

4. **Eli da vesen sain ta: "Şe Mei da va nesalen velan, samel va pürelen mein ta."**  
   *Glos:* O [GEÇMİŞ] söylemek kendi [YÖNELME]: "Eğer Ben [GEÇMİŞ] [GELECEK] kaybetmek yol-[BELİRTME], dost [GELECEK] gelmek ben [YÖNELME]."  
   *TR:* Kendi kendine fısıldadı: "Yolumu kaybetmiş olsaydım bile, dostum bana gelirdi."

5. **Eli fa dumen liren-lerin ya vürel da nelaren peme ta.**  
   *Glos:* O [BİTMİŞLİK] kapatmak göz-çoğul-[BELİRTME] ve korku [GEÇMİŞ] dönmek ışık [YÖNELME].  
   *TR:* Gözlerini yumdu ve korku yerini yeniden ışığa bıraktı.
