@echo off
title ChatCPT 3.0 - Türkçe AI Modeli

echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                                                              ║
echo ║           🤖 ChatCPT 3.0 - TÜRKÇE AI MODELİ 🚀              ║
echo ║                                                              ║
echo ║                    Versiyon: 3.0                             ║
echo ║                                                              ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

REM Sanal ortamı kontrol et
if exist "venv\Scripts\activate.bat" (
    echo ⚡ Sanal ortam aktifleştiriliyor...
    call venv\Scripts\activate.bat
) else (
    echo ⚠️ Sanal ortam bulunamadı. Python global ortamı kullanılacak.
)

REM Python kontrolü
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python bulunamadı! Lütfen Python 3.7+ kurun.
    echo 📥 İndirme: https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Gerekli dosyaları kontrol et
if not exist "ai_model.py" (
    echo ❌ ai_model.py dosyası bulunamadı!
    pause
    exit /b 1
)

if not exist "eğitim_verisi.json" (
    echo ❌ eğitim_verisi.json dosyası bulunamadı!
    pause
    exit /b 1
)

echo ✅ Sistem kontrolleri tamamlandı.
echo 🚀 ChatCPT 3.0 başlatılıyor...
echo.

REM ChatCPT 3.0'ı başlat
python ai_model.py

echo.
echo 👋 ChatCPT 3.0 sonlandırıldı.
pause