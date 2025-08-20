@echo off
echo ChatCPT 3.0 - GitHub Upload Komutlari
echo =====================================
echo.

echo Git repo baslatiliyor...
git init

echo Tum dosyalar ekleniyor...
git add .

echo Commit yapiliyor...
git commit -m "ChatCPT 3.0 - Turkce AI Modeli - Tam Surum

Ozellikler:
- ChatCPT 3.0 ana AI modeli
- Turkce dil destegi (5000+ kelime)
- Google Search API entegrasyonu
- Surekli ogrenme sistemi
- Model kaydetme ve yukleme
- Tek komut kurulum scripti
- Desktop kisayollari
- Kapsamli dokumantasyon

Kurulum:
iwr -useb https://raw.githubusercontent.com/CRTYPUBG/ChatCPT_AI_Models/main/install.ps1 | iex

Ana Dosyalar:
- ai_model.py (ChatCPT 3.0 ana modeli)
- search_engine.py (Google arama entegrasyonu)
- egitim_verisi.json (40+ Turkce egitim verisi)
- install.ps1 (Otomatik kurulum scripti)
- README.md (Kapsamli dokumantasyon)
- requirements.txt (Python paket listesi)

ChatCPT 3.0 - Turkce yapay zeka deneyiminin gelecegi!"

echo Ana branch ayarlaniyor...
git branch -M main

echo GitHub remote ekleniyor...
git remote add origin https://github.com/CRTYPUBG/ChatCPT_AI_Models.git

echo GitHub'a yukleniyor...
git push -u origin main

echo.
if %errorlevel% == 0 (
    echo BASARILI! ChatCPT 3.0 GitHub'a yuklendi!
    echo.
    echo GitHub Repo: https://github.com/CRTYPUBG/ChatCPT_AI_Models
    echo Kurulum Komutu: iwr -useb https://raw.githubusercontent.com/CRTYPUBG/ChatCPT_AI_Models/main/install.ps1 ^| iex
) else (
    echo HATA: Yukleme basarisiz!
    echo GitHub kimlik dogrulamasi gerekebilir.
)

echo.
pause