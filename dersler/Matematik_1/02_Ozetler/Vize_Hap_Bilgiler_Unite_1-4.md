# 📘 MATEMATİK I (MAT105U) - Vize Hap Bilgiler Rehberi (1 - 4. Üniteler)

Bu rehber, Anadolu Üniversitesi Açıköğretim Fakültesi (AÖF) Vize sınavı için 1'den 4. üniteye kadar olan tüm kritik formülleri, grafik yorumlarını, model yaklaşımlarını ve sınav hap bilgilerini içerir.

---

## 📌 Ünite 1: Kümeler ve Sayılar

**Ana Başlıklar:** Kümelerde İşlemler, Alt Küme ve Özalt Küme, De Morgan Kuralları, Sayı Kümeleri, Mutlak Değer

### ⚡ Sınav Odaklı Hap Bilgiler ve Kritik Notlar
- **Alt Küme Sayısı Formülü:** n elemanlı bir kümenin alt küme sayısı 2^n, kendisi hariç özalt küme sayısı ise 2^n - 1'dir. Örn: 4 elemanlı bir kümenin 2^4 = 16 alt kümesi, 15 özalt kümesi vardır.
- **Birleşim ve Kesişim Eleman Sayısı:** s(A ∪ B) = s(A) + s(B) - s(A ∩ B). Eğer A ve B ayrık kümeler ise (kesişimleri boş küme) s(A ∪ B) = s(A) + s(B)'dir.
- **De Morgan Kuralları:** (A ∪ B)' = A' ∩ B' ve (A ∩ B)' = A' ∪ B'. Birleşimin tümleyeni tümleyenlerin kesişimine eşittir.
- **Sayı Kümeleri Hiyerarşisi:** N (Doğal Sayılar: {0,1,2,...}) ⊂ Z (Tam Sayılar: {...,-2,-1,0,1,2,...}) ⊂ Q (Rasyonel Sayılar: a/b şeklinde yazılabilenler) ⊂ R (Gerçel/Reel Sayılar).
- **İrrasyonel Sayılar (Q' veya I):** a/b şeklinde yazılamayan, virgülden sonra devretmeksizin sonsuza giden sayılardır. √2, √3, pi (π ≈ 3.14159) ve e (≈ 2.71828) en klasik irrasyonel sayılardır.
- **Mutlak Değer Özellikleri:** 
- **  - Her x gerçel sayısı için |x| ≥ 0'dır.:**   - Her x gerçel sayısı için |x| ≥ 0'dır.
- **  - |-x| = |x| ve |x * y| = |x| * |y|.:**   - |-x| = |x| ve |x * y| = |x| * |y|.
- **  - Üçgen Eşitsizliği:** |x + y| ≤ |x| + |y|.
- **  - a > 0 olmak üzere; |x| < a ise -a < x < a'dır. |x| > a ise x > a veya x < -a'dır.:**   - a > 0 olmak üzere; |x| < a ise -a < x < a'dır. |x| > a ise x > a veya x < -a'dır.

---

## 📌 Ünite 2: Fonksiyonlar

**Ana Başlıklar:** Fonksiyon Tanımı ve Kümeleri, Bire-Bir ve Örtenlik, Ters Fonksiyon, Bileşke İşlemi, Tek ve Çift Fonksiyonlar

### ⚡ Sınav Odaklı Hap Bilgiler ve Kritik Notlar
- **Fonksiyon Olma Şartı:** f: A -> B için tanım kümesi A'nın her elemanı değer kümesi B'den yalnız bir elemanla eşleşmelidir. A'da açıkta eleman kalamaz, ancak B'de kalabilir.
- **Bire-Bir (Injective) Fonksiyon:** Farklı elemanların görüntüleri de farklı olmalıdır (x1 ≠ x2 => f(x1) ≠ f(x2)). Grafiğe çizilen yatay doğrular grafiği en fazla bir noktada kesmelidir (Yatay Doğru Testi).
- **Örten (Surjective) Fonksiyon:** Değer kümesinde açıkta hiç eleman kalmamasıdır (f(A) = B). Değer kümesinde açıkta eleman kalırsa fonksiyona 'İçine Fonksiyon' denir.
- **Ters Fonksiyon (f^-1):** Bir fonksiyonun tersinin olabilmesi için fonksiyonun MUTLAKA hem BİRE-BİR hem de ÖRTEN (Biyektif) olması şarttır! y = f(x) <=> x = f^-1(y). Bir fonksiyonun grafiği ile tersinin grafiği y = x doğrusuna göre simetriktir.
- **Doğrusal Fonksiyonun Tersi:** f(x) = ax + b ise f^-1(x) = (x - b) / a'dır. Örn: f(x) = 2x + 6 => f^-1(x) = (x - 6) / 2.
- **Bileşke Fonksiyon:** (f o g)(x) = f(g(x)). Bileşke işleminin değişme özelliği yoktur: (f o g) ≠ (g o f). Ancak birleşme özelliği vardır: f o (g o h) = (f o g) o h.
- **Çift Fonksiyon:** f(-x) = f(x) olan fonksiyondur. Grafiği y eksenine göre simetriktir (Örn: f(x) = x^2, f(x) = cos x, f(x) = |x|).
- **Tek Fonksiyon:** f(-x) = -f(x) olan fonksiyondur. Grafiği orijine (0,0) göre simetriktir (Örn: f(x) = x^3, f(x) = sin x, f(x) = x).

---

## 📌 Ünite 3: Polinom Fonksiyonlar

**Ana Başlıklar:** Doğrusal Fonksiyonlar ve Eğim, Paralel ve Dik Doğrular, İkinci Dereceden Fonksiyonlar (Parabol), Tepe Noktası ve Diskriminant

### ⚡ Sınav Odaklı Hap Bilgiler ve Kritik Notlar
- **Doğrunun Eğimi (m):** A(x1, y1) ve B(x2, y2) noktalarından geçen doğrunun eğimi m = (y2 - y1) / (x2 - x1)'dir. y = mx + n denkleminde x'in katsayısı m eğimdir, n ise doğrunun y eksenini kestiği noktadır.
- **Paralel Doğrular:** Eğilimleri birbirine eşittir (d1 // d2 => m1 = m2).
- **Dik Doğrular:** Birbirine dik iki doğrunun eğimleri çarpımı -1'dir (d1 ⊥ d2 => m1 * m2 = -1 => m2 = -1 / m1).
- **İkinci Dereceden Fonksiyon (Parabol):** f(x) = ax^2 + bx + c (a ≠ 0).
- **  - a > 0 ise kollar YUKARI doğrudur ve fonksiyon tepe noktasında en küçük (MİNİMUM) değerini alır.:**   - a > 0 ise kollar YUKARI doğrudur ve fonksiyon tepe noktasında en küçük (MİNİMUM) değerini alır.
- **  - a < 0 ise kollar AŞAĞI doğrudur ve fonksiyon tepe noktasında en büyük (MAKSİMUM) değerini alır.:**   - a < 0 ise kollar AŞAĞI doğrudur ve fonksiyon tepe noktasında en büyük (MAKSİMUM) değerini alır.
- **Tepe Noktası Koordinatları T(r, k):** 
- **  - r = -b / (2a) (Simetri ekseni x = r doğrusudur).:**   - r = -b / (2a) (Simetri ekseni x = r doğrusudur).
- **  - k = f(r) = (4ac - b^2) / (4a) (Fonksiyonun alabileceği en büyük veya en küçük değerdir).:**   - k = f(r) = (4ac - b^2) / (4a) (Fonksiyonun alabileceği en büyük veya en küçük değerdir).
- **Diskriminant (Δ = b^2 - 4ac):** 
- **  - Δ > 0 ise parabol x eksenini iki farklı noktada keser (2 gerçel kök vardır).:**   - Δ > 0 ise parabol x eksenini iki farklı noktada keser (2 gerçel kök vardır).
- **  - Δ = 0 ise parabol x eksenine teğettir (çakışık/çift katlı tek gerçel kök vardır:** x1 = x2 = -b / (2a)).
- **  - Δ < 0 ise parabol x eksenini hiç kesmez (gerçel kök yoktur).:**   - Δ < 0 ise parabol x eksenini hiç kesmez (gerçel kök yoktur).
- **Kökler Bağıntıları:** Kökler toplamı x1 + x2 = -b / a, Kökler çarpımı x1 * x2 = c / a.

---

## 📌 Ünite 4: Üstel ve Logaritmik Fonksiyonlar

**Ana Başlıklar:** Üstel Fonksiyon Tanımı, Doğal Üstel Fonksiyon (e^x), Logaritma Tanımı ve Özellikleri, Doğal Logaritma (ln x)

### ⚡ Sınav Odaklı Hap Bilgiler ve Kritik Notlar
- **Üstel Fonksiyon:** f(x) = a^x (a > 0 ve a ≠ 1).
- **  - a > 1 ise fonksiyon artandır.:**   - a > 1 ise fonksiyon artandır.
- **  - 0 < a < 1 ise fonksiyon azalandır.:**   - 0 < a < 1 ise fonksiyon azalandır.
- **  - Tanım kümesi tüm gerçel sayılar (-∞, +∞), görüntü kümesi pozitif gerçel sayılardır (0, +∞). Grafiği daima (0, 1) noktasından geçer.:**   - Tanım kümesi tüm gerçel sayılar (-∞, +∞), görüntü kümesi pozitif gerçel sayılardır (0, +∞). Grafiği daima (0, 1) noktasından geçer.
- **Doğal Üstel Fonksiyon:** Tabanı Euler sayısı (e ≈ 2.71828) olan f(x) = e^x fonksiyonudur.
- **Logaritma Fonksiyonu:** Üstel fonksiyonun tersidir. y = log_a(x) <=> a^y = x (x > 0, a > 0, a ≠ 1). Logaritması alınan sayı x daima KESİNLİKLE pozitif (> 0) olmalıdır!
- **Temel Logaritma Kuralları:** 
- **  - log_a(1) = 0 ve log_a(a) = 1.:**   - log_a(1) = 0 ve log_a(a) = 1.
- **  - log_a(x * y) = log_a(x) + log_a(y) (Çarpımın logaritması toplamdır).:**   - log_a(x * y) = log_a(x) + log_a(y) (Çarpımın logaritması toplamdır).
- **  - log_a(x / y) = log_a(x) - log_a(y) (Bölümün logaritması farktır).:**   - log_a(x / y) = log_a(x) - log_a(y) (Bölümün logaritması farktır).
- **  - log_a(x^k) = k * log_a(x) (Kuvvet başa katsayı olarak düşer).:**   - log_a(x^k) = k * log_a(x) (Kuvvet başa katsayı olarak düşer).
- **  - Taban Değiştirme Kuralı:** log_a(b) = ln(b) / ln(a) = log(b) / log(a).
- **Doğal Logaritma (ln):** Tabanı e olan logaritmadır. ln(x) = log_e(x). ln(e) = 1, ln(1) = 0, ln(e^k) = k.

---

