@echo off
title ChatCPT 3.0 - GitHub Upload Script

echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                                                              ║
echo ║        🚀 ChatCPT 3.0 - GitHub Upload Script 📤            ║
echo ║                                                              ║
echo ║           Tüm dosyalar GitHub'a yüklenecek                   ║
echo ║                                                              ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

REM Git kontrolü
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Git bulunamadı! Lütfen Git kurun.
    echo 📥 İndirme: https://git-scm.com/download/win
    pause
    exit /b 1
)

echo ✅ Git bulundu
echo.

REM GitHub repo bilgileri
set REPO_URL=https://github.com/CRTYPUBG/ChatCPT_AI_Models.git
set REPO_NAME=ChatCPT_AI_Models

echo 📋 Repo Bilgileri:
echo    URL: %REPO_URL%
echo    İsim: %REPO_NAME%
echo.

REM Mevcut git repo kontrolü
if exist ".git" (
    echo ⚠️ Mevcut Git repo bulundu. Güncelleme yapılacak...
    git status
    echo.
) else (
    echo 🆕 Yeni Git repo başlatılıyor...
    git init
    git remote add origin %REPO_URL%
    echo.
)

echo 📁 Yüklenecek dosyalar kontrol ediliyor...

REM Ana dosyalar
set FILES_TO_CHECK=ai_model.py search_engine.py api_config.py eğitim_verisi.json

for %%f in (%FILES_TO_CHECK%) do (
    if exist "%%f" (
        echo ✅ %%f
    ) else (
        echo ❌ %%f - EKSIK!
    )
)

echo.
echo 📦 Tüm dosyalar Git'e ekleniyor...

REM Tüm dosyaları ekle
git add .

echo.
echo 📝 Commit mesajı oluşturuluyor...

REM Commit yap
git commit -m "ChatCPT 3.0 - Türkçe AI Modeli - Tam Sürüm

✨ Özellikler:
- ChatCPT 3.0 ana AI modeli
- Türkçe dil desteği (5000+ kelime)
- Google Search API entegrasyonu
- Sürekli öğrenme sistemi
- Model kaydetme ve yükleme
- Tek komut kurulum scripti
- Desktop kısayolları
- Kapsamlı dokümantasyon

🚀 Kurulum:
iwr -useb https://raw.githubusercontent.com/CRTYPUBG/ChatCPT_AI_Models/main/install.ps1 | iex

📁 Dosyalar:
- ai_model.py (Ana AI modeli)
- search_engine.py (Google arama)
- eğitim_verisi.json (Türkçe eğitim verisi)
- install.ps1 (Otomatik kurulum)
- README.md (Dokümantasyon)
- requirements.txt (Python paketleri)
- Ve daha fazlası...

🤖 ChatCPT 3.0 - Türkçe yapay zeka deneyiminin geleceği!"

echo.
echo 🚀 GitHub'a yükleniyor...

REM GitHub'a push yap
git branch -M main
git push -u origin main

if errorlevel 0 (
    echo.
    echo ✅ Başarıyla yüklendi!
    echo.
    echo 🌐 GitHub Repo: https://github.com/CRTYPUBG/ChatCPT_AI_Models
    echo 📥 Kurulum Komutu:
    echo    iwr -useb https://raw.githubusercontent.com/CRTYPUBG/ChatCPT_AI_Models/main/install.ps1 ^| iex
    echo.
) else (
    echo.
    echo ❌ Yükleme hatası!
    echo 💡 GitHub kimlik doğrulaması gerekebilir.
    echo.
)

echo 📊 Son durum kontrol ediliyor...
git status

echo.
echo 👋 Upload işlemi tamamlandı!
pause