# ChatCPT 3.0 - GitHub Upload PowerShell Komutları

Write-Host "ChatCPT 3.0 - GitHub Upload Komutlari" -ForegroundColor Green
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host ""

# Git repo başlat
Write-Host "Git repo baslatiliyor..." -ForegroundColor Blue
git init

# Tüm dosyaları ekle
Write-Host "Tum dosyalar ekleniyor..." -ForegroundColor Blue
git add .

# Commit yap
Write-Host "Commit yapiliyor..." -ForegroundColor Blue
$commitMessage = @"
ChatCPT 3.0 - Turkce AI Modeli - Tam Surum

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

Yardimci Dosyalar:
- basit_ai.py (Basit AI versiyonu)
- working_ai_system.py (Alternatif AI sistemi)
- run_ai_system.py (Ana sistem yoneticisi)
- free_search_engine.py (Ucretsiz arama motoru)

Konfigürasyon:
- api_config.py (API ayarlari)
- config.py (Sistem konfigürasyonu)
- .gitignore (Git ignore kurallari)
- LICENSE (MIT lisansi)

ChatCPT 3.0 - Turkce yapay zeka deneyiminin gelecegi!
"@

git commit -m $commitMessage

# Ana branch ayarla
Write-Host "Ana branch ayarlaniyor..." -ForegroundColor Blue
git branch -M main

# GitHub remote ekle
Write-Host "GitHub remote ekleniyor..." -ForegroundColor Blue
git remote add origin https://github.com/CRTYPUBG/ChatCPT_AI_Models.git

# GitHub'a yükle
Write-Host "GitHub'a yukleniyor..." -ForegroundColor Green
git push -u origin main

# Sonuç kontrol
if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "BASARILI! ChatCPT 3.0 GitHub'a yuklendi!" -ForegroundColor Green
    Write-Host ""
    Write-Host "GitHub Repo: https://github.com/CRTYPUBG/ChatCPT_AI_Models" -ForegroundColor Blue
    Write-Host ""
    Write-Host "Kullanicilarin kurulum komutu:" -ForegroundColor Yellow
    Write-Host "iwr -useb https://raw.githubusercontent.com/CRTYPUBG/ChatCPT_AI_Models/main/install.ps1 | iex" -ForegroundColor White
    Write-Host ""
    Write-Host "Ozellikler:" -ForegroundColor Yellow
    Write-Host "  - Tek komut kurulum" -ForegroundColor White
    Write-Host "  - Otomatik kisayol olusturma" -ForegroundColor White
    Write-Host "  - Python sanal ortam" -ForegroundColor White
    Write-Host "  - Google API entegrasyonu" -ForegroundColor White
    Write-Host "  - Turkce AI modeli" -ForegroundColor White
} else {
    Write-Host ""
    Write-Host "HATA: Yukleme basarisiz!" -ForegroundColor Red
    Write-Host "GitHub kimlik dogrulamasi gerekebilir." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Cozum onerileri:" -ForegroundColor Yellow
    Write-Host "  - GitHub Desktop kullanin" -ForegroundColor White
    Write-Host "  - Git credentials ayarlayin" -ForegroundColor White
    Write-Host "  - SSH key ekleyin" -ForegroundColor White
}

Write-Host ""
Write-Host "Upload islemi tamamlandi!" -ForegroundColor Green
Read-Host "Cikis icin Enter'a basin"