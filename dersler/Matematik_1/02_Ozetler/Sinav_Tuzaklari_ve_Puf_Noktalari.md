# ⚠️ MATEMATİK I (MAT105U) - AÖF Sınav Komisyonunun 10 Klasik Tuzağı ve Püf Noktaları

AÖF sınav komisyonunun öğrencileri düşürmek için şıklara özellikle yerleştirdiği çeldiriciler, kavram karmaşaları ve formül tuzakları:

---

## 🚨 Tuzak #1: Kümelerde Alt Küme ile Özalt Küme Sayısı Karışıklığı

❌ **Öğrencilerin Düştüğü Hata / Yanıltıcı Çeldirici:**
Özalt küme sorulduğunda doğrudan 2^n hesaplayıp işaretlemek.

✅ **İşin Doğrusu ve Sınavda Kurtaracak Püf Nokta:**
Alt küme sayısı 2^n'dir; ancak ÖZALT KÜME kümenin kendisi hariç tutulduğu için 2^n - 1'dir. 1 çıkarmayı kesinlikle unutmamalısın.

💡 **Akılda Kalıcı Taktik:** Özalt küme = 2^n - 1 (Kendini çıkar).

---

## 🚨 Tuzak #2: Rasyonel Sayı ile İrrasyonel Sayı Ayrımı (Karekök Tuzağı)

❌ **Öğrencilerin Düştüğü Hata / Yanıltıcı Çeldirici:**
Karekök içindeki her sayının irrasyonel olduğunu düşünmek (örn: √9 veya √16).

✅ **İşin Doğrusu ve Sınavda Kurtaracak Püf Nokta:**
Kök dışına tam çıkan sayılar rasyoneldir (√9 = 3 rasyoneldir). Kök dışına çıkamayan sayılar (√2, √3, √5) ve pi (π), e sayıları irrasyoneldir.

