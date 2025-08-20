# Git Remote Düzeltme Scripti

Write-Host "Git Remote Duzeltme Scripti" -ForegroundColor Green
Write-Host "===========================" -ForegroundColor Cyan
Write-Host ""

# Mevcut remote'ları göster
Write-Host "Mevcut remote'lar:" -ForegroundColor Blue
git remote -v

Write-Host ""
Write-Host "Eski remote'u kaldiriliyor..." -ForegroundColor Yellow
git remote remove origin

Write-Host "Yeni remote ekleniyor..." -ForegroundColor Blue
git remote add origin https://github.com/CRTYPUBG/ChatCPT_AI_Models.git

Write-Host "Yeni remote kontrol ediliyor:" -ForegroundColor Green
git remote -v

Write-Host ""
Write-Host "Git remote duzeltildi!" -ForegroundColor Green
Write-Host "Simdi upload yapabilirsiniz:" -ForegroundColor Yellow
Write-Host "  .\simple_upload.ps1" -ForegroundColor White