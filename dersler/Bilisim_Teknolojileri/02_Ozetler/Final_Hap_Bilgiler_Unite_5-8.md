# 📗 BİLİŞİM TEKNOLOJİLERİ (YBS101U) - Final Hap Bilgiler ve Kapsamlı Tekrar (5 - 8. Üniteler + Vize Özeti)

AÖF Dönem Sonu (Final) sınavında soruların yaklaşık %70'i (14 soru) 5-8. ünitelerden, %30'u (6 soru) 1-4. vize konularından gelir.

---

## 📌 Ünite 5: İnternet ve Mobil Teknolojiler

**Ana Başlıklar:** İnternetin Tarihi, ARPANET ve TCP/IP, WWW ve Web Nesilleri, Mobil İletişim Kuşakları (1G-5G), Bulut Bilişim

### ⚡ Sınav Odaklı Hap Bilgiler ve Kritik Notlar
- **İnternetin Doğuşu:** 1969 yılında ABD Savunma Bakanlığı İleri Araştırma Projeleri Ajansı (DARPA) tarafından kurulan 'ARPANET' internetin ilk atasıdır.
- **TCP/IP:** İnternetin ortak iletişim protokolü kümesidir. Vinton Cerf ve Robert Kahn tarafından geliştirilmiştir.
- **World Wide Web (WWW):** 1989 yılında CERN laboratuvarlarında İngiliz bilim insanı Tim Berners-Lee tarafından bilgi paylaşımını kolaylaştırmak amacıyla icat edilmiştir (HTTP, HTML ve URL standartlarını belirlemiştir).
- **Web 1.0 (Statik Web):** Tek taraflı iletişim. Kullanıcı sadece okuyucudur, içerik üreticileri web yöneticileridir.
- **Web 2.0 (Sosyal ve Etkileşimli Web):** Çift taraflı iletişim. Kullanıcılar içerik üretir, paylaşır ve etkileşime girer (Bloglar, Wikipedia, Sosyal Medya, YouTube).
- **Web 3.0 (Semantik Web / Anlamsal Web):** Makinelerin verileri anlayıp yorumlayabildiği, yapay zeka destekli ve merkeziyetsiz web yapısıdır.
- **Mobil İletişim Nesilleri:** 
- **  - 1G:** Analog sinyaller, sadece ses iletimi.
- **  - 2G:** Dijital iletişim (GSM), SMS (kısa mesaj) ve çok düşük hızlı veri transferi (GPRS/EDGE).
- **  - 3G:** Mobil internet, görüntülü görüşme, veri hızında büyük artış (UMTS/HSPA).
- **  - 4G (LTE):** Yüksek hızlı mobil genişbant, HD video akışı, düşük gecikme süresi.
- **  - 5G:** Ultra yüksek hız (Gigabit seviyesi), 1 milisaniyenin altında ultra düşük gecikme, kitlesel IoT bağlantı kapasitesi.
- **Bulut Bilişim Hizmet Modelleri:** 
- **  - IaaS (Altyapı):** Sunucu, sanal makine, ağ ve depolama kiralama (AWS EC2, Google Compute Engine).
- **  - PaaS (Platform):** Geliştiricilere işletim sistemi, veritabanı ve çalışma ortamı sunma (Heroku, Google App Engine).
- **  - SaaS (Yazılım):** Son kullanıcılara internet üzerinden hazır yazılım sunma (Gmail, Dropbox, Salesforce).

---

## 📌 Ünite 6: İletişim Alt Yapısı ve Güvenlik

**Ana Başlıklar:** Ağ Türleri ve Topolojileri, Ağ Donanımları, OSI ve TCP/IP Modeli, Bilgi Güvenliği (CIA), Siber Tehditler

