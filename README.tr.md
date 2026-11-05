# Alei Language Project (çalışma adı)

İnsanların öğrenmesi ve konuşması hedeflenen, açık anlam katmanı ve Agent Skills araçları bulunan yapay dil projesi. **Alei** bir selamdır; dilin resmî adı henüz seçilmedi. v1.0 bir çalışma standardıdır; akıcılık veya CEFR sertifikası kanıtlanmış değildir. [Başlangıç](docs/start-here.md) · [Standart](standard/README.md) · [English](README.md)

A: **Alei!** — Merhaba!  
B: **Sai süli le?** — İyi misin?  
A: **Ei, mei süli.** — Evet, iyiyim.

Latin temelli alfabe sekizi ünlü 28 harften oluşur. **ñ** İspanyolca ñ gibidir; **ŋ**, İngilizce “sing” sonundaki sestir. `ı` ile `i` farklıdır. `ai`, `ei`, `ae`, `au` tek heceli kayışlardır; vurgu genellikle sondan ikinci hecededir. Ayrıntılar için standart §2'ye bakın.

Gündelik konuşma ve tireli açık tanımlar aynı dilin iki kullanımıdır. `meyar` meyvedir; `meyar-ro-yenar-li-reş-ze-selim-mu-molir`, ağaç kaynaklı, tipik olarak kırmızı, tatlı ve yuvarlak bir meyveyi tarif eder; kesin elma demek değildir. `Jajaya` gibi bilinmeyen bir ad ortak tanım gerektirir. Bu sistem şifreleme değildir.

Python 3.11+ ile bir proje kopyasında `python -m pip install -e .` çalıştırın; `python -m alei_language.cli lookup sael`, `analyze sain`, `parse-semantic meyar-ro-yenar-li-reş-ze-selim-mu-molir` ve `validate` komutlarını aynı modül adıyla kullanın. `python -m unittest discover -s tests` testleri çalıştırır. Araçlar sınırlıdır; aday çözümleme kabul edilmiş sözcük değildir. Kaynak verileri için proje kopyası gerekir. [Agent Skills](docs/how-agent-skills-work.md) model ağırlığını değiştirmez ve kendiliğinden çalışmaz; bağımsız model ve konuşur testleri henüz yapılmadı.

Kod yazmadan öğrenebilir, ad tartışmasına katılabilir, kelime önerebilir veya gramer sorunu bildirebilirsiniz. Issues ve Discussions açıldığında ilgili formda örnek ve kaynak bölümü belirtin. [Katkı](CONTRIBUTING.md), [yönetişim](GOVERNANCE.md), [yol haritası](ROADMAP.md) ve [denetim](docs/audits/bootstrap-audit.md). İnsan sahibi ve topluluğun katkıları proje geçmişinde anılır; dil değişikliği için sahibin kabulü gerekir.

Kod, betikler ve beceriler [Apache-2.0](LICENSE); özgün dil metinleri, standart, örnekler ve türetilmiş sözlük verileri [CC BY 4.0](LICENSE-DOCS) ile lisanslıdır. Yeniden paylaşırken uygun atıf yapın, lisans bağlantısını verin ve değişiklikleri belirtin. Üçüncü taraf materyaller kendi koşullarına tabidir.
## Katılmak için kod yazmanız gerekmez

Bir sorunu bildirmek, sözcük veya deyim önermek için [Issues](https://github.com/egecagintepe/alei-language/issues/new/choose) sayfasındaki uygun formu seçin. Örneği, ne demek istediğinizi ve biliyorsanız ilgili kaynak bölümünü yazın; Türkçe veya İngilizce kullanabilirsiniz. Dil adı hakkındaki [tartışmaya](https://github.com/egecagintepe/alei-language/discussions/6) katılabilirsiniz. Öneriler, sahibinin açık kararı kaydedilene kadar standart değildir.
