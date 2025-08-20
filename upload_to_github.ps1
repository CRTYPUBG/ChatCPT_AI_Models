# ChatCPT 3.0 - GitHub Upload PowerShell Script
# Tüm dosyaları GitHub'a yükler

Write-Host ""
Write-Host "╔══════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║                                                              ║" -ForegroundColor Cyan
Write-Host "║        🚀 ChatCPT 3.0 - GitHub Upload Script 📤            ║" -ForegroundColor Green
Write-Host "║                                                              ║" -ForegroundColor Cyan
Write-Host "║           Tüm dosyalar GitHub'a yüklenecek                   ║" -ForegroundColor Yellow
Write-Host "║                                                              ║" -ForegroundColor Cyan
Write-Host "╚══════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Git kontrolü
try {
    $gitVersion = git --version 2>&1
    Write-Host "✅ Git bulundu: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Git bulunamadı! Lütfen Git kurun." -ForegroundColor Red
    Write-Host "📥 İndirme: https://git-scm.com/download/win" -ForegroundColor Blue
    Read-Host "Devam etmek için Enter'a basın"
    exit 1
}

# Repo bilgileri
$repoUrl = "https://github.com/CRTYPUBG/ChatCPT_AI_Models.git"
$repoName = "ChatCPT_AI_Models"

Write-Host "📋 Repo Bilgileri:" -ForegroundColor Blue
Write-Host "   URL: $repoUrl" -ForegroundColor White
Write-Host "   İsim: $repoName" -ForegroundColor White
Write-Host ""

# Git repo kontrolü
if (Test-Path ".git") {
    Write-Host "⚠️ Mevcut Git repo bulundu. Güncelleme yapılacak..." -ForegroundColor Yellow
    git status
    Write-Host ""
} else {
    Write-Host "🆕 Yeni Git repo başlatılıyor..." -ForegroundColor Blue
    git init
    git remote add origin $repoUrl
    Write-Host ""
}

# Dosya kontrolü
Write-Host "📁 Yüklenecek dosyalar kontrol ediliyor..." -ForegroundColor Blue

$criticalFiles = @(
    "ai_model.py",
    "search_engine.py", 
    "api_config.py",
    "eğitim_verisi.json",
    "install.ps1",
    "README.md",
    "requirements.txt"
)

$allFiles = @(
    "ai_model.py",
    "search_engine.py",
    "api_config.py", 
    "eğitim_verisi.json",
    "install.ps1",
    "quick_start.ps1",
    "start.bat",
    "README.md",
    "KURULUM.md",
    "requirements.txt",
    "LICENSE",
    ".gitignore",
    "config.env.example",
    "basit_ai.py",
    "working_ai_system.py",
    "run_ai_system.py",
    "free_search_engine.py",
    "knowledge_base.json",
    "CPT3.0.py",
    "cpu_ai_system.py",
    "cpu_trainer.py",
    "simple_ai_system.py",
    "self_improving_ai.py",
    "config.py"
)