### ⚡ Sınav Odaklı Hap Bilgiler ve Kritik Notlar
- **Ağ Türleri (Coğrafi Boyuta Göre):** PAN (Kişisel Alan Ağı - Bluetooth), LAN (Yerel Alan Ağı - Ev/Ofis), CAN (Kampüs Alan Ağı - Üniversite), MAN (Metropol Alan Ağı - Şehir çapında), WAN (Geniş Alan Ağı - Şehirler/ülkeler arası; en büyük WAN İnternettir).
- **Ağ Topolojileri:** Yol (Bus - tek bir ana hat), Halka (Ring - jeton mantığı), Yıldız (Star - tüm cihazlar merkezi bir Switch/Hub'a bağlıdır, en yaygın kullanılanıdır), Ağaç (Tree), Örgü (Mesh - her düğüm diğerine bağlıdır, en yüksek hata toleransına sahiptir ancak en maliyetlisidir).
- **Ağ Cihazları:** Hub (Veriyi tüm portlara yayar/broadcast, verimsizdir), Switch (Anahtar - MAC adresine bakarak veriyi sadece ilgili hedefe iletir, Katman 2), Router (Yönlendirici - IP adreslerine bakarak farklı ağlar arasında yönlendirme yapar, Katman 3), Modem (Analog ve dijital sinyal dönüşümü yapar).
- **OSI Modeli (7 Katman - Aşağıdan Yukarıya):** 1. Fiziksel, 2. Veri Bağı (Data Link - MAC adresi, Switch), 3. Ağ (Network - IP adresi, Router), 4. İletim (Transport - TCP, UDP), 5. Oturum (Session), 6. Sunum (Presentation - şifreleme, sıkıştırma, format), 7. Uygulama (Application - HTTP, FTP, SMTP, DNS).
- **Bilgi Güvenliğinin 3 Temel İlkesi (CIA Triad):** 
- **  - Gizlilik (Confidentiality):** Bilgiye sadece yetkili kişilerin erişebilmesi.
- **  - Bütünlük (Integrity):** Bilginin yetkisiz kişilerce değiştirilmemesi, doğruluğunun korunması.
- **  - Erişilebilirlik (Availability):** Yetkili kullanıcıların ihtiyaç duyduklarında bilgiye kesintisiz ulaşabilmesi.
- **Zararlı Yazılımlar (Malware):** 
- **  - Virüs:** Kendi kendine çalışamaz, bir çalıştırılabilir dosyaya veya programa bulaşarak kullanıcı etkisiyle yayılır.
- **  - Solucan (Worm):** İnsan müdahalesi olmadan ağ bağlantılarını kullanarak kendi kendini kopyalayıp yayılan bağımsız programdır.
- **  - Truva Atı (Trojan):** Masum veya faydalı bir yazılım gibi görünüp arka planda arka kapı (backdoor) açan zararlıdır.
- **  - Ransomware (Fidye Yazılımı):** Dosyaları şifreleyerek açılması için fidye talep eden zararlı yazılımdır.
- **Siber Saldırı Türleri:** Oltalama (Phishing - sahte e-posta/web sitesiyle kimlik avı), DoS / DDoS (Hizmeti aksatmak için sunucuyu sahte trafik bombardımanına tutma), Ortadaki Adam (Man-in-the-Middle).

---

## 📌 Ünite 7: Bilgisayar Programlama

**Ana Başlıklar:** Algoritma Kavramı, Akış Şemaları, Programlama Dilleri Düzeyleri, Derleyici vs Yorumlayıcı, Temel Programlama Mantığı

### ⚡ Sınav Odaklı Hap Bilgiler ve Kritik Notlar
- **Algoritma:** Bir problemin çözümü için adım adım tanımlanmış, sonlu, açık, net ve uygulanabilir işlem basamakları dizisidir.
- **Akış Şeması (Flowchart) Sembolleri:** Oval (Başla / Dur), Paralelkenar (Veri Girişi / Çıkışı), Dikdörtgen (İşlem / Hesaplama / Atama), Eşkenar Dörtgen / Baklava (Karar / Karşılaştırma / Koşul).
- **Dillerin Düzeyleri (İnsan Diline Yakınlık):** 
- **  - Düşük Düzey Diller:** Makine dili (0 ve 1'lerden oluşur, donanıma doğrudan bağlıdır) ve Assembly dili (sembolik kısaltmalar: MOV, ADD).
- **  - Orta Düzey Diller:** C dili (hem sistem programlama hem kullanıcı uygulamaları için elverişlidir).
- **  - Yüksek Düzey Diller:** İnsan diline çok yakın, donanımdan bağımsız dillerdir (Python, Java, C#, C++).
- **Derleyici (Compiler) vs Yorumlayıcı (Interpreter):** 
- **  - Derleyici:** Kaynak kodun tamamını tek seferde makine diline çevirir ve çalıştırılabilir bir dosya (.exe vb.) oluşturur (C, C++, Go). Kod derlendikten sonra çok hızlı çalışır.
- **  - Yorumlayıcı:** Kaynak kodları satır satır okur, anında makine diline çevirip çalıştırır (Python, JavaScript, PHP). Hata ayıklama kolaydır ancak çalışma hızı genellikle derlenen dillere göre yavaştır.
- **Temel Programlama Yapıları:** Değişkenler (int, float, string, boolean), Koşul Blokları (if-else, switch-case), Döngüler (for, while - belirli işlemi tekrar ettirme), Fonksiyonlar/Metotlar (kodun tekrar kullanılabilir modüllere ayrılması).
- **Nesne Yönelimli Programlama (OOP) Temel Kavramları:** Sınıf (Class - şablon), Nesne (Object - sınıftan türetilen somut örnek), Kapsülleme (Encapsulation), Kalıtım (Inheritance - miras alma), Çok Biçimlilik (Polymorphism).

---

## 📌 Ünite 8: Bilişim Teknolojilerinde Yeni Yönelimler

**Ana Başlıklar:** Endüstri 4.0, Yapay Zeka ve Makine Öğrenmesi, Büyük Veri (5V), Nesnelerin İnterneti (IoT), Blokzincir

### ⚡ Sınav Odaklı Hap Bilgiler ve Kritik Notlar
- **Sanayi Devrimleri:** Endüstri 1.0 (Buhar makinesi ve mekanizasyon), Endüstri 2.0 (Elektrik enerjisi ve seri üretim bantları), Endüstri 3.0 (Elektronik, bilgisayarlar ve otomasyon), Endüstri 4.0 (Siber-fiziksel sistemler, akıllı fabrikalar, IoT, yapay zeka).
- **Yapay Zeka (Artificial Intelligence - AI):** İnsan zekasına özgü algılama, öğrenme, akıl yürütme ve problem çözme gibi işlevleri bilgisayarların gerçekleştirmesidir. Alan Turing (1950 - Turing Testi).
- **Makine Öğrenmesi (Machine Learning) Türleri:** 
- **  - Denetimli Öğrenme (Supervised Learning):** Etiketli veriler kullanılarak sınıflandırma veya regresyon yapılması.
- **  - Denetimsiz Öğrenme (Unsupervised Learning):** Etiketsiz veriler arasındaki gizli örüntülerin ve kümelerin bulunması (Kümeleme).
- **  - Pekiştirmeli Öğrenme (Reinforcement Learning):** Ödül ve ceza mekanizmasıyla ajanın çevreyle etkileşime girerek en uygun kararları öğrenmesi.
- **Büyük Veri (Big Data) 5V Bileşeni:** Volume (Hacim / Boyut), Velocity (Hız / Veri üretim hızı), Variety (Çeşitlilik / Metin, ses, video), Veracity (Doğruluk / Güvenilirlik), Value (Değer / İş zekasına dönüşme).
- **Nesnelerin İnterneti (IoT - Internet of Things):** Fiziksel nesnelerin (sensörler, ev aletleri, araçlar) internet üzerinden birbirleriyle ve merkezi sistemlerle veri alışverişi yapabilmesidir. Kavramı ilk kez 1999'da Kevin Ashton kullanmıştır.
- **Blokzincir (Blockchain):** Dağıtık, merkeziyetsiz, şifrelenmiş ve değiştirilemez bir dijital defter teknolojisidir. İlk olarak Bitcoin ile 2008'de 'Satoshi Nakamoto' rumuzlu kişi/grup tarafından ortaya atılmıştır. Veriler bloklar halinde kriptografik özetlerle (hash) birbirine zincirlenir.
- **Genişletilmiş Gerçeklik:** Sanal Gerçeklik (VR - tamamen sanal bir ortama girme), Artırılmış Gerçeklik (AR - gerçek dünya görüntüsünün üzerine dijital nesneler bindirme, örn: Pokemon Go), Karma Gerçeklik (MR).

---

## 🎯 Final İçin 1 - 4. Üniteler Hızlı Vize Hatırlatıcıları

### 🔹 Ünite 1: Bilişim Teknolojilerinin Gelişimi
- DIKW Piramidi: Veri (Data - işlenmemiş ham gerçekler) -> Enformasyon (Information - anlamlandırılmış veri) -> Bilgi (Knowledge - deneyim ve bağlamla harmanlanmış enformasyon) -> Bilgelik (Wisdom - bilgiyi doğru ve etik kullanma yetisi).
- İlk Mekanik Hesap Makineleri: Blaise Pascal (Pascaline - sadece toplama ve çıkarma), Gottfried Wilhelm Leibniz (Leibniz Çarkı - 4 işlem yapabilen).
- Modern Bilgisayarın Babası: Charles Babbage (Fark Motoru ve Analitik Motor). Analitik Motor için ilk algoritmayı yazan Ada Lovelace ise 'İlk Bilgisayar Programcısı' kabul edilir.
- Herman Hollerith: 1890 ABD nüfus sayımı için delikli kart sistemini geliştirdi ve daha sonra IBM'e dönüşecek şirketin temelini attı.

### 🔹 Ünite 2: Bilgisayar Donanımı
- Von Neumann Mimarisi 4 Temel Bölüm: Giriş Birimleri, Çıkış Birimleri, Merkezi İşlem Birimi (CPU) ve Bellek (Memory).
- CPU Bileşenleri: 1. Aritmetik ve Mantık Birimi (ALU - matematiksel ve mantıksal işlemleri yapar), 2. Denetim Birimi (Control Unit / CU - komutları çözer, diğer birimleri senkronize yönetir), 3. Yazmaçlar (Registers - CPU içindeki en küçük ve en hızlı geçici depolama alanları).
- Saat Hızı (Clock Speed): İşlemcinin saniyede yaptığı döngü sayısını ifade eder (Hertz/GHz). 1 GHz = saniyede 1 milyar çevrim.
- Bellek Hiyerarşisi (Hız ve Maliyet Sıralaması: En Hızlı ve En Pahalıdan En Yavaşa): Yazmaçlar (Registers) -> L1 Önbellek -> L2 Önbellek -> L3 Önbellek -> RAM -> SSD / Sabit Disk (HDD) -> Optik/Manyetik Teyp.

### 🔹 Ünite 3: İşletim Sistemleri ve Dosya Yönetimi
- İşletim Sistemi (OS): Kullanıcı ve uygulama programları ile bilgisayar donanımı arasındaki iletişimi sağlayan, donanım kaynaklarını yöneten temel sistem yazılımıdır.
- İşletim Sisteminin 4 Temel Yönetim Fonksiyonu: 1. İşlemci Yönetimi (Process Management / Görev Zamanlama), 2. Bellek Yönetimi (RAM tahsisi ve Sanal Bellek), 3. Aygıt (Giriş/Çıkış) Yönetimi, 4. Dosya ve Depolama Yönetimi.
- Çekirdek (Kernel): İşletim sisteminin kalbidir; doğrudan donanım seviyesinde çalışır ve bellek, CPU ve aygıt erişimlerini yönetir.
- Kabuk (Shell) ve Arayüz: Kullanıcının komut girdiği arayüzdür. CLI (Komut Satırı Arayüzü - terminal/bash/cmd) ve GUI (Grafiksel Kullanıcı Arayüzü - pencereler, ikonlar).

### 🔹 Ünite 4: Uygulama Yazılımları
- Yazılım Türleri: Sistem Yazılımları (İşletim sistemleri, aygıt sürücüleri, BIOS) ve Uygulama Yazılımları (Kullanıcının belirli bir işi yapmasını sağlayan yazılımlar: Word, Excel, Photoshop, ERP).
- Kelime İşlemci (Word Processors): Metin oluşturma, düzenleme, biçimlendirme ve raporlama (MS Word, Google Docs, LibreOffice Writer).
- Hesap Tablosu (Spreadsheet): Satır ve sütunlardan oluşan hücreler yapısı. Hücre adresi sütun harfi ve satır numarasından oluşur (örn: B4). Formüller daima '=' (eşittir) işareti ile başlar (MS Excel, Google Sheets, LibreOffice Calc).
- Sunum Yazılımları: Slaytlar, animasyonlar ve görsel anlatım (PowerPoint, Keynote, Prezi).

