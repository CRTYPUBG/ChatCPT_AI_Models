# ChatCPT 3.0 - Otomatik Kurulum Script
# Kullanım: iwr -useb https://raw.githubusercontent.com/CRTYPUBG/ChatCPT_AI_Models/main/install.ps1 | iex

Write-Host "🚀 ChatCPT 3.0 - Türkçe AI Modeli Kurulumu Başlıyor..." -ForegroundColor Green
Write-Host "=" * 60 -ForegroundColor Cyan

# Sistem kontrolü
Write-Host "🔍 Sistem kontrol ediliyor..." -ForegroundColor Yellow

# Python kontrolü
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Python bulundu: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python bulunamadı! Lütfen Python 3.7+ kurun." -ForegroundColor Red
    Write-Host "📥 İndirme: https://www.python.org/downloads/" -ForegroundColor Blue
    exit 1
}

# Git kontrolü
try {
    $gitVersion = git --version 2>&1
    Write-Host "✅ Git bulundu: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Git bulunamadı! Lütfen Git kurun." -ForegroundColor Red
    Write-Host "📥 İndirme: https://git-scm.com/download/win" -ForegroundColor Blue
    exit 1
}

# Kurulum dizini oluştur
$installDir = "$env:USERPROFILE\ChatCPT-3.0"
Write-Host "📁 Kurulum dizini: $installDir" -ForegroundColor Blue

if (Test-Path $installDir) {
    Write-Host "⚠️ Mevcut kurulum bulundu. Güncelleniyor..." -ForegroundColor Yellow
    Set-Location $installDir
    git pull origin main
} else {
    Write-Host "📥 ChatCPT 3.0 indiriliyor..." -ForegroundColor Blue
    git clone https://github.com/CRTYPUBG/ChatCPT_AI_Models.git $installDir
    Set-Location $installDir
}

# Python sanal ortam oluştur
Write-Host "🐍 Python sanal ortamı oluşturuluyor..." -ForegroundColor Blue
python -m venv venv

# Sanal ortamı aktifleştir
Write-Host "⚡ Sanal ortam aktifleştiriliyor..." -ForegroundColor Blue
& ".\venv\Scripts\Activate.ps1"

# Gerekli paketleri kur
Write-Host "📦 Gerekli paketler kuruluyor..." -ForegroundColor Blue
pip install --upgrade pip
pip install -r requirements.txt

# Konfigürasyon dosyası oluştur
Write-Host "⚙️ Konfigürasyon ayarlanıyor..." -ForegroundColor Blue

$configContent = @"
# ChatCPT 3.0 Konfigürasyonu
# Bu dosyayı düzenleyerek ayarları değiştirebilirsiniz

# Google API Ayarları (Opsiyonel)
GOOGLE_API_KEY=your_api_key_here
GOOGLE_SEARCH_ENGINE_ID=your_search_engine_id_here

# Model Ayarları
MODEL_NAME=ChatCPT-3.0
MODEL_VERSION=3.0
LANGUAGE=Turkish

# Sistem Ayarları
AUTO_SAVE=true
DEBUG_MODE=false
MAX_MEMORY=1000
"@

$configContent | Out-File -FilePath "config.env" -Encoding UTF8

# Desktop kısayolu oluştur
Write-Host "🖥️ Desktop kısayolu oluşturuluyor..." -ForegroundColor Blue

$shortcutPath = "$env:USERPROFILE\Desktop\ChatCPT 3.0.lnk"
$targetPath = "powershell.exe"
$arguments = "-WindowStyle Normal -Command `"cd '$installDir'; .\venv\Scripts\Activate.ps1; python ai_model.py`""

$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut($shortcutPath)
$Shortcut.TargetPath = $targetPath
$Shortcut.Arguments = $arguments
$Shortcut.WorkingDirectory = $installDir
$Shortcut.IconLocation = "shell32.dll,25"
$Shortcut.Description = "ChatCPT 3.0 - Türkçe AI Modeli"
$Shortcut.Save()

# Başlat menüsü kısayolu
$startMenuPath = "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\ChatCPT 3.0.lnk"
$StartShortcut = $WshShell.CreateShortcut($startMenuPath)
$StartShortcut.TargetPath = $targetPath
$StartShortcut.Arguments = $arguments
$StartShortcut.WorkingDirectory = $installDir
$StartShortcut.IconLocation = "shell32.dll,25"
$StartShortcut.Description = "ChatCPT 3.0 - Türkçe AI Modeli"
$StartShortcut.Save()

# Kurulum tamamlandı
Write-Host ""
Write-Host "🎉 ChatCPT 3.0 Kurulumu Tamamlandı!" -ForegroundColor Green
Write-Host "=" * 60 -ForegroundColor Cyan
Write-Host ""
Write-Host "📍 Kurulum Dizini: $installDir" -ForegroundColor Blue
Write-Host "🖥️ Desktop Kısayolu: Oluşturuldu" -ForegroundColor Green
Write-Host "📋 Başlat Menüsü: Oluşturuldu" -ForegroundColor Green
Write-Host ""
Write-Host "🚀 Başlatma Seçenekleri:" -ForegroundColor Yellow
Write-Host "   1. Desktop'taki 'ChatCPT 3.0' kısayoluna çift tıklayın" -ForegroundColor White
Write-Host "   2. Başlat menüsünden 'ChatCPT 3.0' arayın" -ForegroundColor White
Write-Host "   3. Bu dizinde 'python ai_model.py' komutunu çalıştırın" -ForegroundColor White
Write-Host ""
Write-Host "⚙️ Konfigürasyon:" -ForegroundColor Yellow
Write-Host "   Google API için 'config.env' dosyasını düzenleyin" -ForegroundColor White
Write-Host ""
Write-Host "📚 Dokümantasyon: README.md dosyasını okuyun" -ForegroundColor Blue
Write-Host ""

# Otomatik başlatma seçeneği
$autoStart = Read-Host "ChatCPT 3.0'ı şimdi başlatmak ister misiniz? (E/H)"
if ($autoStart -eq "E" -or $autoStart -eq "e") {
    Write-Host "🚀 ChatCPT 3.0 başlatılıyor..." -ForegroundColor Green
    python ai_model.py
}

Write-Host "👋 Kurulum tamamlandı! ChatCPT 3.0'ı kullanmaya başlayabilirsiniz." -ForegroundColor Green