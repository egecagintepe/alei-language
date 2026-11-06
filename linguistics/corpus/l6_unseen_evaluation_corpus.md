# ALEI L6 GÖRÜLMEMİŞ DEĞERLENDİRME KORPUSU VE ANLAM TESTLERİ
# (Alei L6 Unseen Semantic Evaluation Corpus & Adversarial Benchmarks)

**Sürüm:** L6.0-Evaluation  
**Tarih:** Kasım 2026  
**Metodoloji:** Bu korpus, dilbilgisi modelleri, ayrıştırıcılar (parsers), tercüme sistemleri ve insanlar için bağımsız ve tarafsız bir doğrulama seti olarak tasarlanmıştır. Cümleler daha önce eğitim setlerinde veya L1–L5 korpuslarında yer almamış orijinal kombinasyonlardan oluşur. "Gold" (referans) anlamsal temsiller giriş metinlerinden ayrı tutulmuştur.

---

## BÖLÜM 1: 7 TEMATİK ALANDA GÖRÜLMEMİŞ METİNLER (7 DOMAINS)

### Alan 1: Günlük İnsan Konuşmaları (Everyday Human Conversations)
* **K1.1:** `Sai süli le? Mei da lümalen lüran ve dumi ne ve.`
  * *Alan:* Ev yaşamı / Pratik diyalog.
  * *Glos:* Sen iyi [SORU]? Ben [GEÇMİŞ] onarmak kapı-[BELİRTME] ve kapalı [OLUMSUZ] [KOŞAÇ].
* **K1.2:** `Meina du avelen nave ta; Sai va pürelen meina lo le?`
  * *Alan:* Davet / Yolculuk.
  * *Glos:* Biz [GÖRÜNÜŞ-SÜREKLİ] gitmek şehir [YÖNELME]; Sen [GELECEK] gelmek biz [BULUNMA] [SORU]?
* **K1.3:** `Davelen tüvanan mein ta; Mei va nivaren elinan.`
  * *Alan:* Talep / Öğrenme.
  * *Glos:* Vermek kitap-[BELİRTME] ben [YÖNELME]; Ben [GELECEK] öğrenmek onlar-[BELİRTME].

### Alan 2: İnsan İlişkileri ve Duygusal Durumlar (Relationship & Emotion)
* **K2.1:** `Mei da miraven mein ve samel da vesen süli tevaran.`
  * *Alan:* Dayanışma / İçsel huzur.
  * *Glos:* Ben [GEÇMİŞ] yardım-etmek ben-[DÖNÜŞLÜ-BELİRTME] ve dost [GEÇMİŞ] söylemek iyi teşekkür-[BELİRTME].
* **K2.2:** `Şe-el Sai vürelen moran, Mei ne va nesalen sain.`
  * *Alan:* Sadakat / Korkuyu aşma.
  * *Glos:* [ÖDÜN] Sen korkmak gece-[BELİRTME], Ben [OLUMSUZ] [GELECEK] kaybetmek/bırakmak sen-[BELİRTME].
* **K2.3:** `Elina du aremen meina ri vel-kür ve selin ve.`
  * *Alan:* Karşılıklı anlayış / Sessiz bağ.
  * *Glos:* Onlar [GÖRÜNÜŞ] düşünmek biz [İYELİK] yol-köprü ve sessiz [KOŞAÇ].

### Alan 3: Fiziksel Olaylar ve Durum Değişimleri (Physical Events & State Transitions)
* **K3.1:** `Lüra da avelen fali pür lera da falen elin.`
  * *Alan:* Başlama (Inchoative) ve Neden-Sonuç.
  * *Glos:* Kapı [GEÇMİŞ] olmak açık çünkü insan [GEÇMİŞ] açmak o-[BELİRTME].
* **K3.2:** `Siril du dumen ve pemar fa nelaren siril-pemar ta.`
  * *Alan:* Hava durumu / Doğal değişim.
  * *Glos:* Gök [GÖRÜNÜŞ] kapanmak ve aydınlık [BİTMİŞLİK] dönmek gök-aydınlık [YÖNELME].
* **K3.3:** `Tüvan da falilen ve lera fa liren elin.`
  * *Alan:* Edilgen eylem ve Algı.
  * *Glos:* Kitap [GEÇMİŞ] [EDİLGEN]-açılmak ve insan [BİTMİŞLİK] görmek o-[BELİRTME].

