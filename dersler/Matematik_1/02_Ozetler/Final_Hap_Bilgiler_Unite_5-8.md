# 📗 MATEMATİK I (MAT105U) - Final Hap Bilgiler ve Kapsamlı Tekrar (5 - 8. Üniteler + Vize Özeti)

AÖF Dönem Sonu (Final) sınavında soruların yaklaşık %70'i (14 soru) 5-8. ünitelerden, %30'u (6 soru) 1-4. vize konularından gelir.

---

## 📌 Ünite 5: Limit, Süreklilik ve Türev

**Ana Başlıklar:** Limit Tanımı ve Özellikleri, 0/0 Belirsizliği ve L'Hopital, Süreklilik Şartları, Türev Tanımı ve Geometrik Anlamı, Temel Türev Alma Kuralları

### ⚡ Sınav Odaklı Hap Bilgiler ve Kritik Notlar
- **Limit Varlık Şartı:** Bir f(x) fonksiyonunun x = a noktasında limitinin olması için sağdan ve soldan limitlerinin birbirine eşit olması gerekir: lim_{x->a^+} f(x) = lim_{x->a^-} f(x) = L.
- **0/0 Belirsizliği ve L'Hopital Kuralı:** lim_{x->a} f(x)/g(x) işleminde 0/0 çıkarsa, pay ve paydanın ayrı ayrı türevi alınarak limit tekrar hesaplanır: lim [f'(x) / g'(x)].
- **Süreklilik Şartları (3 Şart Birlikte Sağlanmalı):** 1. f(a) tanımlı olmalıdır, 2. x -> a iken limit var olmalıdır, 3. lim_{x->a} f(x) = f(a) olmalıdır.
- **Türevin Geometrik Anlamı:** f'(x0), f(x) eğrisine x0 noktasında çizilen teğet doğrusunun eğimine eşittir (mt = f'(x0)).
- **Temel Türev Alma Kuralları:** 
- **  - Sabit sayının türevi sıfırdır:** (c)' = 0.
- **  - Kuvvet kuralı:** (x^n)' = n * x^(n-1). Örn: (x^3)' = 3x^2, (5x^4)' = 20x^3, (x)' = 1.
- **  - Çarpımın Türevi:** (f * g)' = f' * g + f * g'.
- **  - Bölümün Türevi:** (f / g)' = (f' * g - f * g') / (g^2).
- **  - Zincir Kuralı (Bileşke Türevi):** [f(g(x))]' = f'(g(x)) * g'(x).
- **  - Üstel ve Logaritmik Türevler:** (e^x)' = e^x, (e^(kx))' = k * e^(kx), (ln x)' = 1 / x, (ln(g(x)))' = g'(x) / g(x).

---

## 📌 Ünite 6: Matrisler ve Doğrusal Denklem Sistemleri

**Ana Başlıklar:** Matris Boyutu ve Türleri, Matris Çarpımı Kuralları, Determinant Hesaplama (2x2 ve 3x3), Ters Matris ve Cramer Kuralı

### ⚡ Sınav Odaklı Hap Bilgiler ve Kritik Notlar
- **Matris Boyutu:** m satır ve n sütundan oluşan tabloya m x n matris denir. Kare matriste satır ve sütun sayısı eşittir (m = n).
- **Matris Çarpımı Şartı:** A_(m x k) ile B_(k x n) çarpılabilir ve sonuç C_(m x n) boyutunda olur. Yani birinci matrisin SÜTUN sayısı, ikinci matrisin SATIR sayısına eşit olmak zorundadır! Matris çarpımında değişme özelliği yoktur: A * B ≠ B * A.
- **Birim Matris (I):** Asal köşegeni 1, diğer tüm elemanları 0 olan kare matristir. Her A matrisi için A * I = I * A = A'dır.
- **2x2 Determinant:** det |a b; c d| = a * d - b * c (Asal köşegen çarpımı eksi yedek köşegen çarpımı).
- **Determinant Özellikleri:** det(A^T) = det(A), det(A * B) = det(A) * det(B). Bir matrisin iki satırı veya sütunu aynıysa ya da orantılıysa determinantı 0'dır.
- **Ters Matris (A^-1):** Bir kare matrisin tersinin olabilmesi için det(A) ≠ 0 (tekil olmayan / regüler) olması şarttır! Eğer det(A) = 0 ise matris tektir (singüler) ve tersi yoktur!
- **2x2 Ters Matris Formülü:** A = [a b; c d] ise A^-1 = (1 / det(A)) * [d -b; -c a]. Asal köşegen yer değiştirir, yedek köşegen işaret değiştirir.
- **Cramer Kuralı:** Ax = b sisteminde xi = det(Ai) / det(A). Ai matrisi, katsayılar matrisinin i. sütunu yerine b sonuç sütununun yazılmasıyla elde edilir.

