# 🚀 ChatCPT 3.0 - Hızlı Kurulum Kılavuzu

## ⚡ TEK KOMUT KURULUM

### Windows PowerShell'de çalıştırın:

```powershell
iwr -useb https://raw.githubusercontent.com/CRTYPUBG/ChatCPT_AI_Models/main/install.ps1 | iex
```

## 🎯 Bu Komut Ne Yapar?

1. ✅ **Sistem Kontrolü** - Python ve Git kontrol eder
2. 📥 **Otomatik İndirme** - GitHub'dan projeyi indirir
3. 🐍 **Python Ortamı** - Sanal ortam oluşturur
4. 📦 **Paket Kurulumu** - Gerekli kütüphaneleri kurar
5. ⚙️ **Konfigürasyon** - Ayar dosyalarını oluşturur
6. 🖥️ **Kısayollar** - Desktop ve Start Menu kısayolları
7. 🚀 **Otomatik Başlatma** - ChatCPT 3.0'ı başlatır

## 📍 Kurulum Sonrası

### Başlatma Seçenekleri:
- **Desktop Kısayolu:** "ChatCPT 3.0" çift tıklayın
- **Start Menu:** "ChatCPT 3.0" arayın
- **Manuel:** `python ai_model.py` komutu

### Konfigürasyon:
- Google API için `config.env` dosyasını düzenleyin
- Eğitim verisi için `eğitim_verisi.json` dosyasını güncelleyin

## 🔧 Manuel Kurulum (Alternatif)

```bash
# 1. Projeyi indirin
git clone https://github.com/CRTYPUBG/ChatCPT_AI_Models.git
cd ChatCPT_AI_Models

# 2. Python sanal ortamı oluşturun
python -m venv venv
venv\Scripts\activate

# 3. Gerekli paketleri kurun
pip install -r requirements.txt

# 4. ChatCPT 3.0'ı başlatın
python ai_model.py
```

## 🆘 Sorun Giderme

### Python Bulunamadı Hatası:
```
❌ Python bulunamadı!
```
**Çözüm:** [Python 3.7+](https://www.python.org/downloads/) kurun

### Git Bulunamadı Hatası:
```
❌ Git bulunamadı!
```
**Çözüm:** [Git](https://git-scm.com/download/win) kurun

### PowerShell Execution Policy Hatası:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## 📞 Destek

- **GitHub Issues:** [Sorun Bildirin](https://github.com/CRTYPUBG/ChatCPT_AI_Models/issues)
- **Dokümantasyon:** [README.md](README.md)

---

**🤖 ChatCPT 3.0 - Türkçe AI deneyiminin geleceği!**