# Google Search API entegrasyonu
import requests
import json
from typing import List, Dict
import time
from datetime import datetime

class GoogleSearchEngine:
    def __init__(self, api_key: str = None, search_engine_id: str = None):
        """
        Google Custom Search API için yapılandırma
        API key ve Search Engine ID gereklidir
        """
        # API config dosyasından anahtarları al
        try:
            from api_config import get_api_key, get_search_engine_id
            self.api_key = api_key or get_api_key()
            self.search_engine_id = search_engine_id or get_search_engine_id()
        except ImportError:
            self.api_key = api_key or "YOUR_GOOGLE_API_KEY"
            self.search_engine_id = search_engine_id or "YOUR_SEARCH_ENGINE_ID"
        
        self.base_url = "https://www.googleapis.com/customsearch/v1"
        
    def search(self, query: str, num_results: int = 5) -> List[Dict]:
        """
        Google'da arama yapar ve sonuçları döndürür
        """
        try:
            params = {
                'key': self.api_key,
                'cx': self.search_engine_id,
                'q': query,
                'num': min(num_results, 10),  # Google API maksimum 10 sonuç döndürür
                'gl': 'tr',  # Türkiye sonuçları
                'hl': 'tr'   # Türkçe dil
            }
            
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            
            data = response.json()
            results = []
            
            if 'items' in data:
                for item in data['items']:
                    result = {
                        'title': item.get('title', ''),
                        'link': item.get('link', ''),
                        'snippet': item.get('snippet', ''),
                        'displayLink': item.get('displayLink', ''),
                        'formattedUrl': item.get('formattedUrl', ''),
                        'searchTime': datetime.now().isoformat()
                    }
                    results.append(result)
            
            return results
            
        except requests.exceptions.RequestException as e:
            print(f"Arama hatası: {e}")
            return []
        except Exception as e:
            print(f"Beklenmeyen hata: {e}")
            return []
    
    def get_current_info(self, topic: str) -> str:
        """
        Belirli bir konu hakkında güncel bilgi alır
        """
        search_results = self.search(f"{topic} güncel bilgi 2024", num_results=3)
        
        if not search_results:
            return f"{topic} hakkında güncel bilgi bulunamadı."
        
        info_summary = f"{topic} hakkında güncel bilgiler:\n\n"
        
        for i, result in enumerate(search_results, 1):
            info_summary += f"{i}. {result['title']}\n"
            info_summary += f"   {result['snippet']}\n"
            info_summary += f"   Kaynak: {result['displayLink']}\n\n"
        
        return info_summary
    
    def fact_check(self, statement: str) -> Dict:
        """
        Bir ifadeyi doğruluk kontrolünden geçirir
        """
        search_query = f'"{statement}" doğru mu yanlış mı fact check'
        results = self.search(search_query, num_results=3)
        
        return {
            'statement': statement,
            'search_results': results,
            'check_time': datetime.now().isoformat(),
            'confidence': 'medium'  # Bu daha gelişmiş algoritma ile hesaplanabilir
        }

# Test fonksiyonu
def test_search_engine():
    """
    Search engine'i test eder
    """
    search_engine = GoogleSearchEngine()
    
    # Test araması
    print("=== Google Search Test ===")
    results = search_engine.search("yapay zeka son gelişmeler", num_results=3)
    
    for i, result in enumerate(results, 1):
        print(f"{i}. {result['title']}")
        print(f"   {result['snippet']}")
        print(f"   {result['link']}\n")
    
    # Güncel bilgi testi
    print("=== Güncel Bilgi Test ===")
    current_info = search_engine.get_current_info("blockchain teknolojisi")
    print(current_info)

if __name__ == "__main__":
    test_search_engine()