# ALEI L6 AÇIK GELİŞTİRME KORPUSU VE ANLAMSAL DOĞRULAMA SETİ
# (Alei L6 Open Development Corpus & Semantic Verification Suite)

**Sürüm:** L6.1-Open-Development  
**Tarih:** Kasım 2026  
**Sınıflandırma:** Açık Geliştirme Korpusu (Open Development Corpus)  
**Önemli Metodolojik Uyarı:** Bu belge, dilbilgisi ayrıştırıcılarının ve semantik motorların geliştirilme sürecinde kullanılan **açık bir geliştirme setidir**. Referans çözümler bu belgede açıklandığı için, bu korpus **bağımsız/kör (blind) bir kıyaslama testi olarak sunulamaz**. Bağımsız kör değerlendirmeler, ayrıştırıcı ve model geliştirmeden tamamen yalıtılmış harici veri kümeleri ve saklı altın cevaplar (`evaluations/`) üzerinden yürütülmelidir.

---

## BÖLÜM 1: KANONİK VE DENEYSEL İNCELİKLERLE 7 TEMATİK ALAN

*(Kanonik bağlaç `ya` ("ve"), sebep bağlacı `sira` ("çünkü"), zıtlık `lia` ("ama"), teşekkür nidası `Elai`, karşılaştırma `peli ... nera` ve son-edat `ve` ("ile/beraber") kurallarına tam uyumludur).*

### Alan 1: Günlük İnsan Konuşmaları (Everyday Human Conversations)
* **K1.1:** `Sai süli le? Mei da lümalen lüran ya dumi ne.`
  * *Alan:* Ev yaşamı / Pratik diyalog.
  * *Glos:* Sen iyi [SORU]? Ben [GEÇMİŞ] onarmak kapı-[BELİRTME] ve kapalı değil.
* **K1.2:** `Meina du avelen nave ta; Sai va pürelen meina ve le?`
  * *Alan:* Davet / Yolculuk. (Not: `meina ve` = bizimle / comitative postposition).
  * *Glos:* Biz [GÖRÜNÜŞ-SÜREKLİ] gitmek şehir [YÖNELME]; Sen [GELECEK] gelmek biz [İLE/BERABER] [SORU]?
* **K1.3:** `Davelen tüvanan mein ta; Mei va nivaren elinan.`
  * *Alan:* Talep / Öğrenme (İki nesneli yönelme `ta`).
  * *Glos:* Vermek kitap-[BELİRTME] ben [YÖNELME]; Ben [GELECEK] öğrenmek onlar-[BELİRTME].

### Alan 2: İnsan İlişkileri ve Duygusal Durumlar (Relationship & Emotion)
* **K2.1:** `Mei da miraven mein ya samel da vesen: "Elai!"`
  * *Alan:* Dayanışma / İçsel huzur (Dönüşlülük `Mei ... mein` ve kanonik teşekkür `Elai`).
  * *Glos:* Ben [GEÇMİŞ] yardım-etmek ben-[DÖNÜŞLÜ-BELİRTME] ve dost [GEÇMİŞ] söylemek: "Teşekkür ederim!"
* **K2.2:** `Şe-el Sai vürelen moran, Mei ne va nesalen sain.`
  * *Alan:* Sadakat / Korkuyu aşma (Ödün şartı `şe-el` ve Deneyimleyen/Uyaran çatısı).
  * *Glos:* [ÖDÜN-ŞART] Sen korkmak gece-[UYARAN-BELİRTME], Ben [OLUMSUZ] [GELECEK] kaybetmek/bırakmak sen-[BELİRTME].
* **K2.3:** `Elina du aremen meina ri vel-kür lo ya selini.`
  * *Alan:* Karşılıklı anlayış / Sessiz bağ (Bilişsel eylem `aremen` ve durum yüklemi `selini`).
  * *Glos:* Onlar [GÖRÜNÜŞ] düşünmek biz [İYELİK] yol-köprü [BULUNMA] ve sessiz.

### Alan 3: Fiziksel Olaylar ve Durum Değişimleri (Physical Events & State Transitions)
* **K3.1:** `Lüra da avelen fali sira lera da falen elin.`
  * *Alan:* Başlama (Inchoative) ve Neden-Sonuç (Kanonik `sira` = çünkü).
  * *Glos:* Kapı [GEÇMİŞ] olmak açık çünkü insan [GEÇMİŞ] açmak o-[BELİRTME].
