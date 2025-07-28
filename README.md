# 🧠 Loro Chat: Flask Tabanlı Çok Dilli Varlık Yönetim Asistanı

Bu proje, kullanıcıların web arayüzü üzerinden varlık bilgilerini (taşınmaz, taşıt, ekipman vb.) girdiği, bu verileri JSON formatında saklayan ve analiz eden bir Flask tabanlı uygulamadır.  
Ayrıca, gömülü LLM ile doğal dilde analiz yapılır ve çıktı PDF olarak sunulur.

## 🚀 Özellikler

- ✅ Flask tabanlı hızlı backend
- ✅ JSON formatında veri kaydı
- ✅ Manuel form, CSV/JSON dosya yükleme desteği
- ✅ Türkçe, İngilizce, Fransızca dil desteği
- ✅ Ollama tabanlı LLM entegresi (yerel)
- ✅ Grafik üretimi (bar, çizgi, pasta)
- ✅ Otomatik PDF raporu oluşturma
- ✅ Tek dosyalı statik grafik yapısı (`/static/grafik.png`)

## 📦 Kullanılan Teknolojiler

- Python + Flask
- HTML5 / Bootstrap 5
- Chart.js / Matplotlib
- JSON tabanlı veri saklama
- ReportLab (PDF oluşturma)
- Ollama + Mistral / Phi-3 (LLM)

## 🔧 Kurulum

pip install flask matplotlib reportlab
python app.py
🧪 Test Süreci
/ ana sayfası: form, dosya yükleme, dil seçimi

/grafik.png: her analiz sonrası üzerine yazılan grafik

/rapor.pdf: PDF rapor çıktısı (grafik + LLM analiz)

varliklar.json: sistemin kalıcı veri deposu

📂 Dosya Yapısı
pgsql
Kopyala
Düzenle
├── app.py
├── varliklar.json
├── static/
│   └── grafik.png
├── templates/
│   └── index.html
└── uploads/
    └── yüklenen CSV/JSON dosyaları
    
👩‍💻 Geliştirici
Büşra Mina AL
Yapay zekâ mühendisliği | Endüstri mühendisliği
Disiplinler arası üretken çözümler geliştirir, projeleri yalnızca kod değil anlam üzerine kurar.
www.linkedin.com/in/bmi̇nal60135806
