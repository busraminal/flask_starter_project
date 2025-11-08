# 📊 Zorunlu Alan Kontrol Sistemi (Excel Tabanlı Flask Uygulaması)

Bu proje, kullanıcıdan alınan `.xlsx` formatlı Excel dosyalarını **zorunlu alan şemasına göre otomatik kontrol eden**, eksik/kritik hücreleri **sarı renkle işaretleyip** kullanıcıya geri sunan bir veri kalite denetim sistemidir.

---

## 🎯 Amaç
- Veri giriş hatalarını hızlıca tespit etmek
- Zorunlu alan ihlallerini otomatik işaretlemek
- İnsan hatasını azaltarak veri standardizasyonunu güçlendirmek

---

## 🚀 Özellikler

| Özellik | Açıklama |
|--------|---------|
| 📁 Dosya Yükleme | Kullanıcı `.xlsx` dosyasını arayüzden yükler |
| ✅ Zorunlu Alan Kontrolü | Sistem dosyayı şablonla karşılaştırır |
| 🎨 Renkli Vurgu | Eksik/hatalı hücreler **sarı renge boyanır** |
| 🔄 Anlık İşleme | Sonuç kullanıcıya anında sunulur |
| 🌐 Web Arayüzü | Flask tabanlı sade ve hızlı UI |

---

## 🧠 Kullanım Senaryosu
1. Kullanıcı dosyasını yükler.
2. Sistem `zorunlu_saha_sablonu.xlsx` içindeki alanlarla karşılaştırır.
3. Eksik/hatalı hücreler tespit edilir ve sarı renkle boya uygulanır.
4. İşlenmiş dosya kullanıcının indirme sayfasına sunulur.

---

## 🧱 Kullanılan Teknolojiler
- Python
- Flask
- Pandas
- OpenPyXL
- HTML + Bootstrap (UI)
- *(Opsiyonel)* Matplotlib / Seaborn – hata analiz grafikleri için

---

## 📂 Proje Yapısı

```
ZorunluAlanKontrol/
│
├── app.py                         # Flask uygulaması
├── zorunlu_saha_sablonu.xlsx      # Zorunlu alan şeması
├── uploads/                       # Kullanıcı dosyalarının işlendiği klasör
│
├── templates/
│   └── index.html                 # Yükleme ve sonuç sayfası
│
└── static/
    └── style.css                  # Sarı işaretleme + tablo tasarımları
```

---

## 🧪 Kurulum & Çalıştırma

```bash
pip install flask pandas openpyxl
python app.py
```

Tarayıcıda aç:  
```
http://127.0.0.1:5000/
```

---

## 👩‍💻 Geliştirici
**Büşra Mina AL**  
Yapay Zekâ Mühendisi & Endüstri Mühendisi  

LinkedIn: https://www.linkedin.com/in/bmi̇nal60135806

---

## 📜 Lisans
Bu proje eğitim ve kurum içi süreçlerde kullanılmak üzere paylaşılmıştır.  
Dış veya ticari kullanım için geliştirici izni gereklidir.