* **K3.2:** `Siril du dumen ya pemar fa nelaren siril-pemar ta.`
  * *Alan:* Hava durumu / Doğal değişim (`ya` ile iki bağımsız tümce).
  * *Glos:* Gök [GÖRÜNÜŞ] kapanmak ve aydınlık [BİTMİŞLİK] dönmek gök-aydınlık [YÖNELME].
* **K3.3:** `Tüvan da falilen ya lera fa liren elin.`
  * *Alan:* Düzenli edilgen çatı (`-il-`) ve algı eylemi (`liren`).
  * *Glos:* Kitap [GEÇMİŞ] [EDİLGEN]-açılmak ve insan [BİTMİŞLİK] görmek o-[BELİRTME].

### Alan 4: Felsefi ve Mantıksal Argümanlar (Philosophical Arguments)
* **K4.1:** `Ne sam arem du davelen peman ya lia arem süli.`
  * *Alan:* Epistemoloji / Kısmi olumsuzluk (`ne sam` = hepsi değil / NOT ALL; `∃x` zorunluluğu doğurmaz).
  * *Glos:* [OLUMSUZ] bütün düşünce [GÖRÜNÜŞ] vermek ışık-[BELİRTME] ve ama düşünce iyi.
* **K4.2:** `Ne ena lera naelen nesalen selin-peman ke arem lo.`
  * *Alan:* Mantıksal tam olumsuzluk (`ne ena` = hiç kimse / NONE; `ke` ile tümce tamlaması).
  * *Glos:* [OLUMSUZ] bir insan yapabilmek kaybetmek sessiz-ışık-[BELİRTME] [İLGİ] düşünce [BULUNMA].
* **K4.3:** `Şe Sai ne liren velan, vel ne va vo nesalen.`
  * *Alan:* Ontoloji / Varlığın bağımsızlığı (Orta çatı `vo nesalen` = kendi kendine kaybolmaz).
  * *Glos:* [ŞART] Sen [OLUMSUZ] görmek yol-[BELİRTME], yol [OLUMSUZ] [GELECEK] [ORTA-ÇATI] kaybolmak.

### Alan 5: Anlatı Kurgusu ve Zaman Dizimi (Narrative Fiction)
* **K5.1:** `Eli da avelen nave ta ya da liren dori lüran.`
  * *Alan:* Anlatı akışı (Kanonik `ya` ile geçmiş eylem dizilimi).
  * *Glos:* O [GEÇMİŞ] gitmek şehir [YÖNELME] ve [GEÇMİŞ] görmek büyük kapı-[BELİRTME].
* **K5.2:** `Lera ke da şürelen vel lo fa vesen: "Ne vürelen!"`
  * *Alan:* Özne ilgi tümcesi (`Lera ke...`) ve doğrudan aktarılan söz.
  * *Glos:* İnsan [İLGİ] [GEÇMİŞ] durmak yol [BULUNMA] [BİTMİŞLİK] söylemek: "[OLUMSUZ] korkmak!"
* **K5.3:** `Mora fa avelen ya nüra selin da avelen siril lo.`
  * *Alan:* Sahne tasviri ve gece/ay ayrımı.
  * *Glos:* Gece [BİTMİŞLİK] olmak ve ay sessiz [GEÇMİŞ] belirmek gök [BULUNMA].

### Alan 6: Edebi ve Şiirsel Düzyazı (Literary Prose)
* **K6.1:** `Eli peli süli Mei nera ya nüra ri pemar selini.`
  * *Alan:* Kanonik karşılaştırma (`peli ... nera`) ve şiirsel ahenk.
  * *Glos:* O daha iyi ben [KIYASLA] ve ay [İYELİK] aydınlık sessiz.
* **K6.2:** `Şe-el vel lavari ya dumi, meina va pürelen samel ta.`
  * *Alan:* Şiirsel kararlılık (Geniş yol `vel lavari`, bağlaç `ya`).
  * *Glos:* [ÖDÜN] yol geniş ve kapalı, biz [GELECEK] ulaşmak dost [YÖNELME].
* **K6.3:** `Arem ri peme du falen dumi lüran.`
  * *Alan:* Metaforik anlatım.
  * *Glos:* Düşünce [İYELİK] ışık [GÖRÜNÜŞ] açmak kapalı kapı-[BELİRTME].

