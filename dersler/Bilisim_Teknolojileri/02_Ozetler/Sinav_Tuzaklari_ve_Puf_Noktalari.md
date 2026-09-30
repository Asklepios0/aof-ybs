# ⚠️ BİLİŞİM TEKNOLOJİLERİ (YBS101U) - AÖF Sınav Komisyonunun 10 Klasik Tuzağı ve Püf Noktaları

AÖF sınav komisyonunun öğrencileri düşürmek için şıklara özellikle yerleştirdiği çeldiriciler, kavram karmaşaları ve formül tuzakları:

---

## 🚨 Tuzak #1: Veri (Data) ile Enformasyon (Information) Karışıklığı

❌ **Öğrencilerin Düştüğü Hata / Yanıltıcı Çeldirici:**
Öğrenci işlenmemiş ham veriler ile anlamlı hale getirilmiş bilgiyi birbirine karıştırır.

✅ **İşin Doğrusu ve Sınavda Kurtaracak Püf Nokta:**
Veri (Data) tek başına bir anlam ifade etmeyen, bağlamdan yoksun ham ölçümlerdir (örn: '28', 'Ali'). Enformasyon ise bu verilerin işlenip organize edilmiş halidir (örn: 'Ali'nin vize notu 28'dir').

💡 **Akılda Kalıcı Taktik:** 'İşlenmiş' veya 'anlamlandırılmış' kelimesini gördüğün anda cevap Enformasyon'dur!

---

## 🚨 Tuzak #2: RAM ile ROM Arasındaki 'Uçuculuk' (Volatility) Tuzağı

❌ **Öğrencilerin Düştüğü Hata / Yanıltıcı Çeldirici:**
Sınavda 'Elektrik kesildiğinde silinmeyen bellek' sorulduğunda öğrencinin doğrudan RAM'i işaretlemesi.

✅ **İşin Doğrusu ve Sınavda Kurtaracak Püf Nokta:**
RAM geçicidir (volatile), elektrik kesilince içindeki veriler UÇAR. ROM ise kalıcıdır (non-volatile), elektrik kesilse bile içindeki BIOS/üretici verileri silinmez.

💡 **Akılda Kalıcı Taktik:** RAM = 'Rüzgar gibi Uçar' (Geçici); ROM = 'Rıza göstermez, Kalır' (Kalıcı).

---

## 🚨 Tuzak #3: ALU ile Control Unit (CU) Görev Çatışması

❌ **Öğrencilerin Düştüğü Hata / Yanıltıcı Çeldirici:**
Aritmetik Mantık Biriminin (ALU) bilgisayardaki tüm diğer parçalara komut gönderip onları yönettiğini düşünmek.

✅ **İşin Doğrusu ve Sınavda Kurtaracak Püf Nokta:**
Yönetim, senkronizasyon ve komut çözme işi Denetim Birimi'ne (Control Unit) aittir. ALU sadece dört işlem ve mantıksal (BÜYÜK, KÜÇÜK, EŞİT) karşılaştırmaları yapar.

💡 **Akılda Kalıcı Taktik:** Hesap yapıyorsa ALU, emir verip orkestra şefliği yapıyorsa CU (Denetim Birimi).

---

## 🚨 Tuzak #4: İşletim Sisteminin 'Uygulama Yazılımı' Olarak Düşünülmesi

❌ **Öğrencilerin Düştüğü Hata / Yanıltıcı Çeldirici:**
Windows veya Linux'un bir uygulama yazılımı olduğu yanılgısı.

✅ **İşin Doğrusu ve Sınavda Kurtaracak Püf Nokta:**
İşletim sistemleri temel 'SİSTEM YAZILIMI'dır. Uygulama yazılımları (Word, Excel, Photoshop) işletim sisteminin sunduğu altyapı üzerinde çalışır.

💡 **Akılda Kalıcı Taktik:** Bilgisayarın çalışması için şart olan ve donanımı yöneten her şey Sistem Yazılımıdır.

---

## 🚨 Tuzak #5: Hub ile Switch (Anahtar) Farkı

❌ **Öğrencilerin Düştüğü Hata / Yanıltıcı Çeldirici:**
İkisinin de yerel ağda bilgisayarları birbirine bağlayan aynı mantıkta kutular olduğunu zannetmek.

