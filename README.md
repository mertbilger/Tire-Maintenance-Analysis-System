# 🚗 Lastik Bakım Öncelik Analiz Sistemi

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Fuzzy](https://img.shields.io/badge/Fuzzy%20Logic-scikit--fuzzy-green)
![GUI](https://img.shields.io/badge/GUI-Tkinter-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

Bulanık mantık (fuzzy logic) kullanarak lastik bakım önceliğini ve değişim ihtimalini hesaplayan Python tabanlı uygulama.


## ✨ Özellikler

- Kullanıcı dostu Tkinter arayüzü
- 5 temel parametre ile analiz:
  - ⏱️ Günlük kullanım süresi
  - 🛣️ Yol sertliği 
  - 🌡️ Ortam sıcaklığı
  - 🚗 Ortalama hız
  - 💨 Lastik basıncı
- Bulanık mantık kurallarıyla:
  - 🔢 Bakım Önceliği (0-10 skalası)
  - 📊 Değişim İhtimali (%)
- Detaylı matematiksel rapor üretimi

  📊 Matematiksel Model
Üyelik Fonksiyonları
Parametre	Aralık	Düşük	Orta	Yüksek
Yol Sertliği	0-10	0-5 (μ=0.0)	4-8 (μ=0.75)	7-10 (μ=0.4)
Ortalama Hız	0-160 km/s	0-80 (μ=0.0)	60-140 (μ=0.25)	100+ (μ=0.33)


## 🛠️ Kurulum

### Gereksinimler
- Python 3.8+
- Gerekli kütüphaneler:
```bash
git clone https://github.com/mertbilger/Tire-Maintenance-Analysis-System.git

## ÖNEMLİ
```bash
pip install -r requirements.txt