### Alan 7: Yeni Kavramlar ve Bileşik Türetimler (Novel Concepts)
* **K7.1:** `Nave-kür da lümalilen ya lera fa avelen süli.`
  * *Kavram:* `Nave-kür` (Şehir köprüsü / Viyadük).
  * *Glos:* Şehir-köprü [GEÇMİŞ] [EDİLGEN]-onarılmak ve insan [BİTMİŞLİK] olmak iyi.
* **K7.2:** `Mei ri lem peli lavari Sai ri lem nera.`
  * *Kavram:* Kanonik tam karşılaştırma (§4.9 kanıt cümlesi).
  * *Glos:* Ben [İYELİK] ev daha büyük Sen [İYELİK] ev [KIYASLA].
* **K7.3:** `Liren-siril fa davelen peman siril lo.`
  * *Kavram:* `Liren-siril` (Gözlemevi / Gökyüzü seyir yeri).
  * *Glos:* Görmek-gök [BİTMİŞLİK] vermek ışık-[BELİRTME] gök [BULUNMA].

---

## BÖLÜM 2: ÇEKİŞMELİ MİNİMAL ÇİFTLER (ADVERSARIAL MINIMAL PAIRS)

### Çift 1: Geçişli İstem Çatışması vs Edilgen vs Orta Çatı
* **A:** `Vel ne va nesalen.` *(BELİRSİZ/ÇATIŞMA: Geçişli 'nesalen' zorunlu nesne ister; fail yol olamaz).*
* **B:** `Vel ne va nesalilen.` *(GEÇERLİ EDİLGEN: '-il-' ile nesne özneleşmiştir; "Yol kaybedilmeyecek").*
* **C:** `Vel ne va vo nesalen.` *(GEÇERLİ ORTA ÇATI: 'vo' ile spontane süreç; "Yol kaybolmaz").*

### Çift 2: Bağlaç 'ya' vs Son-edat 've'
* **A:** `Lera da avelen ya Mei da liren elin.` *(GEÇERLİ: 'ya' iki bağımsız tümceyi bağlayan kanonik bağlaçtır).*
* **B:** `Lera da avelen ve Mei da liren elin.` *(GEÇERSİZ: 've' comitative son-edattır ("ile/beraber"); tümce bağlacı yapılamaz).*

### Çift 3: Kısmi Olumsuzluk vs Tam Olumsuzluk (Quantifier Scope)
* **A:** `Ne sam lera da avelen.` *(KISMİ: Herkes gelmedi / NOT ALL; `¬∀x`, en az bir kişinin geldiğini mantıksal olarak kanıtlamaz).*
* **B:** `Ne ena lera da avelen.` *(TAM: Hiç kimse / tek bir kişi bile gelmedi / NONE; `∀x ¬`).*

### Çift 4: Karşılaştırma 'peli ... nera' vs Ayrılma 'fi'
* **A:** `Eli peli süli Mei nera.` *(KANONİK KIYAS: O benden daha iyidir).*
* **B:** `Eli süli Mei fi.` *(SAPMA: 'fi' ayrılma edatıdır ("-den"); kıyas için standart 'peli ... nera' zorunludur).*

### Çift 5: Gelecek-Geçmiş (Future-in-the-Past) vs Karşı-Olgusal (Counterfactual)
* **A:** `Mei da va avelen.` *(GELECEK-GEÇMİŞ / NİYET: Gelecektim / gelme niyetindeydim; şart öncülü olmadığı için counterfactual değildir).*
* **B:** `Şe Sai da avelen, Mei da va miraven sain.` *(KARŞI-OLGUSAL GEÇMİŞ: Gelmiş olsaydın, yardım etmiş olurdum).*

---

## BÖLÜM 3: GELECEK BAĞIMSIZ DEĞERLENDİRME PROTOKOLÜ (FUTURE EVALUATION PROTOCOL)

Gelecekteki dilbilgisi ve çoklu-model kör testlerinin bilimsel geçerliliği için şu protokol uygulanacaktır:
1. **Veri Ayrımı:** Değerlendirme setleri asla `linguistics/` veya `docs/` altında açık kaynak olarak tutulmayacak; şifreli veya kapalı `evaluations/blind-eval-v*/` dizinlerinde saklanacaktır.
2. **Kör Değerlendirme:** Test edilen modele girdi verilirken gold cevaplar, kural açıklamaları ve ipuçları context penceresine verilmeyecektir.
3. **Ölçüm Kriterleri:** İnsan öğrenilebilirliği ve edebi estetik puanları, gerçek insan deneklerle çift-kör anketler yapılmadan sayısal metrik olarak iddia edilmeyecektir.
