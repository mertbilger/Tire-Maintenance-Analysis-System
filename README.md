# 🚗 Lastik Bakım Öncelik Analiz Sistemi

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Fuzzy](https://img.shields.io/badge/Fuzzy%20Logic-scikit--fuzzy-green)
![GUI](https://img.shields.io/badge/GUI-Tkinter-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

Bulanık mantık (fuzzy logic) kullanarak araç lastiklerinin bakım önceliğini ve değişim ihtimalini hesaplayan Python tabanlı gelişmiş analiz uygulaması.


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
2. Gerekli Kütüphaneleri Yükleyin
```bash
pip install -r requirements.txt
```
