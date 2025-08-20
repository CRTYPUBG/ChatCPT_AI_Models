# ChatCPT 3.0 - GitHub Hazırlık Master Script
# Tüm dosyaları kontrol eder, eksikleri bildirir ve GitHub'a yüklemeye hazırlar

param(
    [switch]$AutoUpload,
    [switch]$SkipCheck
)

function Show-Banner {
    Clear-Host
    Write-Host ""
    Write-Host "╔══════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
    Write-Host "║                                                              ║" -ForegroundColor Cyan
    Write-Host "║      🚀 ChatCPT 3.0 - GitHub Hazırlık Master Script 📦     ║" -ForegroundColor Green
    Write-Host "║                                                              ║" -ForegroundColor Cyan
    Write-Host "║           Tüm dosyalar kontrol edilip yüklenecek             ║" -ForegroundColor Yellow
    Write-Host "║                                                              ║" -ForegroundColor Cyan
    Write-Host "╚══════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
    Write-Host ""
}

function Test-Prerequisites {
    Write-Host "🔍 Ön koşullar kontrol ediliyor..." -ForegroundColor Blue
    
    # Git kontrolü
    try {
        $gitVersion = git --version 2>&1
        Write-Host "✅ Git: $gitVersion" -ForegroundColor Green
    } catch {
        Write-Host "❌ Git bulunamadı!" -ForegroundColor Red
        return $false
    }
    
    # PowerShell sürümü
    $psVersion = $PSVersionTable.PSVersion
    Write-Host "✅ PowerShell: $psVersion" -ForegroundColor Green
    
    return $true
}

function Get-ProjectFiles {
    return @{
        "Ana AI Sistemi" = @(
            @{Name="ai_model.py"; Critical=$true; Description="ChatCPT 3.0 ana AI modeli"},
            @{Name="search_engine.py"; Critical=$true; Description="Google Search API entegrasyonu"},
            @{Name="api_config.py"; Critical=$true; Description="API konfigürasyon yöneticisi"},
            @{Name="eğitim_verisi.json"; Critical=$true; Description="Türkçe eğitim verisi (40+ örnek)"}
        )
        "Kurulum Sistemi" = @(
            @{Name="install.ps1"; Critical=$true; Description="Otomatik kurulum scripti"},
            @{Name="quick_start.ps1"; Critical=$false; Description="Hızlı başlatma scripti"},
            @{Name="start.bat"; Critical=$false; Description="Windows başlatıcı"},
            @{Name="requirements.txt"; Critical=$true; Description="Python paket listesi"}
        )
        "Dokümantasyon" = @(
            @{Name="README.md"; Critical=$true; Description="Ana dokümantasyon"},
            @{Name="KURULUM.md"; Critical=$false; Description="Kurulum kılavuzu"},
            @{Name="LICENSE"; Critical=$false; Description="MIT lisansı"},
            @{Name=".gitignore"; Critical=$true; Description="Git ignore kuralları"},
            @{Name="config.env.example"; Critical=$false; Description="Konfigürasyon örneği"}
        )
        "Alternatif Sistemler" = @(
            @{Name="basit_ai.py"; Critical=$false; Description="Basit AI sistemi"},
            @{Name="working_ai_system.py"; Critical=$false; Description="Çalışan AI sistemi"},
            @{Name="run_ai_system.py"; Critical=$false; Description="Ana sistem yöneticisi"},
            @{Name="simple_ai_system.py"; Critical=$false; Description="Basit AI arayüzü"}
        )
        "Gelişmiş Özellikler" = @(
            @{Name="free_search_engine.py"; Critical=$false; Description="Ücretsiz arama motoru"},
            @{Name="cpu_ai_system.py"; Critical=$false; Description="CPU AI sistemi"},
            @{Name="cpu_trainer.py"; Critical=$false; Description="CPU model eğitimi"},
            @{Name="self_improving_ai.py"; Critical=$false; Description="Kendini geliştiren AI"},
            @{Name="CPT3.0.py"; Critical=$false; Description="Orijinal CPT3.0 sistemi"}
        )
        "Konfigürasyon" = @(
            @{Name="config.py"; Critical=$false; Description="Sistem konfigürasyonu"},
            @{Name="knowledge_base.json"; Critical=$false; Description="Bilgi tabanı"}
        )
        "Upload Araçları" = @(
            @{Name="upload_to_github.ps1"; Critical=$false; Description="PowerShell upload scripti"},
            @{Name="upload_to_github.bat"; Critical=$false; Description="Batch upload scripti"},
            @{Name="check_files.ps1"; Critical=$false; Description="Dosya kontrol scripti"},
            @{Name="prepare_for_github.ps1"; Critical=$false; Description="Master hazırlık scripti"}
        )
    }
}

