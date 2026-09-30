# 📘 BİLİŞİM TEKNOLOJİLERİ (YBS101U) - Vize Hap Bilgiler Rehberi (1 - 4. Üniteler)

Bu rehber, Anadolu Üniversitesi Açıköğretim Fakültesi (AÖF) Vize sınavı için 1'den 4. üniteye kadar olan tüm kritik formülleri, grafik yorumlarını, model yaklaşımlarını ve sınav hap bilgilerini içerir.

---

## 📌 Ünite 1: Bilişim Teknolojilerinin Gelişimi

**Ana Başlıklar:** Tarihsel Süreç, Bilgisayar Kuşakları, DIKW Hiyerarşisi, Moore Yasası, Önemli Öncüler

### ⚡ Sınav Odaklı Hap Bilgiler ve Kritik Notlar
- **DIKW Piramidi:** Veri (Data - işlenmemiş ham gerçekler) -> Enformasyon (Information - anlamlandırılmış veri) -> Bilgi (Knowledge - deneyim ve bağlamla harmanlanmış enformasyon) -> Bilgelik (Wisdom - bilgiyi doğru ve etik kullanma yetisi).
- **İlk Mekanik Hesap Makineleri:** Blaise Pascal (Pascaline - sadece toplama ve çıkarma), Gottfried Wilhelm Leibniz (Leibniz Çarkı - 4 işlem yapabilen).
- **Modern Bilgisayarın Babası:** Charles Babbage (Fark Motoru ve Analitik Motor). Analitik Motor için ilk algoritmayı yazan Ada Lovelace ise 'İlk Bilgisayar Programcısı' kabul edilir.
- **Herman Hollerith:** 1890 ABD nüfus sayımı için delikli kart sistemini geliştirdi ve daha sonra IBM'e dönüşecek şirketin temelini attı.
- **ENIAC (1946):** J. Presper Eckert ve John Mauchly tarafından geliştirilen, ilk genel amaçlı, tamamen elektronik, ondalık tabanlı devasa bilgisayardır (Vakum tüpleri kullanılmıştır).
- **EDVAC ve Von Neumann:** John von Neumann tarafından ortaya atılan 'Saklı Program' mimarisini (program ve verinin aynı bellekte tutulması) kullanan ilk tasarımdır.
- **1. Kuşak (1940-1956):** Vakum (Elektron) tüpleri kullanıldı. Çok büyük, çok ısı üreten, sık arızalanan ve makine diliyle programlanan makinelerdir.
- **2. Kuşak (1956-1963):** Transistörün icadı (1947, Bell Labs - Shockley, Bardeen, Brattain). Bilgisayarlar küçüldü, hızlandı ve Assembly/FORTRAN gibi diller doğdu.
- **3. Kuşak (1964-1971):** Entegre Devreler (Mikroçipler - Jack Kilby ve Robert Noyce). Klavye, monitör ve işletim sistemleri kullanılmaya başlandı.
- **4. Kuşak (1971-Günümüz):** Mikroişlemciler (Intel 4004 - 1971). Tek bir silikon çip üzerine tüm CPU yerleştirildi; kişisel bilgisayarlar (PC) devrimi başladı.
- **5. Kuşak (Gelecek/Günümüz):** Yapay zeka, paralel işlemciler, kuantum hesaplama ve doğal dil işleme.
- **Moore Yasası:** Intel'in kurucularından Gordon Moore'a göre bir mikroçip üzerindeki transistör sayısı yaklaşık her 18-24 ayda bir iki katına çıkacaktır.

---

## 📌 Ünite 2: Bilgisayar Donanımı

**Ana Başlıklar:** Von Neumann Mimarisi, Merkezi İşlem Birimi (CPU), Bellek Hiyerarşisi, Giriş-Çıkış Birimleri, Veri Birimleri