✅ **İşin Doğrusu ve Sınavda Kurtaracak Püf Nokta:**
Hub aptaldır; bir porttan gelen veriyi bütün portlara yayınlar (Broadcast), ağda çakışma ve yavaşlık yaratır. Switch ise akıllıdır; gelen verinin MAC adresine bakar ve sadece ilgili hedef bilgisayara iletir.

💡 **Akılda Kalıcı Taktik:** Sadece hedefe yollayan akıllı kutu: SWITCH. Herkese saçan: HUB.

---

## 🚨 Tuzak #6: OSI Modeli Katman Sırası ve Görevleri

❌ **Öğrencilerin Düştüğü Hata / Yanıltıcı Çeldirici:**
Ağ (Network) katmanında MAC adreslerinin kullanıldığını sanmak.

✅ **İşin Doğrusu ve Sınavda Kurtaracak Püf Nokta:**
MAC adresleri 2. Katman olan 'Veri Bağı (Data Link)' katmanında kullanılır. IP adresleri ve yönlendirme (routing) ise 3. Katman olan 'Ağ (Network)' katmanında gerçekleşir.

💡 **Akılda Kalıcı Taktik:** MAC = 2. Katman (Veri Bağı); IP = 3. Katman (Ağ Katmanı).

---

## 🚨 Tuzak #7: Virüs ile Solucan (Worm) Ayırımı

❌ **Öğrencilerin Düştüğü Hata / Yanıltıcı Çeldirici:**
İkisini eş anlamlı kabul etmek.

✅ **İşin Doğrusu ve Sınavda Kurtaracak Püf Nokta:**
Virüs kendi başına çalışamaz; bir taşıyıcı dosyaya (.exe, .doc vb.) ihtiyaç duyar ve kullanıcının o dosyayı açması gerekir. Solucan (Worm) ise kullanıcı müdahalesi olmadan ağ üzerinden kendi kendini kopyalar ve yayılır.

💡 **Akılda Kalıcı Taktik:** Kendi kendine bağımsız yayılan: SOLUCAN; Kullanıcı çalıştırınca bulaşan: VİRÜS.

---

## 🚨 Tuzak #8: Derleyici (Compiler) ile Yorumlayıcı (Interpreter) Farkı

❌ **Öğrencilerin Düştüğü Hata / Yanıltıcı Çeldirici:**
Python'ın derleyici kullandığını, C'nin yorumlayıcı olduğunu düşünmek.

✅ **İşin Doğrusu ve Sınavda Kurtaracak Püf Nokta:**
C, C++ derleyicidir (tüm kodu bir kerede makine diline çevirip .exe üretir). Python ve JavaScript ise yorumlayıcıdır (kodu satır satır okur ve hemen icra eder).

💡 **Akılda Kalıcı Taktik:** Tek seferde toplu çeviri: Derleyici (Compiler). Satır satır anlık çeviri: Yorumlayıcı (Interpreter).

---

## 🚨 Tuzak #9: Açık Kaynak Kod (Open Source) ile Ücretsiz Yazılım (Freeware) Eşit Değildir

❌ **Öğrencilerin Düştüğü Hata / Yanıltıcı Çeldirici:**
Ücretsiz olan her yazılımın açık kaynak kodlu olduğunu sanmak.

✅ **İşin Doğrusu ve Sınavda Kurtaracak Püf Nokta:**
Adobe Reader ücretsizdir (Freeware) ama kaynak kodları gizlidir (kapalı kaynak). Açık kaynak kodlu bir yazılım ise hem ücretsiz olabilir hem de kaynak kodları herkes tarafından görülebilir ve geliştirilebilir.

💡 **Akılda Kalıcı Taktik:** Freeware = Kod kapalı ama bedava. Open Source = Kod açık, herkes geliştirebilir.

---

## 🚨 Tuzak #10: Web 2.0 ile Web 3.0 Ayrımı

❌ **Öğrencilerin Düştüğü Hata / Yanıltıcı Çeldirici:**
Sosyal medyanın ve Wikipedia'nın Web 3.0 olduğunu varsaymak.

✅ **İşin Doğrusu ve Sınavda Kurtaracak Püf Nokta:**
Kullanıcıların içerik ürettiği blog, sosyal medya ve video paylaşım siteleri Web 2.0'dır. Web 3.0 ise semantik web (makinelerin anlamlandırdığı web), yapay zeka entegrasyonu ve merkeziyetsiz blokzincir yapılarıdır.

💡 **Akılda Kalıcı Taktik:** Sosyal Medya = Web 2.0; Semantik Web ve Yapay Zeka = Web 3.0.

---

