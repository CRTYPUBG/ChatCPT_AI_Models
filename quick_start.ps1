# ChatCPT 3.0 - Hızlı Başlatma Scripti
# Bu script ChatCPT 3.0'ı hızlıca başlatır

param(
    [switch]$NoLogo,
    [switch]$Debug,
    [string]$ConfigFile = "config.env"
)

# Logo göster (eğer -NoLogo kullanılmamışsa)
if (-not $NoLogo) {
    Clear-Host
    Write-Host ""
    Write-Host "╔══════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
    Write-Host "║                                                              ║" -ForegroundColor Cyan
    Write-Host "║           🤖 ChatCPT 3.0 - TÜRKÇE AI MODELİ 🚀              ║" -ForegroundColor Green
    Write-Host "║                                                              ║" -ForegroundColor Cyan
    Write-Host "║                    Versiyon: 3.0                             ║" -ForegroundColor Yellow
    Write-Host "║                                                              ║" -ForegroundColor Cyan
    Write-Host "║  ✨ Gelişmiş Türkçe Dil Modeli                               ║" -ForegroundColor White
    Write-Host "║  🧠 Akıllı Yanıt Sistemi                                     ║" -ForegroundColor White
    Write-Host "║  🔍 Google Arama Entegrasyonu                                ║" -ForegroundColor White
    Write-Host "║  📚 Sürekli Öğrenme Yeteneği                                 ║" -ForegroundColor White
    Write-Host "║                                                              ║" -ForegroundColor Cyan
    Write-Host "╚══════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
    Write-Host ""
}

# Sistem kontrolü
Write-Host "🔍 Sistem kontrol ediliyor..." -ForegroundColor Yellow

# Python kontrolü
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Python: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python bulunamadı!" -ForegroundColor Red
    Write-Host "📥 Kurulum: https://www.python.org/downloads/" -ForegroundColor Blue
    Read-Host "Devam etmek için Enter'a basın"
    exit 1
}

# Gerekli dosyaları kontrol et
$requiredFiles = @("ai_model.py", "eğitim_verisi.json", "search_engine.py", "api_config.py")
$missingFiles = @()

foreach ($file in $requiredFiles) {
    if (-not (Test-Path $file)) {
        $missingFiles += $file
    }
}

if ($missingFiles.Count -gt 0) {
    Write-Host "❌ Eksik dosyalar:" -ForegroundColor Red
    foreach ($file in $missingFiles) {
        Write-Host "   - $file" -ForegroundColor Red
    }
    Write-Host "💡 Lütfen tüm dosyaların mevcut olduğundan emin olun." -ForegroundColor Yellow
    Read-Host "Devam etmek için Enter'a basın"
    exit 1
}

# Sanal ortam kontrolü
if (Test-Path "venv\Scripts\activate.bat") {
    Write-Host "⚡ Python sanal ortamı aktifleştiriliyor..." -ForegroundColor Blue
    & ".\venv\Scripts\Activate.ps1"
} else {
    Write-Host "⚠️ Sanal ortam bulunamadı. Global Python kullanılacak." -ForegroundColor Yellow
}

# Konfigürasyon kontrolü
if (Test-Path $ConfigFile) {
    Write-Host "⚙️ Konfigürasyon yüklendi: $ConfigFile" -ForegroundColor Green
} else {
    Write-Host "⚠️ Konfigürasyon dosyası bulunamadı: $ConfigFile" -ForegroundColor Yellow
    Write-Host "💡 Google API için config.env dosyasını oluşturun." -ForegroundColor Blue
}

# Debug modu
if ($Debug) {
    Write-Host "🐛 Debug modu aktif" -ForegroundColor Magenta
    $env:DEBUG_MODE = "true"
}

# ChatCPT 3.0'ı başlat
Write-Host "🚀 ChatCPT 3.0 başlatılıyor..." -ForegroundColor Green
Write-Host "💡 Çıkmak için sohbet modunda 'çıkış' yazın." -ForegroundColor Blue
Write-Host ""

try {
    python ai_model.py
} catch {
    Write-Host "❌ ChatCPT 3.0 başlatılırken hata oluştu!" -ForegroundColor Red
    Write-Host "💡 Gerekli Python paketlerinin kurulu olduğundan emin olun:" -ForegroundColor Yellow
    Write-Host "   pip install -r requirements.txt" -ForegroundColor White
}

Write-Host ""
Write-Host "👋 ChatCPT 3.0 sonlandırıldı." -ForegroundColor Green
Write-Host "🙏 Kullandığınız için teşekkürler!" -ForegroundColor Blue

# Pencereyi açık tut
if (-not $NoLogo) {
    Read-Host "Çıkmak için Enter'a basın"
}