### ⚡ Sınav Odaklı Hap Bilgiler ve Kritik Notlar
- **Von Neumann Mimarisi 4 Temel Bölüm:** Giriş Birimleri, Çıkış Birimleri, Merkezi İşlem Birimi (CPU) ve Bellek (Memory).
- **CPU Bileşenleri:** 1. Aritmetik ve Mantık Birimi (ALU - matematiksel ve mantıksal işlemleri yapar), 2. Denetim Birimi (Control Unit / CU - komutları çözer, diğer birimleri senkronize yönetir), 3. Yazmaçlar (Registers - CPU içindeki en küçük ve en hızlı geçici depolama alanları).
- **Saat Hızı (Clock Speed):** İşlemcinin saniyede yaptığı döngü sayısını ifade eder (Hertz/GHz). 1 GHz = saniyede 1 milyar çevrim.
- **Bellek Hiyerarşisi (Hız ve Maliyet Sıralaması:** En Hızlı ve En Pahalıdan En Yavaşa): Yazmaçlar (Registers) -> L1 Önbellek -> L2 Önbellek -> L3 Önbellek -> RAM -> SSD / Sabit Disk (HDD) -> Optik/Manyetik Teyp.
- **RAM (Random Access Memory):** Geçici (uçucu/volatile) ana bellektir. Elektrik kesildiğinde veriler silinir. DRAM (Dinamik - yenileme gerekir, ucuz, ana RAM) ve SRAM (Statik - yenileme gerekmez, çok hızlı, önbellek olarak kullanılır).
- **ROM (Read Only Memory):** Kalıcı (uçucu olmayan/non-volatile) bellektir. Fabrika çıkışı BIOS/UEFI yazılımını tutar. Çeşitleri: PROM (bir kez programlanır), EPROM (morötesi ışıkla silinir), EEPROM (elektriksel olarak silinip yazılır, Flash bellekler bu yapıdadır).
- **Giriş Birimleri:** Klavye, fare, mikrofon, optik okuyucu, barkod okuyucu, tarayıcı.
- **Çıkış Birimleri:** Monitör, yazıcı, hoparlör, projeksiyon.
- **Hem Giriş Hem Çıkış Birimleri:** Dokunmatik ekranlar (Touchscreen), modemler, ağ kartları (NIC), ses kartları.
- **Veri Ölçü Birimleri (İkili Sistem - 2^10 = 1024 kuralı):** 1 Byte = 8 Bit. 1 Kilobyte (KB) = 1024 Byte. 1 Megabyte (MB) = 1024 KB. 1 Gigabyte (GB) = 1024 MB. 1 Terabyte (TB) = 1024 GB. 1 Petabyte (PB) = 1024 TB.

---

## 📌 Ünite 3: İşletim Sistemleri ve Dosya Yönetimi

**Ana Başlıklar:** İşletim Sisteminin Görevleri, Çekirdek (Kernel) ve Kabuk (Shell), İşletim Sistemi Türleri, Dosya Sistemleri

