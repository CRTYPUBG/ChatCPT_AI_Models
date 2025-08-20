# Google Search API Konfigürasyonu
"""
Google Custom Search API kullanmak için:

1. Google Cloud Console'a gidin: https://console.cloud.google.com/
2. Yeni bir proje oluşturun veya mevcut projeyi seçin
3. "APIs & Services" > "Library" bölümüne gidin
4. "Custom Search API"yi etkinleştirin
5. "Credentials" bölümünden API key oluşturun
6. Custom Search Engine oluşturun: https://cse.google.com/
7. Aşağıdaki değerleri güncelleyin
"""

# Google API Konfigürasyonu
GOOGLE_API_CONFIG = {
    # Google Cloud Console'dan alacağınız API key
    "api_key": "AIzaSyClRGy008rrFUp38-5djGdKoy4srD0igng",
    
    # Custom Search Engine ID (https://cse.google.com/ adresinden)
    "search_engine_id": "4392d26beb40c4053",
    
    # Arama parametreleri
    "default_results": 5,
    "max_results": 10,
    "country": "tr",  # Türkiye
    "language": "tr"  # Türkçe
}

# Alternatif ücretsiz arama motorları
ALTERNATIVE_SEARCH_ENGINES = {
    "duckduckgo": {
        "enabled": True,
        "base_url": "https://api.duckduckgo.com/",
        "description": "Ücretsiz, gizlilik odaklı arama motoru"
    },
    "bing": {
        "enabled": False,
        "api_key": "YOUR_BING_API_KEY",
        "base_url": "https://api.bing.microsoft.com/v7.0/search",
        "description": "Microsoft Bing Search API"
    }
}

# Sistem ayarları
SYSTEM_CONFIG = {
    "auto_improve_interval": 3600,  # 1 saat (saniye)
    "max_knowledge_base_size": 10000,  # Maksimum öğrenilen bilgi sayısı
    "backup_interval": 86400,  # 24 saat (saniye)
    "log_level": "INFO"
}

# Öğrenme parametreleri
LEARNING_CONFIG = {
    "confidence_threshold": 0.7,  # Bilgiyi kabul etme eşiği
    "max_search_results": 5,
    "fact_check_enabled": True,
    "auto_learn_from_search": True
}

def get_api_key():
    """
    API anahtarını döndürür
    """
    return GOOGLE_API_CONFIG["api_key"]

def get_search_engine_id():
    """
    Search Engine ID'sini döndürür
    """
    return GOOGLE_API_CONFIG["search_engine_id"]

def is_api_configured():
    """
    API'nin yapılandırılıp yapılandırılmadığını kontrol eder
    """
    api_key = GOOGLE_API_CONFIG["api_key"]
    search_id = GOOGLE_API_CONFIG["search_engine_id"]
    
    return (api_key != "YOUR_GOOGLE_API_KEY_HERE" and 
            search_id != "YOUR_SEARCH_ENGINE_ID_HERE" and
            api_key and search_id)

# Test fonksiyonu
if __name__ == "__main__":
    print("=== API Konfigürasyon Kontrolü ===")
    
    if is_api_configured():
        print("✅ API yapılandırması tamamlanmış!")
        print(f"API Key: {get_api_key()[:10]}...")
        print(f"Search Engine ID: {get_search_engine_id()}")
    else:
        print("❌ API yapılandırması gerekli!")
        print("\nYapılması gerekenler:")
        print("1. Google Cloud Console'da proje oluşturun")
        print("2. Custom Search API'yi etkinleştirin")
        print("3. API key oluşturun")
        print("4. Custom Search Engine oluşturun")
        print("5. api_config.py dosyasındaki değerleri güncelleyin")
        
        print(f"\nMevcut API Key: {GOOGLE_API_CONFIG['api_key']}")
        print(f"Mevcut Search Engine ID: {GOOGLE_API_CONFIG['search_engine_id']}")