# ChatCPT 3.0 - Hızlı Dosya Kontrol
# Kritik dosyaların varlığını kontrol eder

Write-Host "ChatCPT 3.0 - Dosya Kontrol" -ForegroundColor Green
Write-Host "============================" -ForegroundColor Cyan
Write-Host ""

# Kritik dosyalar
$files = @{
    "ai_model.py" = "ChatCPT 3.0 ana AI modeli"
    "search_engine.py" = "Google Search API"
    "api_config.py" = "API konfigurasyonu"
    "eğitim_verisi.json" = "Turkce egitim verisi"
    "install.ps1" = "Otomatik kurulum scripti"
    "README.md" = "Dokumantasyon"
    "requirements.txt" = "Python paketleri"
    ".gitignore" = "Git ignore kurallari"
}

$existing = 0
$missing = @()

Write-Host "Kritik dosyalar kontrol ediliyor..." -ForegroundColor Blue
Write-Host ""

foreach ($file in $files.Keys) {
    if (Test-Path $file) {
        $size = (Get-Item $file).Length
        $sizeKB = [math]::Round($size / 1024, 2)
        Write-Host "  OK: $file ($sizeKB KB)" -ForegroundColor Green
        Write-Host "      $($files[$file])" -ForegroundColor DarkGray
        $existing++
    } else {
        Write-Host "  EKSIK: $file" -ForegroundColor Red
        Write-Host "         $($files[$file])" -ForegroundColor DarkGray
        $missing += $file
    }
    Write-Host ""
}

# Özet
Write-Host "OZET:" -ForegroundColor Blue
Write-Host "-----" -ForegroundColor Cyan
Write-Host "Mevcut: $existing" -ForegroundColor Green
Write-Host "Eksik: $($missing.Count)" -ForegroundColor Red
Write-Host "Toplam: $($files.Count)" -ForegroundColor Blue
Write-Host "Tamamlanma: $([math]::Round(($existing / $files.Count) * 100, 1))%" -ForegroundColor Yellow

if ($missing.Count -eq 0) {
    Write-Host ""
    Write-Host "TUM DOSYALAR MEVCUT!" -ForegroundColor Green
    Write-Host "GitHub'a yuklemeye hazir!" -ForegroundColor Blue
    
    Write-Host ""
    $upload = Read-Host "Simdi yuklemek ister misiniz? (E/H)"
    if ($upload -eq "E" -or $upload -eq "e") {
        & ".\simple_upload.ps1"
    }
} else {
    Write-Host ""
    Write-Host "EKSIK DOSYALAR:" -ForegroundColor Red
    foreach ($file in $missing) {
        Write-Host "  - $file" -ForegroundColor Red
    }
    Write-Host ""
    Write-Host "Lutfen eksik dosyalari olusturun." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Kontrol tamamlandi!" -ForegroundColor Green