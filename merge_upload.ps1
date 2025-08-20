# ChatCPT 3.0 - Merge Upload Script
# GitHub'daki dosyalarla merge eder

Write-Host "ChatCPT 3.0 - Merge Upload Script" -ForegroundColor Green
Write-Host "==================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "GitHub'dan son degisiklikleri cekiliyor..." -ForegroundColor Blue
git pull origin main --allow-unrelated-histories

if ($LASTEXITCODE -ne 0) {
    Write-Host "Pull basarisiz! Conflict cozuluyor..." -ForegroundColor Yellow
    
    # Conflict'leri otomatik çöz (bizim dosyalarımızı tercih et)
    git checkout --ours .
    git add .
    git commit -m "Conflict cozuldu - local dosyalar tercih edildi"
}

Write-Host ""
Write-Host "Tum dosyalar ekleniyor..." -ForegroundColor Blue
git add .

Write-Host ""
Write-Host "Commit yapiliyor..." -ForegroundColor Blue
git commit -m "ChatCPT 3.0 - Merge Update - Tum Dosyalar

Guncellenen Dosyalar:
- ai_model.py (ChatCPT 3.0 ana AI modeli)
- egitim_verisi.json (40 Turkce egitim verisi) - YENİ
- search_engine.py (Google Search API)
- api_config.py (API konfigurasyonu)
- install.ps1 (Tek komut kurulum)
- README.md (Kapsamli dokumantasyon)
- requirements.txt (Python paketleri)

Eklenen Yardimci Dosyalar:
- basit_ai.py (Basit AI sistemi)
- working_ai_system.py (Alternatif AI)
- run_ai_system.py (Ana sistem yoneticisi)
- free_search_engine.py (Ucretsiz arama)
- quick_check.ps1 (Dosya kontrol)
- simple_upload.ps1 (GitHub upload)

Kurulum:
iwr -useb https://raw.githubusercontent.com/CRTYPUBG/ChatCPT_AI_Models/main/install.ps1 | iex"

Write-Host ""
Write-Host "GitHub'a push yapiliyor..." -ForegroundColor Green
git push origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "BASARILI! ChatCPT 3.0 merge edildi ve yuklendi!" -ForegroundColor Green
    Write-Host ""
    Write-Host "GitHub Repo: https://github.com/CRTYPUBG/ChatCPT_AI_Models" -ForegroundColor Blue
    Write-Host ""
    Write-Host "Test etmek icin:" -ForegroundColor Yellow
    Write-Host "iwr -useb https://raw.githubusercontent.com/CRTYPUBG/ChatCPT_AI_Models/main/install.ps1 | iex" -ForegroundColor White
} else {
    Write-Host ""
    Write-Host "HATA: Merge push basarisiz!" -ForegroundColor Red
    Write-Host "Manuel cozum gerekebilir." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Merge upload islemi tamamlandi!" -ForegroundColor Green
Read-Host "Cikis icin Enter'a basin"