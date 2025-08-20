# 🤖 ChatCPT 3.0 - Türkçe AI Modeli

**ChatCPT 3.0**, gelişmiş Türkçe yapay zeka modeli. Sohbet, arama, öğrenme ve bağlam hafızası özellikleri ile donatılmış.

## ⚡ Hızlı Kurulum

### Windows PowerShell (Önerilen)
```powershell
iwr -useb https://raw.githubusercontent.com/[username]/chatcpt-3.0/main/install.ps1 | iex
```

### Manuel Kurulum
```bash
git clone https://github.com/[username]/chatcpt-3.0.git
cd chatcpt-3.0
pip install -r requirements.txt
python ai_model.py
```

## 🚀 Özellikler

### ✨ Temel Özellikler
- **🧠 Gelişmiş Türkçe Dil Modeli** - 5000+ kelime sözlüğü
- **💬 Akıllı Sohbet Sistemi** - Doğal dil işleme
- **🔍 Google Arama Entegrasyonu** - Güncel bilgi alma
- **📚 Sürekli Öğrenme** - Etkileşimlerden öğrenme
- **💾 Model Kaydetme** - Kalıcı hafıza

### 🎯 Gelişmiş Özellikler
- **Pattern Matching** - Yanıt kalıpları
- **Context Memory** - Bağlam hafızası
- **Confidence Scoring** - Güven skoru
- **Fine-tuning** - Model ince ayarı
- **Word Embeddings** - Kelime vektörleri

## 🎮 Kullanım

### Temel Komutlar
```
👤 Siz: Merhaba ChatCPT
🤖 ChatCPT 3.0: Merhaba! Size nasıl yardımcı olabilirim?

👤 Siz: Python nedir?
🤖 ChatCPT 3.0: [Detaylı Python açıklaması + güven skoru]

👤 Siz: ara: yapay zeka haberleri
🤖 ChatCPT 3.0: [Google'dan güncel bilgiler]
```

### Sistem Komutları
- `bilgi` - Model bilgileri
- `ara: [konu]` - Güncel bilgi arama
- `eğit: [dosya]` - Yeni verilerle eğitim
- `çıkış` - Programdan çık

## ⚙️ Konfigürasyon

### Google API Ayarları (Opsiyonel)
`config.env` dosyasını düzenleyin:
```env
GOOGLE_API_KEY=your_api_key_here
GOOGLE_SEARCH_ENGINE_ID=your_search_engine_id_here
```

### Google API Kurulumu
1. [Google Cloud Console](https://console.cloud.google.com/) → Yeni proje
2. "APIs & Services" → "Custom Search API" etkinleştir
3. API key oluştur
4. [Custom Search Engine](https://cse.google.com/) oluştur

## 📁 Proje Yapısı

```
ChatCPT-3.0/
├── 🤖 ai_model.py              # Ana AI modeli
├── 🔍 search_engine.py         # Google arama
├── 📚 eğitim_verisi.json       # Türkçe eğitim verisi
├── ⚙️ api_config.py            # API ayarları
├── 📋 requirements.txt         # Python paketleri
├── 🚀 install.ps1              # Otomatik kurulum
├── 📖 README.md                # Bu dosya
└── 📁 models/
    └── ChatCPT-3.0/
        ├── model.pkl           # Ana model
        ├── vocabulary.json     # Kelime sözlüğü
        └── patterns.json       # Yanıt kalıpları
```

## 🧠 Model Mimarisi

### Kelime İşleme
- **Tokenization** - Türkçe tokenizer
- **Vocabulary** - 5000 kelimelik sözlük
- **Embeddings** - 100 boyutlu vektörler

### Öğrenme Algoritması
- **Pattern Extraction** - Kalıp çıkarma
- **Similarity Calculation** - Benzerlik hesaplama
- **Confidence Scoring** - Güven değerlendirmesi
- **Fine-tuning** - İnce ayar

### Hafıza Sistemi
- **Context Memory** - Son 10 etkileşim
- **Knowledge Base** - Öğrenilen bilgiler
- **Response Patterns** - Yanıt kalıpları

## 📊 Performans

- **Model Boyutu:** ~50MB
- **Başlatma Süresi:** ~2-3 saniye
- **Yanıt Süresi:** ~1-2 saniye
- **Bellek Kullanımı:** ~100-200MB
- **Dil Desteği:** Türkçe optimizasyonu

## 🔧 Geliştirme

### Yeni Eğitim Verisi Ekleme
```json
{
    "instruction": "Soru metni",
    "input": "Ek girdi (opsiyonel)",
    "output": "Beklenen yanıt"
}
```

### Model Eğitimi
```python
# Yeni verilerle eğitim
model.fine_tune(new_training_data)

# Etkileşimden öğrenme
model.learn_from_interaction(user_input, expected_output)
```

### API Entegrasyonu
```python
from ai_model import AIModelInterface

ai = AIModelInterface()
response = ai.chat("Merhaba ChatCPT")
print(response)
```

## 🐛 Sorun Giderme

### Yaygın Hatalar

**Python Bulunamadı**
```bash
# Python 3.7+ kurun
https://www.python.org/downloads/
```

**Paket Kurulum Hatası**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Google API Hatası**
- `config.env` dosyasındaki API anahtarlarını kontrol edin
- Google Cloud Console'da API limitlerini kontrol edin

### Log Dosyaları
- Model dosyaları: `./models/ChatCPT-3.0/`
- Bilgi tabanı: `knowledge_base.json`
- Konfigürasyon: `config.env`

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit yapın (`git commit -m 'Add amazing feature'`)
4. Push yapın (`git push origin feature/amazing-feature`)
5. Pull Request açın

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 🙏 Teşekkürler

- **Türkçe Dil Desteği** - Türkçe optimizasyonu
- **Open Source Community** - Kütüphane desteği
- **Contributors** - Geliştirici katkıları

## 📞 Destek

- **Issues:** GitHub Issues kullanın
- **Dokümantasyon:** README.md dosyası
- **Örnekler:** `examples/` klasörü

---

**⭐ Projeyi beğendiyseniz yıldız vermeyi unutmayın!**

## 🚀 Hızlı Başlangıç

```powershell
# Tek komutla kurulum
iwr -useb https://raw.githubusercontent.com/[username]/chatcpt-3.0/main/install.ps1 | iex

# Başlatma
python ai_model.py
```

**ChatCPT 3.0** - Türkçe yapay zeka deneyiminin geleceği! 🤖✨