Write-Host "🔍 Kritik dosyalar:" -ForegroundColor Yellow
foreach ($file in $criticalFiles) {
    if (Test-Path $file) {
        Write-Host "   ✅ $file" -ForegroundColor Green
    } else {
        Write-Host "   ❌ $file - EKSIK!" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "📦 Tüm dosyalar:" -ForegroundColor Yellow
$existingFiles = 0
foreach ($file in $allFiles) {
    if (Test-Path $file) {
        Write-Host "   ✅ $file" -ForegroundColor Green
        $existingFiles++
    } else {
        Write-Host "   ⚠️ $file - Yok" -ForegroundColor DarkYellow
    }
}

Write-Host ""
Write-Host "📊 Toplam: $existingFiles/$($allFiles.Count) dosya mevcut" -ForegroundColor Blue

# Kullanıcı onayı
Write-Host ""
$confirm = Read-Host "Tüm dosyaları GitHub'a yüklemek istiyor musunuz? (E/H)"
if ($confirm -ne "E" -and $confirm -ne "e") {
    Write-Host "❌ İşlem iptal edildi." -ForegroundColor Red
    exit
}

Write-Host ""
Write-Host "📦 Tüm dosyalar Git'e ekleniyor..." -ForegroundColor Blue

# Git add
git add .

Write-Host "📝 Commit mesajı oluşturuluyor..." -ForegroundColor Blue

# Commit mesajı
$commitMessage = @"
ChatCPT 3.0 - Türkçe AI Modeli - Tam Sürüm

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

📁 Ana Dosyalar:
- ai_model.py (ChatCPT 3.0 ana modeli)
- search_engine.py (Google arama entegrasyonu)
- eğitim_verisi.json (40+ Türkçe eğitim verisi)
- install.ps1 (Otomatik kurulum scripti)
- README.md (Kapsamlı dokümantasyon)
- requirements.txt (Python paket listesi)

🔧 Yardımcı Dosyalar:
- quick_start.ps1 (Hızlı başlatma)
- start.bat (Windows başlatıcı)
- KURULUM.md (Kurulum kılavuzu)
- working_ai_system.py (Alternatif AI sistemi)
- basit_ai.py (Basit AI versiyonu)

⚙️ Konfigürasyon:
- api_config.py (API ayarları)
- config.env.example (Konfigürasyon örneği)
- .gitignore (Git ignore kuralları)
- LICENSE (MIT lisansı)

🤖 ChatCPT 3.0 - Türkçe yapay zeka deneyiminin geleceği!
"@

# Commit yap
git commit -m $commitMessage

Write-Host ""
Write-Host "🚀 GitHub'a yükleniyor..." -ForegroundColor Green

# Push yap
git branch -M main
$pushResult = git push -u origin main 2>&1

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "✅ Başarıyla yüklendi!" -ForegroundColor Green
    Write-Host ""
    Write-Host "🌐 GitHub Repo: https://github.com/CRTYPUBG/ChatCPT_AI_Models" -ForegroundColor Blue
    Write-Host ""
    Write-Host "📥 Kullanıcılar için kurulum komutu:" -ForegroundColor Yellow
    Write-Host "iwr -useb https://raw.githubusercontent.com/CRTYPUBG/ChatCPT_AI_Models/main/install.ps1 | iex" -ForegroundColor White
    Write-Host ""
    Write-Host "🎯 Özellikler:" -ForegroundColor Yellow
    Write-Host "   • Tek komut kurulum" -ForegroundColor White
    Write-Host "   • Otomatik kısayol oluşturma" -ForegroundColor White
    Write-Host "   • Python sanal ortam" -ForegroundColor White
    Write-Host "   • Google API entegrasyonu" -ForegroundColor White
    Write-Host "   • Türkçe AI modeli" -ForegroundColor White
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "❌ Yükleme hatası!" -ForegroundColor Red
    Write-Host "💡 Olası nedenler:" -ForegroundColor Yellow
    Write-Host "   • GitHub kimlik doğrulaması gerekli" -ForegroundColor White
    Write-Host "   • İnternet bağlantısı sorunu" -ForegroundColor White
    Write-Host "   • Repo erişim izni sorunu" -ForegroundColor White
    Write-Host ""
    Write-Host "🔧 Çözüm önerileri:" -ForegroundColor Yellow
    Write-Host "   • GitHub Desktop kullanın" -ForegroundColor White
    Write-Host "   • Git credentials ayarlayın" -ForegroundColor White
    Write-Host "   • SSH key ekleyin" -ForegroundColor White
    Write-Host ""
}

Write-Host "📊 Son durum kontrol ediliyor..." -ForegroundColor Blue
git status

Write-Host ""
Write-Host "👋 Upload işlemi tamamlandı!" -ForegroundColor Green
Read-Host "Çıkmak için Enter'a basın"