function Test-ProjectFiles {
    $projectFiles = Get-ProjectFiles
    $stats = @{
        Total = 0
        Existing = 0
        Critical = 0
        CriticalMissing = 0
        Missing = @()
    }
    
    foreach ($category in $projectFiles.Keys) {
        Write-Host "$category" -ForegroundColor Yellow
        
        foreach ($fileInfo in $projectFiles[$category]) {
            $fileName = $fileInfo.Name
            $isCritical = $fileInfo.Critical
            $description = $fileInfo.Description
            
            $stats.Total++
            if ($isCritical) { $stats.Critical++ }
            
            if (Test-Path $fileName) {
                $fileSize = (Get-Item $fileName).Length
                $fileSizeKB = [math]::Round($fileSize / 1024, 2)
                $criticalMark = if ($isCritical) { "[KRITIK]" } else { "" }
                Write-Host "   ✅ $fileName ($fileSizeKB KB) $criticalMark" -ForegroundColor Green
                Write-Host "      💬 $description" -ForegroundColor DarkGray
                $stats.Existing++
            } else {
                $criticalMark = if ($isCritical) { "[KRITIK EKSIK]" } else { "" }
                Write-Host "   ❌ $fileName - EKSIK! $criticalMark" -ForegroundColor Red
                Write-Host "      💬 $description" -ForegroundColor DarkGray
                $stats.Missing += $fileName
                if ($isCritical) { $stats.CriticalMissing++ }
            }
        }
        Write-Host ""
    }
    
    return $stats
}

function Show-Statistics($stats) {
    Write-Host "📊 PROJE İSTATİSTİKLERİ:" -ForegroundColor Blue
    Write-Host "=" * 40 -ForegroundColor Cyan
    Write-Host "📁 Toplam dosya: $($stats.Total)" -ForegroundColor White
    Write-Host "✅ Mevcut dosya: $($stats.Existing)" -ForegroundColor Green
    Write-Host "❌ Eksik dosya: $($stats.Missing.Count)" -ForegroundColor Red
    Write-Host "🔥 Kritik dosya: $($stats.Critical)" -ForegroundColor Yellow
    Write-Host "⚠️ Eksik kritik: $($stats.CriticalMissing)" -ForegroundColor Red
    Write-Host "📈 Tamamlanma: $([math]::Round(($stats.Existing / $stats.Total) * 100, 1))%" -ForegroundColor Blue
    Write-Host "🎯 Kritik tamamlanma: $([math]::Round((($stats.Critical - $stats.CriticalMissing) / $stats.Critical) * 100, 1))%" -ForegroundColor Yellow
}

function Show-ReadyStatus($stats) {
    Write-Host ""
    if ($stats.CriticalMissing -eq 0) {
        Write-Host "🎉 PROJE GITHUB'A YÜKLEMEYE HAZIR!" -ForegroundColor Green
        Write-Host "✅ Tüm kritik dosyalar mevcut" -ForegroundColor Green
        
        if ($stats.Missing.Count -gt 0) {
            Write-Host "⚠️ $($stats.Missing.Count) opsiyonel dosya eksik ama sorun değil" -ForegroundColor Yellow
        }
        
        return $true
    } else {
        Write-Host "❌ PROJE HENÜZ HAZIR DEĞİL!" -ForegroundColor Red
        Write-Host "🔥 $($stats.CriticalMissing) kritik dosya eksik" -ForegroundColor Red
        
        Write-Host ""
        Write-Host "⚠️ EKSIK KRİTİK DOSYALAR:" -ForegroundColor Red
        foreach ($file in $stats.Missing) {
            $projectFiles = Get-ProjectFiles
            foreach ($category in $projectFiles.Keys) {
                foreach ($fileInfo in $projectFiles[$category]) {
                    if ($fileInfo.Name -eq $file -and $fileInfo.Critical) {
                        Write-Host "   [KRITIK] $file - $($fileInfo.Description)" -ForegroundColor Red
                    }
                }
            }
        }
        
        return $false
    }
}

# Ana script başlangıcı
Show-Banner

if (-not $SkipCheck) {
    if (-not (Test-Prerequisites)) {
        Write-Host "❌ Ön koşullar karşılanmadı!" -ForegroundColor Red
        exit 1
    }
}

Write-Host "🔍 Proje dosyaları kontrol ediliyor..." -ForegroundColor Blue
Write-Host ""

$stats = Test-ProjectFiles

Show-Statistics $stats

$isReady = Show-ReadyStatus $stats

if ($isReady) {
    Write-Host ""
    Write-Host "🚀 GitHub Repo Bilgileri:" -ForegroundColor Blue
    Write-Host "   📍 URL: https://github.com/CRTYPUBG/ChatCPT_AI_Models" -ForegroundColor White
    Write-Host "   📥 Kurulum: iwr -useb https://raw.githubusercontent.com/CRTYPUBG/ChatCPT_AI_Models/main/install.ps1 | iex" -ForegroundColor White
    
    if ($AutoUpload) {
        Write-Host ""
        Write-Host "🚀 Otomatik yükleme başlatılıyor..." -ForegroundColor Green
        & ".\upload_to_github.ps1"
    } else {
        Write-Host ""
        $upload = Read-Host "GitHub'a yüklemek ister misiniz? (E/H)"
        if ($upload -eq "E" -or $upload -eq "e") {
            Write-Host "🚀 GitHub upload scripti çalıştırılıyor..." -ForegroundColor Green
            & ".\upload_to_github.ps1"
        }
    }
} else {
    Write-Host ""
    Write-Host "💡 Yapılması gerekenler:" -ForegroundColor Yellow
    Write-Host "   1. Eksik kritik dosyaları oluşturun" -ForegroundColor White
    Write-Host "   2. Bu scripti tekrar çalıştırın" -ForegroundColor White
    Write-Host "   3. Hazır olduğunda GitHub'a yükleyin" -ForegroundColor White
}

Write-Host ""
Write-Host "👋 GitHub hazırlık işlemi tamamlandı!" -ForegroundColor Green