# ChatCPT 3.0 - Dosya Kontrol Scripti
# Tüm gerekli dosyaların mevcut olup olmadığını kontrol eder

Write-Host ""
Write-Host "🔍 ChatCPT 3.0 - Dosya Kontrol Scripti" -ForegroundColor Green
Write-Host "=" * 50 -ForegroundColor Cyan
Write-Host ""

# Gerekli dosyalar listesi
$requiredFiles = @{
    "Ana AI Sistemi" = @(
        "ai_model.py",
        "search_engine.py", 
        "api_config.py",
        "eğitim_verisi.json"
    )
    "Kurulum Dosyaları" = @(
        "install.ps1",
        "quick_start.ps1",
        "start.bat",
        "requirements.txt"
    )
    "Dokümantasyon" = @(
        "README.md",
        "KURULUM.md",
        "LICENSE",
        ".gitignore",
        "config.env.example"
    )
    "Alternatif AI Sistemleri" = @(
        "basit_ai.py",
        "working_ai_system.py",
        "run_ai_system.py",
        "simple_ai_system.py"
    )
    "Gelişmiş Özellikler" = @(
        "free_search_engine.py",
        "cpu_ai_system.py",
        "cpu_trainer.py",
        "self_improving_ai.py",
        "CPT3.0.py"
    )
    "Konfigürasyon" = @(
        "config.py",
        "knowledge_base.json"
    )
    "Upload Scriptleri" = @(
        "upload_to_github.ps1",
        "upload_to_github.bat",
        "check_files.ps1"
    )
}

$totalFiles = 0
$existingFiles = 0
$missingFiles = @()

foreach ($category in $requiredFiles.Keys) {
    Write-Host "📁 $category:" -ForegroundColor Yellow
    
    foreach ($file in $requiredFiles[$category]) {
        $totalFiles++
        
        if (Test-Path $file) {
            $fileSize = (Get-Item $file).Length
            $fileSizeKB = [math]::Round($fileSize / 1024, 2)
            Write-Host "   ✅ $file ($fileSizeKB KB)" -ForegroundColor Green
            $existingFiles++
        } else {
            Write-Host "   ❌ $file - EKSIK!" -ForegroundColor Red
            $missingFiles += $file
        }
    }
    Write-Host ""
}

# Özet
Write-Host "📊 ÖZET:" -ForegroundColor Blue
Write-Host "=" * 30 -ForegroundColor Cyan
Write-Host "✅ Mevcut dosyalar: $existingFiles" -ForegroundColor Green
Write-Host "❌ Eksik dosyalar: $($missingFiles.Count)" -ForegroundColor Red
Write-Host "📁 Toplam dosya: $totalFiles" -ForegroundColor Blue
Write-Host "📈 Tamamlanma oranı: $([math]::Round(($existingFiles / $totalFiles) * 100, 1))%" -ForegroundColor Yellow

if ($missingFiles.Count -gt 0) {
    Write-Host ""
    Write-Host "⚠️ EKSIK DOSYALAR:" -ForegroundColor Red
    foreach ($file in $missingFiles) {
        Write-Host "   • $file" -ForegroundColor Red
    }
    
    Write-Host ""
    Write-Host "💡 Bu dosyaları oluşturmak için:" -ForegroundColor Yellow
    Write-Host "   1. Kiro IDE'de dosyaları kontrol edin" -ForegroundColor White
    Write-Host "   2. Eksik dosyaları yeniden oluşturun" -ForegroundColor White
    Write-Host "   3. Bu scripti tekrar çalıştırın" -ForegroundColor White
} else {
    Write-Host ""
    Write-Host "🎉 TÜM DOSYALAR MEVCUT!" -ForegroundColor Green
    Write-Host "🚀 GitHub'a yüklemeye hazır!" -ForegroundColor Blue
    
    Write-Host ""
    $upload = Read-Host "Şimdi GitHub'a yüklemek ister misiniz? (E/H)"
    if ($upload -eq "E" -or $upload -eq "e") {
        Write-Host "🚀 GitHub upload scripti çalıştırılıyor..." -ForegroundColor Green
        & ".\upload_to_github.ps1"
    }
}

Write-Host ""
Write-Host "👋 Dosya kontrolü tamamlandı!" -ForegroundColor Green