---

## 📌 Ünite 7: Çok Değişkenli Fonksiyonlar

**Ana Başlıklar:** İki Değişkenli Fonksiyonlar, Birinci Mertebeden Kısmi Türevler, Schwarz Teoremi, İkinci Mertebeden Kısmi Türevler ve Ekstremum

### ⚡ Sınav Odaklı Hap Bilgiler ve Kritik Notlar
- **Çok Değişkenli Fonksiyon:** z = f(x, y) şeklinde birden fazla bağımsız değişkene sahip fonksiyonlardır.
- **Kısmi Türev Mantığı:** 
- **  - x'e göre kısmi türev (∂f/∂x veya fx):** y bir sabit sayı kabul edilerek x'e göre türev alınır.
- **  - y'ye göre kısmi türev (∂f/∂y veya fy):** x bir sabit sayı kabul edilerek y'ye göre türev alınır.
- **Schwarz Teoremi (Karma Kısmi Türevlerin Eşitliği):** Eğer sürekli türevlenebiliyorsa fxy = fyx'tir. Yani önce x'e sonra y'ye türev almak ile önce y'ye sonra x'e türev almak aynı sonucu verir.
- **İki Değişkenli Fonksiyonlarda Yerel Ekstremum (Maksimum/Minimum) Bulma Adımları:** 
- **  1. Kritik Nokta:** fx = 0 ve fy = 0 denklemleri ortak çözülerek kritik (x0, y0) noktaları bulunur.
- **  2. Hessian Determinantı (D):** D = fxx * fyy - (fxy)^2 hesaplanır.
- **     - Eğer D > 0 ve fxx > 0 ise fonksiyon (x0, y0) noktasında bir YEREL MİNİMUM'a sahiptir.:**      - Eğer D > 0 ve fxx > 0 ise fonksiyon (x0, y0) noktasında bir YEREL MİNİMUM'a sahiptir.
- **     - Eğer D > 0 ve fxx < 0 ise fonksiyon (x0, y0) noktasında bir YEREL MAKSİMUM'a sahiptir.:**      - Eğer D > 0 ve fxx < 0 ise fonksiyon (x0, y0) noktasında bir YEREL MAKSİMUM'a sahiptir.
- **     - Eğer D < 0 ise nokta bir EYER (SEMER) NOKTASI'dır (ne maksimum ne minimumdur).:**      - Eğer D < 0 ise nokta bir EYER (SEMER) NOKTASI'dır (ne maksimum ne minimumdur).
- **     - Eğer D = 0 ise test sonuçsuz kalır, başka yöntemlere bakılır.:**      - Eğer D = 0 ise test sonuçsuz kalır, başka yöntemlere bakılır.

---

## 📌 Ünite 8: İktisadi Uygulamalar

**Ana Başlıklar:** Piyasa Dengesi (Arz-Talep), Toplam ve Marjinal Hasılat, Toplam ve Marjinal Maliyet, Kâr Maksimizasyonu Kuralı (MR=MC), Talebin Fiyat Esnekliği

### ⚡ Sınav Odaklı Hap Bilgiler ve Kritik Notlar
- **Piyasa Denge Fiyatı ve Miktarı:** Talep (Qd) ve Arz (Qs) fonksiyonları eşitlenerek bulunur: Qd = Qs => P* (denge fiyatı) bulunur, yerine konularak Q* (denge miktarı) elde edilir.
- **Hasılat Fonksiyonları:** 
- **  - Toplam Hasılat (TR - Total Revenue):** TR = P * Q (Fiyat çarpı miktar).
- **  - Marjinal Hasılat (MR - Marginal Revenue):** Üretilen/satılan son birimin toplam hasılata katkısıdır. Toplam Hasılatın Q'ya göre 1. türevidir: MR = d(TR) / dQ.
- **Maliyet Fonksiyonları:** 
- **  - Toplam Maliyet (TC - Total Cost):** TC = TFC (Sabit Maliyet) + TVC (Değişken Maliyet).
- **  - Ortalama Maliyet (AC - Average Cost):** AC = TC / Q.
- **  - Marjinal Maliyet (MC - Marginal Cost):** Bir birim ek üretimin maliyetidir. Toplam Maliyetin Q'ya göre 1. türevidir: MC = d(TC) / dQ.
- **Kâr Maksimizasyonu Kuralı:** Toplam Kâr (π) = TR - TC. Kârın maksimum olması için 1. türevin sıfır olması gerekir: dπ/dQ = 0 => MR - MC = 0 => MR = MC! Yani kârı maksimize eden üretim düzeyinde Marjinal Hasılat daima Marjinal Maliyete eşit olmalıdır.
- **Talebin Fiyat Esnekliği Formülü:** ε = (dQ / dP) * (P / Q). Q'nun fiyata göre türevi ile P/Q oranının çarpımıdır.

