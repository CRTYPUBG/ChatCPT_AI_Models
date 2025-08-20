# ChatCPT 3.0 - Basit GitHub Upload Script
# Emoji sorunları olmadan çalışır

Write-Host "ChatCPT 3.0 - GitHub Upload Scripti" -ForegroundColor Green
Write-Host "====================================" -ForegroundColor Cyan
Write-Host ""

# Git kontrolü
try {
    $gitVersion = git --version 2>&1
    Write-Host "Git bulundu: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "Git bulunamadi! Lutfen Git kurun." -ForegroundColor Red
    exit 1
}

# Repo bilgileri
$repoUrl = "https://github.com/CRTYPUBG/ChatCPT_AI_Models.git"

Write-Host "Repo URL: $repoUrl" -ForegroundColor Blue
Write-Host ""

# Git repo kontrolü
if (Test-Path ".git") {
    Write-Host "Mevcut Git repo bulundu. Guncelleme yapilacak..." -ForegroundColor Yellow
} else {
    Write-Host "Yeni Git repo baslatiliyor..." -ForegroundColor Blue
    git init
    git remote add origin $repoUrl
}

# Kritik dosyaları kontrol et
$criticalFiles = @(
    "ai_model.py",
    "search_engine.py", 
    "api_config.py",
    "eğitim_verisi.json",
    "install.ps1",
    "README.md",
    "requirements.txt"
)

Write-Host "Kritik dosyalar kontrol ediliyor..." -ForegroundColor Blue
$missingCritical = @()

foreach ($file in $criticalFiles) {
    if (Test-Path $file) {
        Write-Host "  OK: $file" -ForegroundColor Green
    } else {
        Write-Host "  EKSIK: $file" -ForegroundColor Red
        $missingCritical += $file
    }
}

if ($missingCritical.Count -gt 0) {
    Write-Host ""
    Write-Host "HATA: $($missingCritical.Count) kritik dosya eksik!" -ForegroundColor Red
    foreach ($file in $missingCritical) {
        Write-Host "  - $file" -ForegroundColor Red
    }
    Write-Host ""
    Write-Host "Lutfen eksik dosyalari olusturun ve tekrar deneyin." -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "Tum kritik dosyalar mevcut!" -ForegroundColor Green

# Kullanıcı onayı
$confirm = Read-Host "GitHub'a yuklemek istiyor musunuz? (E/H)"
if ($confirm -ne "E" -and $confirm -ne "e") {
    Write-Host "Islem iptal edildi." -ForegroundColor Yellow
    exit
}

Write-Host ""
Write-Host "Dosyalar Git'e ekleniyor..." -ForegroundColor Blue
git add .

Write-Host "Commit yapiliyor..." -ForegroundColor Blue
$commitMessage = "ChatCPT 3.0 - Turkce AI Modeli

Ozellikler:
- ChatCPT 3.0 ana AI modeli
- Turkce dil destegi (5000+ kelime)
- Google Search API entegrasyonu
- Surekli ogrenme sistemi
- Model kaydetme ve yukleme
- Tek komut kurulum scripti

Kurulum:
iwr -useb https://raw.githubusercontent.com/CRTYPUBG/ChatCPT_AI_Models/main/install.ps1 | iex

ChatCPT 3.0 - Turkce yapay zeka deneyiminin gelecegi!"

git commit -m $commitMessage

Write-Host "GitHub'a yukleniyor..." -ForegroundColor Green
git branch -M main
git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "BASARILI! GitHub'a yuklendi!" -ForegroundColor Green
    Write-Host ""
    Write-Host "GitHub Repo: https://github.com/CRTYPUBG/ChatCPT_AI_Models" -ForegroundColor Blue
    Write-Host ""
    Write-Host "Kullanicilarin kurulum komutu:" -ForegroundColor Yellow
    Write-Host "iwr -useb https://raw.githubusercontent.com/CRTYPUBG/ChatCPT_AI_Models/main/install.ps1 | iex" -ForegroundColor White
} else {
    Write-Host ""
    Write-Host "HATA: Yukleme basarisiz!" -ForegroundColor Red
    Write-Host "GitHub kimlik dogrulamasi gerekebilir." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Upload islemi tamamlandi!" -ForegroundColor Green
Read-Host "Cikis icin Enter'a basin"