### ⚡ Sınav Odaklı Hap Bilgiler ve Kritik Notlar
- **İşletim Sistemi (OS):** Kullanıcı ve uygulama programları ile bilgisayar donanımı arasındaki iletişimi sağlayan, donanım kaynaklarını yöneten temel sistem yazılımıdır.
- **İşletim Sisteminin 4 Temel Yönetim Fonksiyonu:** 1. İşlemci Yönetimi (Process Management / Görev Zamanlama), 2. Bellek Yönetimi (RAM tahsisi ve Sanal Bellek), 3. Aygıt (Giriş/Çıkış) Yönetimi, 4. Dosya ve Depolama Yönetimi.
- **Çekirdek (Kernel):** İşletim sisteminin kalbidir; doğrudan donanım seviyesinde çalışır ve bellek, CPU ve aygıt erişimlerini yönetir.
- **Kabuk (Shell) ve Arayüz:** Kullanıcının komut girdiği arayüzdür. CLI (Komut Satırı Arayüzü - terminal/bash/cmd) ve GUI (Grafiksel Kullanıcı Arayüzü - pencereler, ikonlar).
- **Sanal Bellek (Virtual Memory):** RAM yetersiz kaldığında sabit diskin (paging file / swap alanı) bir bölümünün geçici olarak RAM gibi kullanılması tekniğidir.
- **İşletim Sistemi Sınıfları:** Tek Kullanıcılı - Tek Görevli (MS-DOS), Tek Kullanıcılı - Çok Görevli (Windows 10/11, macOS), Çok Kullanıcılı - Çok Görevli (Unix, Linux sunucular), Gerçek Zamanlı (RTOS - savunma sanayii, otomotiv, robotik).
- **Açık Kaynak Kodlu İşletim Sistemleri:** Linux (1991'de Linus Torvalds tarafından geliştirilen çekirdek üzerine kuruludur). Dağıtımlar: Ubuntu, Fedora, Debian, Pardus (TÜBİTAK).
- **Dosya Sistemleri:** FAT32 (maksimum 4 GB tek dosya boyutu sınırı vardır), NTFS (Windows standartı, güvenlik izinleri, şifreleme ve günlükleme destekler), exFAT (USB bellekler için evrensel), ext4 (modern Linux), APFS (Apple Dosya Sistemi).
- **Dosya Yolları:** Mutlak Yol (Absolute Path - Kök dizinden başlar: 'C:\Users\Belgeler\rapor.docx'), Göreceli Yol (Relative Path - bulunulan dizinden başlar: '..\rapor.docx').

---

## 📌 Ünite 4: Uygulama Yazılımları

**Ana Başlıklar:** Yazılım Türleri, Ofis Yazılımları, Yazılım Lisanslama Türleri, SaaS ve Bulut Uygulamaları

### ⚡ Sınav Odaklı Hap Bilgiler ve Kritik Notlar
- **Yazılım Türleri:** Sistem Yazılımları (İşletim sistemleri, aygıt sürücüleri, BIOS) ve Uygulama Yazılımları (Kullanıcının belirli bir işi yapmasını sağlayan yazılımlar: Word, Excel, Photoshop, ERP).
- **Kelime İşlemci (Word Processors):** Metin oluşturma, düzenleme, biçimlendirme ve raporlama (MS Word, Google Docs, LibreOffice Writer).
- **Hesap Tablosu (Spreadsheet):** Satır ve sütunlardan oluşan hücreler yapısı. Hücre adresi sütun harfi ve satır numarasından oluşur (örn: B4). Formüller daima '=' (eşittir) işareti ile başlar (MS Excel, Google Sheets, LibreOffice Calc).
- **Sunum Yazılımları:** Slaytlar, animasyonlar ve görsel anlatım (PowerPoint, Keynote, Prezi).
- **Veritabanı Yönetim Sistemleri (DBMS):** Büyük verilerin yapısal olarak saklanması ve SQL ile sorgulanması (MS Access, Oracle, MySQL, PostgreSQL).
- **Yazılım Lisanslama Modelleri:** 
- **  - Ticari (Proprietary) Yazılım:** Telif hakkı saklıdır, kaynak kod kapalıdır, ücret ödenerek kullanım lisansı alınır (MS Windows, Photoshop).
- **  - Açık Kaynak Kodlu (Open Source):** Kaynak kodları herkese açıktır; incelenebilir, değiştirilebilir ve dağıtılabilir (Linux, LibreOffice, GIMP, Apache). GNU Genel Kamu Lisansı (GPL) yaygındır.
- **  - Paylaşılan Yazılım (Shareware):** Belirli bir süre (örneğin 30 gün) veya kısıtlı özellikle ücretsiz denenebilen, süre sonunda ücret talep eden yazılımlardır.
- **  - Ücretsiz Yazılım (Freeware):** Kullanımı tamamen ücretsiz olan ancak kaynak kodu kapalı olan yazılımlardır (Adobe Acrobat Reader).
- **  - Kamu Malı (Public Domain):** Telif hakkı süresi dolmuş veya bilinçli olarak kamuya bağışlanmış, hiçbir kısıtlaması olmayan yazılımlar.
- **SaaS (Software as a Service - Hizmet Olarak Yazılım):** Yazılımın bilgisayara kurulmadan doğrudan web tarayıcısı üzerinden bulut sunuculardan çalıştırılması modelidir (Office 365, Google Workspace, Canva).

---

