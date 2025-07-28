# 🟡 Zorunlu Alan Kontrol Sistemi (Excel Tabanlı Flask Uygulaması)

Bu proje, kullanıcıdan alınan `.xlsx` formatlı Excel dosyalarını önceden tanımlı kurallara göre analiz eden ve eksik/kritik alanları **renklendirerek (örneğin sarı)** kullanıcıya sunan bir **veri denetim sistemidir**.

## 🎯 Proje Amacı

- Zorunlu alan içeren veri setlerinde eksik veya hatalı bilgilerin tespiti
- Otomatikleştirilmiş **veri kalitesi kontrolü**
- Excel dosyasındaki kritik eksikleri **renkli biçimde vurgulamak**

---

## 🚀 Özellikler

- ✅ Excel dosyası yükleme (drag & drop / file picker)
- ✅ Zorunlu alan tanımı şemasıyla karşılaştırma
- ✅ Eksik/hatalı hücrelerin sarıya boyanması
- ✅ Anlık görsel çıktı ve doğrulama tablosu
- ✅ Flask tabanlı web arayüzü
- ✅ VS Code uyumlu çalışma yapısı

---

## 🧠 Kullanım Senaryosu

1. Kullanıcı `.xlsx` dosyasını yükler
2. Sistem bu dosyayı, tanımlı zorunlu alanlara göre kontrol eder
3. Eksik alanlar belirlenir
4. Sonuç dosyası:
   - Sarıya boyalı hücreler ile görsel çıktı
   - Hangi satır/hücrede eksiklik olduğu
   - Ek olarak tablo halinde detay rapor (isteğe bağlı)

---

## 📦 Kullanılan Teknolojiler

- **Python**
- **Flask** (backend)
- **OpenPyXL / Pandas** (Excel işleme)
- **HTML + Bootstrap** (arayüz)
- **Matplotlib / Seaborn** (grafik opsiyonel)

---

## 🗂️ Dosya Yapısı

📄 app.py # Flask uygulaması
📁 templates/
└── index.html # Ana yükleme ve sonuç arayüzü
📁 static/
└── style.css # Sarı boyama + tablo stilizasyonu
📄 zorunlu_saha_sablonu.xlsx # Zorunlu alan şeması
📄 uploads/ # Kullanıcının yüklediği dosyalar

## 🧪 Kurulum
pip install flask pandas openpyxl
python app.py
Ardından tarayıcında http://127.0.0.1:5000/ adresine git.

👩‍💻 Geliştirici
Büşra Mina AL
Yapay zekâ & sistem mühendisi — veriyle konuşan arayüzler geliştirir.
🧠 “Veri doğruysa sistem güçlüdür” anlayışıyla bu uygulamayı geliştirmiştir.
www.linkedin.com/in/bmi̇nal60135806

📜 Lisans
Bu proje eğitim ve iç süreçlerde kullanılmak üzere açık kaynak olarak paylaşılmıştır.