### Alan 4: Felsefi ve Mantıksal Argümanlar (Philosophical Arguments)
* **K4.1:** `Sam arem süli ve, lia ne sam arem du davelen peman.`
  * *Alan:* Epistemoloji / Düşünce eleştirisi.
  * *Glos:* Bütün düşünce iyi [KOŞAÇ], fakat [OLUMSUZ] bütün düşünce [GÖRÜNÜŞ] vermek ışık-[BELİRTME].
* **K4.2:** `Ne ena lera naelen nesalen selin-peman ke ve arem lo.`
  * *Alan:* Varlık felsefesi / İçsel sükunet.
  * *Glos:* [OLUMSUZ] bir insan yapabilmek kaybetmek sessiz-ışık-[BELİRTME] [İLGİ] [KOŞAÇ] düşünce [BULUNMA].
* **K4.3:** `Şe Sai ne liren velan, vel ne va vo nesalen.`
  * *Alan:* Ontoloji / Varlığın bağımsızlığı (Orta çatı).
  * *Glos:* [ŞART] Sen [OLUMSUZ] görmek yol-[BELİRTME], yol [OLUMSUZ] [GELECEK] [ORTA-ÇATI] kaybolmak.

### Alan 5: Anlatı Kurgusu ve Zaman Dizimi (Narrative Fiction)
* **K5.1:** `Eli da avelen nave ta den da liren dori lüran.`
  * *Alan:* Anlatı akışı (den = sonra).
  * *Glos:* O [GEÇMİŞ] gelmek şehir [YÖNELME] sonra [GEÇMİŞ] görmek büyük kapı-[BELİRTME].
* **K5.2:** `Lera ke da şürelen vel lo fa vesen: "Ne vürelen!"`
  * *Alan:* İlgi tümcesi ve doğrudan aktarım.
  * *Glos:* İnsan [İLGİ] [GEÇMİŞ] durmak yol [BULUNMA] [BİTMİŞLİK] söylemek: "[OLUMSUZ] korkmak!"
* **K5.3:** `Mora fa avelen ve nüra selin da avelen siril lo.`
  * *Alan:* Sahne tasviri.
  * *Glos:* Gece [BİTMİŞLİK] olmak ve ay sessiz [GEÇMİŞ] gelmek/belirmek gök [BULUNMA].

### Alan 6: Edebi ve Şiirsel Düzyazı (Literary Prose)
* **K6.1:** `Siril-pemar süli sam fi, lia nüra ri pemar selin ve.`
  * *Alan:* Estetik karşılaştırma ve üstünlük.
  * *Glos:* Gök-aydınlık iyi hepsi [AYRILMA/KIYAS], fakat ay [İYELİK] aydınlık sessiz [KOŞAÇ].
* **K6.2:** `Şe-el vel dori ve dumi, meina va pürelen samel ta.`
  * *Alan:* Şiirsel kararlılık.
  * *Glos:* [ÖDÜN] yol geniş ve kapalı, biz [GELECEK] ulaşmak dost [YÖNELME].
* **K6.3:** `Arem ri peme du falen dumi lüran.`
  * *Alan:* Metaforik anlatım.
  * *Glos:* Düşünce [İYELİK] ışık [GÖRÜNÜŞ] açmak kapalı kapı-[BELİRTME].

### Alan 7: Yeni Kavramlar ve Bileşik Türetimler (Novel Concepts)
* **K7.1:** `Nave-kür da lümalilen ve lera fa avelen süli.`
  * *Kavram:* `Nave-kür` (Şehir köprüsü / Viyadük).
  * *Glos:* Şehir-köprü [GEÇMİŞ] [EDİLGEN]-onarılmak ve insan [BİTMİŞLİK] olmak iyi.
* **K7.2:** `Tüvan-nave dori ve sam tüvan lo ve.`
  * *Kavram:* `Tüvan-nave` (Kütüphane / Kitap kenti).
  * *Glos:* Kitap-şehir büyük ve bütün kitap [BULUNMA] [KOŞAÇ].
* **K7.3:** `Liren-siril fa davelen peman siril lo.`
  * *Kavram:* `Liren-siril` (Gözlemevi / Gökyüzü seyir yeri).
  * *Glos:* Görmek-gök [BİTMİŞLİK] vermek ışık-[BELİRTME] gök [BULUNMA].

---

## BÖLÜM 2: ÇEKİŞMELİ MİNİMAL ÇİFTLER (ADVERSARIAL MINIMAL PAIRS)

Bu çiftler, ayrıştırıcının ve dil modellerinin ince anlamsal ayrımları ayırt edip edemediğini denetlemek için özel olarak kurgulanmıştır.

