# ChatCPT 3.0 - Force Upload Script
# GitHub'daki mevcut dosyaları override eder

Write-Host "ChatCPT 3.0 - Force Upload Script" -ForegroundColor Green
Write-Host "==================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "UYARI: Bu script GitHub'daki mevcut dosyalari override edecek!" -ForegroundColor Red
$confirm = Read-Host "Devam etmek istiyor musunuz? (E/H)"

if ($confirm -ne "E" -and $confirm -ne "e") {
    Write-Host "Islem iptal edildi." -ForegroundColor Yellow
    exit
}

Write-Host ""
Write-Host "Git durumu kontrol ediliyor..." -ForegroundColor Blue
git status

Write-Host ""
Write-Host "Remote'dan son degisiklikleri cekiliyor..." -ForegroundColor Blue
git pull origin main --allow-unrelated-histories

Write-Host ""
Write-Host "Tum dosyalar ekleniyor..." -ForegroundColor Blue
git add .

Write-Host ""
Write-Host "Commit yapiliyor..." -ForegroundColor Blue
git commit -m "ChatCPT 3.0 - Tam Surum - Tum Dosyalar

Ana Dosyalar:
- ai_model.py (ChatCPT 3.0 ana AI modeli)
- egitim_verisi.json (40 Turkce egitim verisi)
- search_engine.py (Google Search API)
- api_config.py (API konfigurasyonu)
- install.ps1 (Tek komut kurulum)
- README.md (Kapsamli dokumantasyon)
- requirements.txt (Python paketleri)

Yardimci Dosyalar:
- basit_ai.py (Basit AI sistemi)
- working_ai_system.py (Alternatif AI)
- run_ai_system.py (Ana sistem yoneticisi)
- free_search_engine.py (Ucretsiz arama)

Upload Araclari:
- quick_check.ps1 (Dosya kontrol)
- simple_upload.ps1 (GitHub upload)
- fix_git.ps1 (Git remote duzeltme)

Kurulum Komutu:
iwr -useb https://raw.githubusercontent.com/CRTYPUBG/ChatCPT_AI_Models/main/install.ps1 | iex

ChatCPT 3.0 - Turkce yapay zeka deneyiminin gelecegi!"

Write-Host ""
Write-Host "GitHub'a force push yapiliyor..." -ForegroundColor Green
git push origin main --force

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "BASARILI! ChatCPT 3.0 GitHub'a yuklendi!" -ForegroundColor Green
    Write-Host ""
    Write-Host "GitHub Repo: https://github.com/CRTYPUBG/ChatCPT_AI_Models" -ForegroundColor Blue
    Write-Host ""
    Write-Host "Kullanicilarin kurulum komutu:" -ForegroundColor Yellow
    Write-Host "iwr -useb https://raw.githubusercontent.com/CRTYPUBG/ChatCPT_AI_Models/main/install.ps1 | iex" -ForegroundColor White
    Write-Host ""
    Write-Host "Yuklenen dosyalar:" -ForegroundColor Green
    Write-Host "  - ai_model.py (ChatCPT 3.0 ana modeli)" -ForegroundColor White
    Write-Host "  - egitim_verisi.json (40 Turkce egitim verisi)" -ForegroundColor White
    Write-Host "  - search_engine.py (Google arama)" -ForegroundColor White
    Write-Host "  - install.ps1 (Otomatik kurulum)" -ForegroundColor White
    Write-Host "  - README.md (Dokumantasyon)" -ForegroundColor White
    Write-Host "  - Ve daha fazlasi..." -ForegroundColor White
} else {
    Write-Host ""
    Write-Host "HATA: Force push basarisiz!" -ForegroundColor Red
    Write-Host "GitHub kimlik dogrulamasi gerekebilir." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Force upload islemi tamamlandi!" -ForegroundColor Green
Read-Host "Cikis icin Enter'a basin"