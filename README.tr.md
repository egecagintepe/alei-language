# Alei — İnsan Odaklı Açık Yapay Dil

[![Lisans: Apache-2.0](https://img.shields.io/badge/Kod-Apache--2.0-blue.svg)](LICENSE)
[![Belgeler: CC BY 4.0](https://img.shields.io/badge/Belgeler-CC%20BY%204.0-lightgrey.svg)](LICENSE-DOCS)
[![Standart: v1.0 / v1.1.0-RC](https://img.shields.io/badge/Standart-v1.1.0--RC-green.svg)](standard/README.md)
[![Dil Adı: Alei](https://img.shields.io/badge/Dil-Alei-teal.svg)](governance/decisions/README.md)

**Alei**, duru bir anlatım, şeffaf anlamsal türetim ve edebi zenginlik hedefiyle geliştirilen, insan odaklı açık bir yapay edebi dildir. **Alei**, dilin sahibince onaylanmış resmî adıdır ([AD-2026-001](governance/decisions/README.md)); `Alei!` aynı zamanda dilin evrensel selamlaşma ifadesidir ("Merhaba!").

Dil, kolay öğrenilebilir 270 köklü üretken bir gramer omurgasını; kavramların kapalı ve ezbere sözcükler yerine kaynak, renk, tat, işlev ve malzeme gibi nitelik rolleriyle açıkça tarif edilmesini sağlayan **şeffaf anlambilim (transparent semantics)** katmanıyla birleştirir.

> [!NOTE]
> **Önce İnsan Alei:** Alei, insanların konuşması, edebiyat üretmesi ve öğrenmesi için tasarlanmıştır. Ayrı bir çalışma olan *AleiFlow* deneysel bir programlama dili hattıdır ve bu deponun öncelikli amacı değildir.

[English README](README.md) · [Başlangıç Rehberi](docs/start-here.md) · [Gramer Kılavuzu](docs/grammar.md) · [Standart Belgesi](standard/README.md) · [Etkileşimli Dokümantasyon Önizlemesi](docs/site/index.html)

---

## 1. Kısa Diyalog ve Telaffuz

Onaylı Alei v1.1.0 kurallarıyla tipik bir gündelik diyalog:

```text
A: Alei! Sai süli le?
   [aˈlei̯ | sai̯ ˈsy.li le]
   "Merhaba! İyi misin?"
   (merhaba | sen iyi-SIFAT SORU)

B: Alei! Mei süli. Sai yelen ke miraven Meian le?
   [aˈlei̯ | mei̯ ˈsy.li || sai̯ ˈje.len ke miˈra.ven ˈmei̯.an le]
   "Merhaba! Ben iyiyim. Bana yardım edebilir misin?"
   (merhaba | ben iyi-SIFAT || sen yapabilmek-FİİL Kİ yardım-etmek-FİİL ben-BELİRTME SORU)

A: Ei, Mei yelen ke miraven Saian. Süli vel!
   [ei̯ | mei̯ ˈje.len ke miˈra.ven ˈsai̯.an || ˈsy.li vel]
   "Evet, sana yardım edebilirim. Yolun açık olsun!"
   (evet | ben yapabilmek-FİİL Kİ yardım-etmek-FİİL sen-BELİRTME || iyi-SIFAT yol)
```

### Bir Bakışta Telaffuz
- **28 harfli Latin alfabesi** (8 ünlü: `a e ı i o ö u ü`; 20 ünsüz: `b d f g h j k l m n ñ ŋ p r s ş t v y z`).
- `ı` (art, düz) ile `i` (ön, düz) kesinlikle ayrı seslerdir.
- `ñ` damaksıl geniz sesi [ɲ] (İspanyolca *ñ* gibi); `ŋ` artdamaksıl geniz sesi [ŋ] (İngilizce *sing* sonundaki gibi).
- `ai`, `ei`, `ae`, `au` ikili ünlüleri (diphthong) tek hecede kayan seslerdir.
- Düzenli vurgu: sondan bir önceki hecededir.

---

## 2. Alei'yi İlginç Kılan Nedir?

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        Alei Mimari Genel Bakışı                        │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
    ┌───────────────────────────────┴───────────────────────────────┐
    │                                                               │
    ▼                                                               ▼
┌───────────────────────────────┐       ┌───────────────────────────────┐
│       İnsan Edebi Çekirdeği   │       │   Şeffaf Anlambilim Katmanı   │
│  - 270 onaylı kök             │       │  - Analitik tanımlar          │
│  - 28 harfli Latin alfabesi   │       │  - BAŞ-ROL-DEĞER yapısı       │
│  - Sondan bir önceki hece vurgusu│    │  - Ontolojik tip güvenliği    │
│  - Düzenli -en, -i, -na, -an  │       │  - Ezbere tahmini reddeder    │
└───────────────┬───────────────┘       └───────────────┬───────────────┘
                │                                       │
                └───────────────────┬───────────────────┘
                                    │
                                    ▼
┌───────────────────────────────────────────────────────────────────────┐
│                     Alei Analiz ve AST Motoru                         │
│  - Belirsizlik sınıflandırmalı tipli SentenceAST (IR)                 │
│  - Makinece okunur fiil valans çerçeveleri ve çatı denetimi           │
│  - 58 testlik deterministik doğrulama paketi                          │
└───────────────────────────────────┬───────────────────────────────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    ▼                               ▼
┌───────────────────────────────────────┐   ┌───────────────────────────┐
│     İnsan Yazımı ve Agent Skills      │   │    Akademik Araştırma Lab │
│  - 7 prosedürel beceri                │   │  - Alei-Bench (6 görev)   │
│  - Şiir, diyalog ve düzyazı           │   │  - Kör çeviri paketi v2   │
│  - RFC tabanlı sahip yönetişimi       │   │  - Epistemik kalibrasyon  │
└───────────────────────────────────────┘   └───────────────────────────┘
                    │
                    ▼
     [AleiFlow ayrı, deneysel bir programlama dili çalışma hattıdır]
```

1. **Kök Ekonomisi ve Üretken Morfoloji:** Özenle korunan 270 onaylı kök; düzenli isim, fiil (`-en`), sıfat (`-i`) ve çoğul (`-na`) çekimleriyle geniş bir anlatım alanı sağlar.
2. **Şeffaf Açık Anlambilim:** Gündelik sözcüklerin ötesinde, karmaşık veya yeni kavramlar tireli `BAŞ-ROL-DEĞER` kalıplarıyla çözümlenebilir:
   - `meyar` = meyve
   - `meyar-ro-yenar-li-reş-ze-selim-mu-molir` = ağaçtan gelen (`ro-yenar`), tipik olarak kırmızı (`li-reş`), tatlı (`ze-selim`) ve yuvarlak (`mu-molir`) bir meyve.
   *Bu dizilim dünyadaki her elmayı kesin olarak tek başına karşıladığını iddia etmez; ancak nesnenin temel algısal özelliklerini berrak biçimde aktarır.*
3. **Epistemik Disiplin:** Alei araçları, tanımlanmamış kökler hakkında dayanaksız tahmin yürütmeyi (`Jajaya` gibi) reddeder. Paylaşılan bir tanım yoksa sistem zorlama anlam uydurmaz.
4. **Yönetişimli Dil Gelişimi:** Dilin kuralları ve yeni kökleri, insan dil sahibinin resmî karar mekanizmasıyla (RFC ve AD kararları) güvenle ilerler.
5. **Akademik Araştırma Altyapısı:** [Araştırma Çalışma Alanı](research/README.md), [Literatür Taraması](research/literature-survey.md), [Alei-Bench Spesifikasyonu](research/benchmark-design.md) ve [2026–2027 Yayın Yol Haritası](research/roadmap.md) incelenebilir.

---

## 3. 60 Saniyede Başlayın

Alei, **Python 3.11+** gerektirir. Depoyu klonlayıp araçları bir dakikada deneyebilirsiniz:

```bash
# 1. Depoyu klonlayın
git clone https://github.com/egecagintepe/alei-language.git
cd alei-language

# 2. Paketi düzenlenebilir (editable) modda kurun
python -m pip install -e .

# 3. v1.1.0'da dil sahibince onaylanan yardım kökünü (Mirav) sorgulayın
python -m alei_language.cli lookup mirav --version 1.1.0

# 4. Eski biçimi sorgulayın (Mivav, sürüm uyarısıyla birlikte döner)
python -m alei_language.cli lookup mivav --version 1.1.0

# 5. Tam bir cümleyi tipli AST ve valans denetimiyle ayrıştırın
python -m alei_language.cli parse-ast "Mei da sileven tüvanan." --version 1.1.0

# 6. Şeffaf anlamsal bir ifadeyi çözümleyin
python -m alei_language.cli parse-semantic "meyar-li-reş-ze-selim"

# 7. Test paketini çalıştırın (58 deterministik test)
python -m unittest discover -s tests
```

---

## 4. Öğrenme Kaynakları ve Belgeler

- 📖 **[Başlangıç Rehberi](docs/start-here.md):** Adım adım gramer, sözcük sırası ve durum ekleri.
- 📐 **[Gramer Kılavuzu](docs/grammar.md):** SVO/SOV dizilimi, isim yüklemleri, `le` soru eki ve `ke` tümleç yapısı.
- 🗂️ **[Sözlük Dizini](docs/glossary.md):** v1.0 kökleri, v1.1.0 eklemeleri ve işlev sözcükleri.
- 🎭 **[Deneysel Edebiyat Külliyatı](linguistics/corpus/experimental-literature.md):** Özgün düzyazılar, şiirler ve kapsam/zaman/valans karşıtlıklarını gösteren 12 minimal çift.
- 💬 **[İletişimsel Diyaloglar](linguistics/corpus/experimental-dialogues.md):** 30 pratik günlük replik ve tutarlı karakterlerle 8 çok turlu diyalog.
- 🔬 **[L5 Dil Mühendisliği Araştırma Raporu](docs/research/blind-translation-01-five-stanza-audit.md):** ChatGPT'den Gemini'ye yapılan ilk kör çeviri deneyinin ayrıntılı denetimi.

---

## 5. Geliştiriciler ve Yapay Zekâ Sistemleri İçin

Alei, `.agents/skills/` dizini altında yedi kural temelli **Agent Skills** içerir:
- `alei-speak`: Karakterli diyalog ve konuşma alıştırması.
- `alei-tutor`: Adım adım insan dili eğitimi.
- `alei-translate`: Alei, Türkçe ve İngilizce arasında belirsizlik izlemeli çeviri.
- `alei-audit`: Sözdizimi ve şeffaf anlambilim doğrulama.
- `alei-propose`: Fonotaktik kurallara uygun aday kök taslağı hazırlama.
- `alei-research`: Kök ailelerini ve tarihsel kaynakları inceleme.
- `alei-literary`: Şiir ve edebi düzyazı üretimi.

> [!IMPORTANT]
> Agent Skills, yapay zekâ model ağırlıklarını kalıcı olarak değiştirmez; harici bir işletici olmadan kendiliğinden çalışmaz.

---

## 6. Nasıl Katkıda Bulunabilirsiniz?

Dilbilimcilerin, yapay dil meraklılarının, yazarların, eğitimcilerin ve yazılımcıların katkılarını bekliyoruz!

- **Yeni Sözcük veya Deyim Önerin:** [Sözcük Öneri Formunu](.github/ISSUE_TEMPLATE/idiom-proposal.yml) kullanın. Yeni kök önermeden önce mevcut köklerle şeffaf bileşikler üretmeyi tercih edin.
- **Gramer Açığı veya Uyuşmazlığı Bildirin:** [Gramer Açığı Bildirim Formunu](.github/ISSUE_TEMPLATE/grammar-gap.yml) doldurun.
- **Edebi Metin Katkısı Sunun:** Deneysel külliyata kısa öyküler, şiirler veya diyaloglar önerin.
- **Topluluğa Katılın:** [GitHub Tartışmaları (Discussions)](https://github.com/egecagintepe/alei-language/discussions) bölümünde fikirlerinizi paylaşın.

*Not: Önerilen tüm sözcükler ve gramer kuralları, dil sahibinin resmî kararı (`AD-2026-xxx`) çıkana kadar `öneri / deneysel` statüsünde kalır.*

---

## 7. Mevcut Durum ve Sürüm Haritası

| Katman | Dal / Durum | Temel Özellikler |
|---|---|---|
| **v1.0 (Arşiv)** | `main` | Orijinal standart (SHA-256 `265fcc0...`); 270 kök, 101 örnek cümle. |
| **Bütünlük Denetimi** | PR #7 (`phase-2/linguistic-integrity`) | 101 cümle denetimi, korumacı ayrıştırıcı, tip denetleyici. |
| **v1.1.0-RC** | PR #8 (`owner/alei-v1.1-pr`) | Resmî ad **Alei** ([AD-2026-001](governance/decisions/README.md)); tercih edilen yardım kökü **Mirav** ([AD-2026-002](governance/decisions/README.md)); sürümlü katman. |
| **L5 Aşaması (Aktif)** | Dal: `l5/linguistic-engineering-community` | Tipli AST, valans doğrulama, kör çeviri denetimi, 42 fixture'lık test paketi, edebi külliyat. |

---

## 8. Lisans ve Atıf

- **Yazılım ve Beceriler:** [Apache-2.0](LICENSE) lisanslıdır.
- **Dilbilimsel Veri, Standart ve Belgeler:** [CC BY 4.0](LICENSE-DOCS) lisanslıdır.

Akademik veya yapay dil araştırmalarında Alei'ye atıf için:
```bibtex
@misc{alei2026,
  author = {Tepe, Ege Çağın and Alei Contributors},
  title = {Alei: An Open Human-First Constructed Language with Transparent Semantics},
  year = {2026},
  publisher = {GitHub},
  howpublished = {\url{https://github.com/egecagintepe/alei-language}}
}
```
