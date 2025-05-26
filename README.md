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

## 🛠️ Kurulum

### Gereksinimler
- Python 3.8+
- Gerekli kütüphaneler:
```bash
git clone https://github.com/mertbilger/Tire-Maintenance-Analysis-System.git

## ÖNEMLİ
```bash
pip install -r requirements.txt
# Üyelik fonksiyonları örneği
temperature['low'] = fuzz.trimf(temperature.universe, [10, 10, 22])
temperature['medium'] = fuzz.trimf(temperature.universe, [18, 25, 32])
temperature['high'] = fuzz.trimf(temperature.universe, [28, 40, 40])

# Örnek kural
rule1 = ctrl.Rule(temperature['high'] | noise['high'], ac_level['high'])