---

## 🎯 Final İçin 1 - 4. Üniteler Hızlı Vize Hatırlatıcıları

### 🔹 Ünite 1: Kümeler ve Sayılar
- Alt Küme Sayısı Formülü: n elemanlı bir kümenin alt küme sayısı 2^n, kendisi hariç özalt küme sayısı ise 2^n - 1'dir. Örn: 4 elemanlı bir kümenin 2^4 = 16 alt kümesi, 15 özalt kümesi vardır.
- Birleşim ve Kesişim Eleman Sayısı: s(A ∪ B) = s(A) + s(B) - s(A ∩ B). Eğer A ve B ayrık kümeler ise (kesişimleri boş küme) s(A ∪ B) = s(A) + s(B)'dir.
- De Morgan Kuralları: (A ∪ B)' = A' ∩ B' ve (A ∩ B)' = A' ∪ B'. Birleşimin tümleyeni tümleyenlerin kesişimine eşittir.
- Sayı Kümeleri Hiyerarşisi: N (Doğal Sayılar: {0,1,2,...}) ⊂ Z (Tam Sayılar: {...,-2,-1,0,1,2,...}) ⊂ Q (Rasyonel Sayılar: a/b şeklinde yazılabilenler) ⊂ R (Gerçel/Reel Sayılar).

### 🔹 Ünite 2: Fonksiyonlar
- Fonksiyon Olma Şartı: f: A -> B için tanım kümesi A'nın her elemanı değer kümesi B'den yalnız bir elemanla eşleşmelidir. A'da açıkta eleman kalamaz, ancak B'de kalabilir.
- Bire-Bir (Injective) Fonksiyon: Farklı elemanların görüntüleri de farklı olmalıdır (x1 ≠ x2 => f(x1) ≠ f(x2)). Grafiğe çizilen yatay doğrular grafiği en fazla bir noktada kesmelidir (Yatay Doğru Testi).
- Örten (Surjective) Fonksiyon: Değer kümesinde açıkta hiç eleman kalmamasıdır (f(A) = B). Değer kümesinde açıkta eleman kalırsa fonksiyona 'İçine Fonksiyon' denir.
- Ters Fonksiyon (f^-1): Bir fonksiyonun tersinin olabilmesi için fonksiyonun MUTLAKA hem BİRE-BİR hem de ÖRTEN (Biyektif) olması şarttır! y = f(x) <=> x = f^-1(y). Bir fonksiyonun grafiği ile tersinin grafiği y = x doğrusuna göre simetriktir.

### 🔹 Ünite 3: Polinom Fonksiyonlar
- Doğrunun Eğimi (m): A(x1, y1) ve B(x2, y2) noktalarından geçen doğrunun eğimi m = (y2 - y1) / (x2 - x1)'dir. y = mx + n denkleminde x'in katsayısı m eğimdir, n ise doğrunun y eksenini kestiği noktadır.
- Paralel Doğrular: Eğilimleri birbirine eşittir (d1 // d2 => m1 = m2).
- Dik Doğrular: Birbirine dik iki doğrunun eğimleri çarpımı -1'dir (d1 ⊥ d2 => m1 * m2 = -1 => m2 = -1 / m1).
- İkinci Dereceden Fonksiyon (Parabol): f(x) = ax^2 + bx + c (a ≠ 0).

### 🔹 Ünite 4: Üstel ve Logaritmik Fonksiyonlar
- Üstel Fonksiyon: f(x) = a^x (a > 0 ve a ≠ 1).
-   - a > 1 ise fonksiyon artandır.
-   - 0 < a < 1 ise fonksiyon azalandır.
-   - Tanım kümesi tüm gerçel sayılar (-∞, +∞), görüntü kümesi pozitif gerçel sayılardır (0, +∞). Grafiği daima (0, 1) noktasından geçer.

