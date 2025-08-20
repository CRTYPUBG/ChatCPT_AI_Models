#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kendini Geliştiren AI Sistemi - Ana Başlatıcı
Bu script tüm sistemi başlatır ve kullanıcı arayüzünü sağlar
"""

import os
import sys
import time
from datetime import datetime

def check_requirements():
    """
    Gerekli kütüphaneleri kontrol eder
    """
    # Temel kütüphaneler
    basic_packages = {
        'torch': 'torch',
        'transformers': 'transformers', 
        'datasets': 'datasets',
        'requests': 'requests',
        'beautifulsoup4': 'bs4'  # beautifulsoup4 paketi bs4 olarak import edilir
    }
    
    missing_packages = []
    
    print("📦 Kütüphane kontrolü:")
    for package_name, import_name in basic_packages.items():
        try:
            __import__(import_name)
            print(f"   ✅ {package_name}")
        except ImportError:
            print(f"   ❌ {package_name}")
            missing_packages.append(package_name)
    
    # Unsloth'u ayrı kontrol et (CUDA hatası verebilir)
    try:
        import unsloth
        print("   ✅ unsloth (GPU modu)")
    except Exception as e:
        if "CUDA" in str(e) or "Torch not compiled with CUDA" in str(e):
            print("   ⚠️ unsloth (CUDA hatası - CPU modunda çalışacak)")
        else:
            print("   ❌ unsloth (yüklü değil)")
            # Unsloth olmadan da çalışabiliriz
    
    if missing_packages:
        print(f"\n❌ Eksik kütüphaneler: {', '.join(missing_packages)}")
        print("Kurulum için:")
        print(f"pip install {' '.join(missing_packages)}")
        return False
    
    print("✅ Tüm temel kütüphaneler mevcut!")
    return True

def display_banner():
    """
    Sistem başlangıç banner'ını gösterir
    """
    banner = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║        🤖 KENDİNİ GELİŞTİREN AI SİSTEMİ v1.0 🚀            ║
║                                                              ║
║  • Google Search API Entegrasyonu                           ║
║  • Dinamik Öğrenme Sistemi                                  ║
║  • Bilgi Tabanı Yönetimi                                    ║
║  • Türkçe Dil Desteği                                       ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""
    print(banner)

def show_system_info():
    """
    Sistem bilgilerini gösterir
    """
    from api_config import is_api_configured
    
    print("📊 **Sistem Durumu:**")
    print(f"   🕒 Başlatma Zamanı: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"   🐍 Python Sürümü: {sys.version.split()[0]}")
    print(f"   📁 Çalışma Dizini: {os.getcwd()}")
    
    if is_api_configured():
        print("   🔍 Arama Motoru: Google Search API ✅")
    else:
        print("   🔍 Arama Motoru: Ücretsiz (DuckDuckGo + Wikipedia) ⚠️")
        print("   💡 Google API için api_config.py dosyasını düzenleyin")
    
    print()

def main_menu():
    """
    Ana menüyü gösterir
    """
    while True:
        print("\n" + "="*60)
        print("🎯 **ANA MENÜ**")
        print("="*60)
        print("1. 🤖 AI Sohbet Modunu Başlat")
        print("2. 🏋️ Modeli Eğit (CPT3.0.py)")
        print("3. 📊 Sistem İstatistikleri")
        print("4. ⚙️ Konfigürasyon Kontrolü")
        print("5. 🧪 Arama Motoru Testi")
        print("6. 📚 Bilgi Tabanını Görüntüle")
        print("7. 🚀 Kendini Geliştirme Başlat")
        print("8. ❌ Çıkış")
        print("="*60)
        
        choice = input("👤 Seçiminiz (1-8): ").strip()
        
        if choice == "1":
            start_ai_chat()
        elif choice == "2":
            train_model()
        elif choice == "3":
            show_system_stats()
        elif choice == "4":
            check_configuration()
        elif choice == "5":
            test_search_engine()
        elif choice == "6":
            view_knowledge_base()
        elif choice == "7":
            start_self_improvement()
        elif choice == "8":
            print("👋 Görüşmek üzere!")
            break
        else:
            print("❌ Geçersiz seçim! Lütfen 1-8 arası bir sayı girin.")

def start_ai_chat():
    """
    AI sohbet modunu başlatır
    """
    try:
        print("\n🚀 AI Sohbet Modu Başlatılıyor...")
        
        # Önce GPU modunu dene
        try:
            from self_improving_ai import SelfImprovingAI
            ai_system = SelfImprovingAI()
            ai_system.interactive_chat()
        except Exception as gpu_error:
            if "CUDA" in str(gpu_error) or "unsloth" in str(gpu_error).lower() or "transformers" in str(gpu_error).lower():
                print("⚠️ GPU/Transformers modu çalışmıyor, çalışan AI sistemine geçiliyor...")
                from working_ai_system import WorkingAISystem
                ai_system = WorkingAISystem()
                ai_system.interactive_chat()
            else:
                raise gpu_error
        
    except Exception as e:
        print(f"❌ AI sistemi başlatılırken hata: {e}")
        print("💡 Gerekli kütüphanelerin kurulu olduğundan emin olun")

def train_model():
    """
    Model eğitimini başlatır
    """
    print("\n🏋️ Model Eğitimi Başlatılıyor...")
    print("Seçenekler:")
    print("1. GPU Modu (Unsloth + Mistral 7B) - Hızlı ama GPU gerektirir")
    print("2. CPU Modu (DialoGPT) - Yavaş ama GPU gerektirmez")
    
    choice = input("Hangi modu seçiyorsunuz? (1/2): ").strip()
    
    if choice == "1":
        print("⚠️ GPU modu seçildi - CUDA gerektirir!")
        confirm = input("Devam etmek istiyor musunuz? (e/h): ").lower()
        if confirm == 'e':
            try:
                import subprocess
                result = subprocess.run([sys.executable, "CPT3.0.py"], 
                                      capture_output=True, text=True)
                
                if result.returncode == 0:
                    print("✅ GPU model eğitimi başarıyla tamamlandı!")
                else:
                    print(f"❌ GPU eğitim hatası: {result.stderr}")
                    
            except Exception as e:
                print(f"❌ GPU eğitimi başlatılırken hata: {e}")
        else:
            print("❌ GPU eğitimi iptal edildi.")
    
    elif choice == "2":
        print("⚙️ CPU modu seçildi - GPU gerektirmez ama yavaştır")
        confirm = input("Devam etmek istiyor musunuz? (e/h): ").lower()
        if confirm == 'e':
            try:
                import subprocess
                result = subprocess.run([sys.executable, "cpu_trainer.py"], 
                                      capture_output=True, text=True)
                
                if result.returncode == 0:
                    print("✅ CPU model eğitimi başarıyla tamamlandı!")
                    print(result.stdout)
                else:
                    print(f"❌ CPU eğitim hatası: {result.stderr}")
                    
            except Exception as e:
                print(f"❌ CPU eğitimi başlatılırken hata: {e}")
        else:
            print("❌ CPU eğitimi iptal edildi.")
    
    else:
        print("❌ Geçersiz seçim!")

def show_system_stats():
    """
    Sistem istatistiklerini gösterir
    """
    try:
        # Önce GPU modunu dene
        try:
            from self_improving_ai import SelfImprovingAI
            ai_system = SelfImprovingAI()
            stats = ai_system.get_stats()
        except Exception as gpu_error:
            if "CUDA" in str(gpu_error) or "transformers" in str(gpu_error).lower():
                print("⚠️ GPU/Transformers modu çalışmıyor, çalışan AI sisteminden istatistikler alınıyor...")
                from working_ai_system import WorkingAISystem
                ai_system = WorkingAISystem()
                stats = ai_system.get_stats()
            else:
                raise gpu_error
        
        print("\n📊 **Sistem İstatistikleri:**")
        print("-" * 40)
        for key, value in stats.items():
            print(f"   {key}: {value}")
        
    except Exception as e:
        print(f"❌ İstatistikler alınırken hata: {e}")

def check_configuration():
    """
    Konfigürasyon kontrolü yapar
    """
    print("\n⚙️ **Konfigürasyon Kontrolü:**")
    print("-" * 40)
    
    try:
        from api_config import is_api_configured, GOOGLE_API_CONFIG
        
        if is_api_configured():
            print("✅ Google API yapılandırması: Tamamlanmış")
        else:
            print("❌ Google API yapılandırması: Eksik")
            print("💡 api_config.py dosyasını düzenleyin")
        
        # Dosya kontrolü
        files_to_check = [
            "eğitim_verisi.json",
            "config.py",
            "CPT3.0.py",
            "self_improving_ai.py",
            "search_engine.py",
            "free_search_engine.py"
        ]
        
        print("\n📁 **Dosya Kontrolü:**")
        for file in files_to_check:
            if os.path.exists(file):
                print(f"   ✅ {file}")
            else:
                print(f"   ❌ {file} - Eksik!")
        
    except Exception as e:
        print(f"❌ Konfigürasyon kontrolünde hata: {e}")

def test_search_engine():
    """
    Arama motorunu test eder
    """
    print("\n🧪 **Arama Motoru Testi:**")
    print("-" * 40)
    
    try:
        from api_config import is_api_configured
        
        if is_api_configured():
            from search_engine import GoogleSearchEngine
            search_engine = GoogleSearchEngine()
            results = search_engine.search("yapay zeka test", num_results=2)
            print("🔍 Google Search API Testi:")
        else:
            from free_search_engine import FreeSearchEngine
            search_engine = FreeSearchEngine()
            results = search_engine.comprehensive_search("yapay zeka test", num_results=2)
            print("🔍 Ücretsiz Arama Motoru Testi:")
        
        if results:
            for i, result in enumerate(results, 1):
                print(f"   {i}. {result.get('title', 'Başlık yok')}")
                print(f"      {result.get('snippet', 'Açıklama yok')[:100]}...")
        else:
            print("   ❌ Arama sonucu bulunamadı")
            
    except Exception as e:
        print(f"❌ Arama motoru testinde hata: {e}")

def view_knowledge_base():
    """
    Bilgi tabanını görüntüler
    """
    try:
        import json
        
        if os.path.exists("knowledge_base.json"):
            with open("knowledge_base.json", 'r', encoding='utf-8') as f:
                kb = json.load(f)
            
            print("\n📚 **Bilgi Tabanı:**")
            print("-" * 40)
            print(f"   📊 Toplam Öğrenilen Bilgi: {len(kb.get('learned_facts', {}))}")
            print(f"   🕒 Son Güncelleme: {kb.get('last_update', 'Bilinmiyor')}")
            print(f"   📈 İyileştirme Oturumları: {len(kb.get('improvement_log', []))}")
            
            if kb.get('learned_facts'):
                print("\n   🔍 **Son Öğrenilen Konular:**")
                for i, (topic, info) in enumerate(list(kb['learned_facts'].items())[-5:], 1):
                    print(f"      {i}. {topic.replace('_', ' ').title()}")
        else:
            print("❌ Bilgi tabanı dosyası bulunamadı")
            
    except Exception as e:
        print(f"❌ Bilgi tabanı görüntülenirken hata: {e}")

def start_self_improvement():
    """
    Kendini geliştirme sürecini başlatır
    """
    print("\n🚀 **Kendini Geliştirme Süreci:**")
    print("-" * 40)
    
    try:
        # Önce GPU modunu dene
        try:
            from self_improving_ai import SelfImprovingAI
            ai_system = SelfImprovingAI()
            ai_system.self_improve()
        except Exception as gpu_error:
            if "CUDA" in str(gpu_error) or "transformers" in str(gpu_error).lower():
                print("⚠️ GPU/Transformers modu çalışmıyor, çalışan AI sistemine geçiliyor...")
                from working_ai_system import WorkingAISystem
                ai_system = WorkingAISystem()
                ai_system.self_improve()
            else:
                raise gpu_error
        
        print("✅ Kendini geliştirme süreci tamamlandı!")
        
    except Exception as e:
        print(f"❌ Kendini geliştirme sürecinde hata: {e}")

def main():
    """
    Ana program
    """
    # Banner göster
    display_banner()
    
    # Gereksinimler kontrolü
    if not check_requirements():
        print("\n❌ Gerekli kütüphaneler eksik. Lütfen kurulumu tamamlayın.")
        return
    
    # Sistem bilgileri
    show_system_info()
    
    # Ana menü
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\n👋 Program kullanıcı tarafından sonlandırıldı.")
    except Exception as e:
        print(f"\n❌ Beklenmeyen hata: {e}")

if __name__ == "__main__":
    main()