### Çift 1: Geçişli İstem Çatışması vs Edilgen Çatı
* **A:** `Vel ne va nesalen.` *(GEÇERSİZ/BELİRSİZ: Geçişli 'nesalen' eylemi nesnesiz kalamaz; fail yol olamaz).*
* **B:** `Vel ne va nesalilen.` *(GEÇERLİ: Edilgen '-il-' ile nesne özneleşmiştir; "Yol kaybedilmeyecek").*
* **C:** `Vel ne va vo nesalen.` *(GEÇERLİ: Orta çatı 'vo' ile kendi kendine kaybolmama; "Yol kaybolmaz").*

### Çift 2: Dönüşlülük (Reflexive) vs Dostluk İsmi (Samel)
* **A:** `Mei da miraven mein.` *(GEÇERLİ DÖNÜŞLÜ: Kendime yardım ettim).*
* **B:** `Mei da miraven samelan.` *(GEÇERLİ GEÇİŞLİ: Bir dosta yardım ettim - Samel asla 'kendi' demek değildir).*

### Çift 3: Kısmi Olumsuzluk vs Tam Olumsuzluk (Quantifier Scope)
* **A:** `Ne sam lera da avelen.` *(KISMİ: Herkes gelmedi; bazıları geldi, bazıları gelmedi).*
* **B:** `Ne ena lera da avelen.` *(TAM: Hiç kimse / tek bir kişi bile gelmedi).*

### Çift 4: Durum (Stative) vs Eylem (Event) vs Sonuç (Resultative)
* **A:** `Lüra fali.` *(DURUM: Kapı açıktır).*
* **B:** `Lüra du falen.` *(SÜREÇ: Kapı açılıyor / açılmakta).*
* **C:** `Lüra fa falen.` *(SONUÇ: Kapı açıldı / açık duruma geçti).*

### Çift 5: Gerçek Koşul vs Karşı-Olgusal (Counterfactual)
* **A:** `Şe Sai avelen, Mei miraven sain.` *(GERÇEK: Gelirsen yardım ederim).*
* **B:** `Şe Sai da avelen, Mei da va miraven sain.` *(KARŞI-OLGUSAL: Gelmiş olsaydın, yardım etmiş olurdum).*

---

## BÖLÜM 3: AYRIŞTIRILMIŞ REFERANS (GOLD) ANLAMSAL CEVAPLAR
*(Bu bölüm, model değerlendirme boru hatlarında sistem çıktısıyla kıyaslanacak bağımsız altın tablodur)*

```json
{
  "corpus_version": "L6.0",
  "gold_evaluations": {
    "K1.1": {
      "speech_act": "question_plus_assertion",
      "clause_1": {"subject": "Sai", "predicate": "süli", "type": "nominal_question"},
      "clause_2": {"subject": "Mei", "verb": "lümalen", "patient": "lüran", "tense": "past"},
      "clause_3": {"subject": "lüran", "predicate": "dumi", "polarity": false}
    },
    "K2.1": {
      "clause_1": {"subject": "Mei", "verb": "miraven", "voice": "reflexive", "patient": "mein"},
      "clause_2": {"subject": "samel", "verb": "vesen", "patient": "süli tevaran", "tense": "past"}
    },
    "K4.1": {
      "clause_1": {"subject": "sam arem", "predicate": "süli", "quantifier": "universal_affirmative"},
      "clause_2": {"subject": "ne sam arem", "verb": "davelen", "patient": "peman", "quantifier": "partial_negation"}
    },
    "K4.3": {
      "type": "conditional",
      "antecedent": {"subject": "Sai", "verb": "liren", "patient": "velan", "polarity": false},
      "consequent": {"subject": "vel", "verb": "nesalen", "voice": "middle", "marker": "vo", "polarity": false}
    },
    "Adversarial_Pair_1": {
      "sentence_A": {"valid": false, "reason": "valency_clash_transitive_omission"},
      "sentence_B": {"valid": true, "voice": "passive", "marker": "-il-"},
      "sentence_C": {"valid": true, "voice": "middle", "marker": "vo"}
    },
    "Adversarial_Pair_3": {
      "sentence_A": {"scope": "partial_negation", "logical_form": "¬∀x (Person(x) → Arrived(x))"},
      "sentence_B": {"scope": "total_negation", "logical_form": "∀x (Person(x) → ¬Arrived(x))"}
    }
  }
}
```
