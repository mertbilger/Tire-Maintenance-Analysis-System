# 🚗 Lastik Bakım Analiz Sistemi

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Fuzzy](https://img.shields.io/badge/Fuzzy%20Logic-scikit--fuzzy-green)
![GUI](https://img.shields.io/badge/GUI-Tkinter-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

Bulanık mantık (fuzzy logic) kullanarak araç lastiklerinin bakım önceliğini ve değişim ihtimalini hesaplayan Python tabanlı gelişmiş analiz uygulaması.

### Proje, Zadeh (1965) tarafından geliştirilen bulanık mantık teorisine dayanmaktadır:


## 📚 Teorik Temeller

Proje, lastik bakım yönetiminde bulanık mantık yaklaşımını uygulamaktadır. Geleneksel yöntemlerin aksine:

- **Çoklu parametrelerin** (sıcaklık, hız vb.) non-lineer etkileşimlerini modellemekte
- Kesin olmayan sınır değerlerinde ("yüksek hız" gibi) insan mantığına uyumlu karar verme sağlamakta
- Literatürde benzer çalışmalarda %88-92 doğruluk oranları rapor edilmiştir
- Endüstriyel uygulamalarda lastik ömrü tahminlerinde %15-20'lik iyileşme sağladığı gözlemlenmiştir

## ✨ Özellikler

- **Kapsamlı Parametre Analizi**:
  - ⏱️ Günlük kullanım süresi (0-24 saat)
  - 🛣️ Yol sertliği (1-10 skalası)
  - 🌡️ Ortam sıcaklığı (-20°C - 50°C)
  - 🚗 Ortalama hız (0-200 km/s)
  - 💨 Lastik basıncı (20-40 PSI)

- **Gelişmiş Çıktılar**:
  - 🔢 Bakım Önceliği (0-10 skalası)
  - 📊 Değişim İhtimali (%)
  - 📈 Grafiksel gösterimler
  - 📝 Detaylı matematiksel rapor

- **Kullanıcı Dostu Arayüz**:
  - Tkinter tabanlı modern GUI
  - Kolay parametre girişi
  - Anlık sonuç görüntüleme
 
## 🧠 Bulanık Mantık Temelleri


1. **Bulanıklaştırma**: Kesin değerlerin üyelik fonksiyonlarıyla bulanık kümeler halinde ifadesi
   - Örneğin: "Yol sertliği 7 → %40 yüksek, %60 orta"

2. **Kural Tabanı**: 8 adet uzman kuralı içerir

3. **Çıkarım Mekanizması**: Mamdani tipi bulanık çıkarım sistemi

4. **Durulaştırma**: Centroid yöntemi ile net değer hesaplama

```bash
[Girdi Parametreleri] → [Bulanıklaştırma] → [Kural Değerlendirme] → [Durulaştırma] → [Çıktılar]
```

## 🛠️ Kurulum

### Ön Gereksinimler
- Python 3.8 veya üzeri
- Git (opsiyonel)

### Adım Adım Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/mertbilger/Tire-Maintenance-Analysis-System.git
cd Tire-Maintenance-Analysis-System
```
## ÖNEMLİ

2. Gerekli Kütüphaneleri Yükleyin
```bash
pip install -r requirements.txt
```
## 🖥️ Kullanım

1.Uygulamayı başlatın

2.Arayüzde tüm parametreleri girin

3.Hesapla" butonuna basın

4.Sonuçları ve grafikleri görüntüleyin