💡 **Akılda Kalıcı Taktik:** Kökten tam çıkıyorsa Rasyonel (Q), çıkamıyorsa İrrasyonel (Q').

---

## 🚨 Tuzak #3: Ters Fonksiyon Varlık Şartı

❌ **Öğrencilerin Düştüğü Hata / Yanıltıcı Çeldirici:**
Her fonksiyonun tersinin alınabileceğini zannetmek.

✅ **İşin Doğrusu ve Sınavda Kurtaracak Püf Nokta:**
Bir fonksiyonun tersinin var olabilmesi için fonksiyonun MUTLAKA hem BİRE-BİR hem de ÖRTEN olması gerekir. İkisinden biri eksikse ters fonksiyon tanımlanamaz.

💡 **Akılda Kalıcı Taktik:** Ters fonksiyon = Bire-bir VE Örten (Biyektif) olmak zorundadır.

---

## 🚨 Tuzak #4: Parabolde Tepe Noktasının Maksimum mu Minimum mu Olduğu

❌ **Öğrencilerin Düştüğü Hata / Yanıltıcı Çeldirici:**
a katsayısı pozitifken fonksiyonun maksimum değer aldığını sanmak.

✅ **İşin Doğrusu ve Sınavda Kurtaracak Püf Nokta:**
f(x) = ax^2 + bx + c fonksiyonunda a > 0 ise kollar YUKARI açılır ve çukurun dibi MİNİMUM değerdir. a < 0 ise kollar AŞAĞI iner ve tepe noktası MAKSİMUM değerdir.

💡 **Akılda Kalıcı Taktik:** a > 0 => Gülen yüz (En dip = Minimum); a < 0 => Üzgün yüz (Zirve = Maksimum).

---

## 🚨 Tuzak #5: Bir Doğruya Dik Olan Doğrunun Eğimi

❌ **Öğrencilerin Düştüğü Hata / Yanıltıcı Çeldirici:**
Dik doğrunun eğimini bulurken sadece işaretini değiştirmek (m yerine -m almak).

✅ **İşin Doğrusu ve Sınavda Kurtaracak Püf Nokta:**
Dik iki doğrunun eğimleri çarpımı -1'dir (m1 * m2 = -1). Dolayısıyla dik doğrunun eğimi hem ters çevrilir hem işareti değişir: m2 = -1 / m1.

💡 **Akılda Kalıcı Taktik:** Örn: m1 = 2 ise dik doğrunun eğimi -1/2'dir (sadece -2 değil!).

---

## 🚨 Tuzak #6: Logaritmanın Tanım Kümesi Pozitiflik Şartı

❌ **Öğrencilerin Düştüğü Hata / Yanıltıcı Çeldirici:**
log_a(x) ifadesinde x'in sıfır veya negatif olabileceğini varsaymak.

✅ **İşin Doğrusu ve Sınavda Kurtaracak Püf Nokta:**
Logaritması alınan sayı daima sıfırdan KESİNLİKLE BÜYÜK olmalıdır (x > 0). Taban da pozitif ve 1'den farklı olmalıdır (a > 0, a ≠ 1). log(0) tanımsızdır, negatifin logaritması reel sayılarda yoktur.

💡 **Akılda Kalıcı Taktik:** Logaritmanın içi daima > 0 olmak zorundadır.

---

## 🚨 Tuzak #7: 0/0 Belirsizliğinde L'Hopital Kuralı Uygulaması

❌ **Öğrencilerin Düştüğü Hata / Yanıltıcı Çeldirici:**
Bölümün türev kuralını [(f'g - fg')/g^2] uygulamaya çalışmak.

✅ **İşin Doğrusu ve Sınavda Kurtaracak Püf Nokta:**
L'Hopital kuralında bölümün genel türevi ALINMAZ! Sadece payın türevi alınıp paya [f'(x)], paydanın türevi alınıp paydaya [g'(x)] yazılır.

💡 **Akılda Kalıcı Taktik:** L'Hopital = Payın türevi / Paydanın türevi.

---

## 🚨 Tuzak #8: Matris Çarpımı Değişme Özelliği Yanılgısı

❌ **Öğrencilerin Düştüğü Hata / Yanıltıcı Çeldirici:**
Sayılar gibi matrislerde de A * B = B * A olduğunu düşünmek.

✅ **İşin Doğrusu ve Sınavda Kurtaracak Püf Nokta:**
Matris çarpımında kural olarak DEĞİŞME ÖZELLİĞİ YOKTUR (A * B ≠ B * A). Çoğu zaman biri tanımlıyken diğeri boyut uyumsuzluğundan hesaplanamaz bile.

💡 **Akılda Kalıcı Taktik:** A * B ile B * A matrislerde eşit DEĞİLDİR!

---

## 🚨 Tuzak #9: Ters Matris Varlık Şartı (Determinant Sıfır Olma Durumu)

❌ **Öğrencilerin Düştüğü Hata / Yanıltıcı Çeldirici:**
Her kare matrisin tersinin olduğunu varsaymak.

✅ **İşin Doğrusu ve Sınavda Kurtaracak Püf Nokta:**
Bir A matrisinin tersinin (A^-1) var olabilmesi için det(A) ≠ 0 olmalıdır. Determinantı 0 olan matrislere 'Tekil (Singüler)' matris denir ve tersleri YOKTUR.

💡 **Akılda Kalıcı Taktik:** det(A) = 0 ise ters matris YOKTUR.

---

## 🚨 Tuzak #10: Kâr Maksimizasyonunda Türev Alma Tuzağı

❌ **Öğrencilerin Düştüğü Hata / Yanıltıcı Çeldirici:**
Kârı bulmak için sadece fiyatı veya maliyeti sıfıra eşitlemek.

✅ **İşin Doğrusu ve Sınavda Kurtaracak Püf Nokta:**
Kârı maksimize eden miktar; Marjinal Hasılatın Marjinal Maliyete eşit olduğu (MR = MC) üretim düzeyidir. TR'nin türevi ile TC'nin türevi birbirine eşitlenir.

💡 **Akılda Kalıcı Taktik:** Maksimum Kâr = MR'yi bul, MC'ye eşitle (MR = MC).

---

