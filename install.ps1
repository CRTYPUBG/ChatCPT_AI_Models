# ChatCPT 3.0 - Temiz Kurulum Script
# Conflict'siz, temiz kurulum dosyası

Write-Host "ChatCPT 3.0 - Turkce AI Modeli Kurulumu Basliyor..." -ForegroundColor Green
Write-Host "=" * 60 -ForegroundColor Cyan

# Sistem kontrolü
Write-Host "Sistem kontrol ediliyor..." -ForegroundColor Yellow

# Python kontrolü
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Python bulundu: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "Python bulunamadi! Lutfen Python 3.7+ kurun." -ForegroundColor Red
    Write-Host "Indirme: https://www.python.org/downloads/" -ForegroundColor Blue
    exit 1
}

# Git kontrolü
try {
    $gitVersion = git --version 2>&1
    Write-Host "Git bulundu: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "Git bulunamadi! Lutfen Git kurun." -ForegroundColor Red
    Write-Host "Indirme: https://git-scm.com/download/win" -ForegroundColor Blue
    exit 1
}

# Kurulum dizini oluştur
$installDir = "$env:USERPROFILE\ChatCPT-3.0"
Write-Host "Kurulum dizini: $installDir" -ForegroundColor Blue

if (Test-Path $installDir) {
    Write-Host "Mevcut kurulum bulundu. Guncelleniyor..." -ForegroundColor Yellow
    Set-Location $installDir
    git pull origin main
} else {
    Write-Host "ChatCPT 3.0 indiriliyor..." -ForegroundColor Blue
    git clone https://github.com/CRTYPUBG/ChatCPT_AI_Models.git $installDir
    Set-Location $installDir
}

# Python sanal ortam oluştur
Write-Host "Python sanal ortami olusturuluyor..." -ForegroundColor Blue
python -m venv venv

# Sanal ortamı aktifleştir
Write-Host "Sanal ortam aktiflestirilyor..." -ForegroundColor Blue
& ".\venv\Scripts\Activate.ps1"

# Gerekli paketleri kur
Write-Host "Gerekli paketler kuruluyor..." -ForegroundColor Blue
pip install --upgrade pip
pip install -r requirements.txt

# Konfigürasyon dosyası oluştur
Write-Host "Konfigurasyon ayarlaniyor..." -ForegroundColor Blue

$configContent = @"
# ChatCPT 3.0 Konfigurasyonu
# Bu dosyayi duzenleyerek ayarlari degistirebilirsiniz

# Google API Ayarlari (Opsiyonel)
GOOGLE_API_KEY=your_api_key_here
GOOGLE_SEARCH_ENGINE_ID=your_search_engine_id_here

# Model Ayarlari
MODEL_NAME=ChatCPT-3.0
MODEL_VERSION=3.0
LANGUAGE=Turkish

# Sistem Ayarlari
AUTO_SAVE=true
DEBUG_MODE=false
MAX_MEMORY=1000
"@

$configContent | Out-File -FilePath "config.env" -Encoding UTF8

# Desktop kısayolu oluştur
Write-Host "Desktop kisayolu olusturuluyor..." -ForegroundColor Blue

$shortcutPath = "$env:USERPROFILE\Desktop\ChatCPT 3.0.lnk"
$targetPath = "powershell.exe"
$arguments = "-WindowStyle Normal -Command `"cd '$installDir'; .\venv\Scripts\Activate.ps1; python ai_model.py`""

$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut($shortcutPath)
$Shortcut.TargetPath = $targetPath
$Shortcut.Arguments = $arguments
$Shortcut.WorkingDirectory = $installDir
$Shortcut.IconLocation = "shell32.dll,25"
$Shortcut.Description = "ChatCPT 3.0 - Turkce AI Modeli"
$Shortcut.Save()

# Başlat menüsü kısayolu
$startMenuPath = "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\ChatCPT 3.0.lnk"
$StartShortcut = $WshShell.CreateShortcut($startMenuPath)
$StartShortcut.TargetPath = $targetPath
$StartShortcut.Arguments = $arguments
$StartShortcut.WorkingDirectory = $installDir
$StartShortcut.IconLocation = "shell32.dll,25"
$StartShortcut.Description = "ChatCPT 3.0 - Turkce AI Modeli"
$StartShortcut.Save()

# Kurulum tamamlandı
Write-Host ""
Write-Host "ChatCPT 3.0 Kurulumu Tamamlandi!" -ForegroundColor Green
Write-Host "=" * 60 -ForegroundColor Cyan
Write-Host ""
Write-Host "Kurulum Dizini: $installDir" -ForegroundColor Blue
Write-Host "Desktop Kisayolu: Olusturuldu" -ForegroundColor Green
Write-Host "Baslat Menusu: Olusturuldu" -ForegroundColor Green
Write-Host ""
Write-Host "Baslatma Secenekleri:" -ForegroundColor Yellow
Write-Host "   1. Desktop'taki 'ChatCPT 3.0' kisayoluna cift tiklayin" -ForegroundColor White
Write-Host "   2. Baslat menusunden 'ChatCPT 3.0' arayin" -ForegroundColor White
Write-Host "   3. Bu dizinde 'python ai_model.py' komutunu calistirin" -ForegroundColor White
Write-Host ""
Write-Host "Konfigurasyon:" -ForegroundColor Yellow
Write-Host "   Google API icin 'config.env' dosyasini duzenleyin" -ForegroundColor White
Write-Host ""
Write-Host "Dokumantasyon: README.md dosyasini okuyun" -ForegroundColor Blue
Write-Host ""

# Otomatik başlatma seçeneği
$autoStart = Read-Host "ChatCPT 3.0'i simdi baslatmak ister misiniz? (E/H)"
if ($autoStart -eq "E" -or $autoStart -eq "e") {
    Write-Host "ChatCPT 3.0 baslatiliyor..." -ForegroundColor Green
    python ai_model.py
}

Write-Host "Kurulum tamamlandi! ChatCPT 3.0'i kullanmaya baslayabilirsiniz." -ForegroundColor Green