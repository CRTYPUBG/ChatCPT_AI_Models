# Ücretsiz Arama Motoru Entegrasyonu
import requests
import json
from typing import List, Dict
from datetime import datetime
import time
from bs4 import BeautifulSoup
import urllib.parse

class FreeSearchEngine:
    """
    Ücretsiz arama motorları için entegrasyon
    Google API gerektirmez
    """
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
    
    def duckduckgo_search(self, query: str, num_results: int = 5) -> List[Dict]:
        """
        DuckDuckGo ile arama yapar (ücretsiz)
        """
        try:
            # DuckDuckGo Instant Answer API
            url = "https://api.duckduckgo.com/"
            params = {
                'q': query,
                'format': 'json',
                'no_html': '1',
                'skip_disambig': '1'
            }
            
            response = self.session.get(url, params=params)
            response.raise_for_status()
            
            data = response.json()
            results = []
            
            # Abstract (özet) bilgisi varsa ekle
            if data.get('Abstract'):
                results.append({
                    'title': data.get('Heading', query),
                    'snippet': data.get('Abstract', ''),
                    'link': data.get('AbstractURL', ''),
                    'source': 'DuckDuckGo Abstract',
                    'searchTime': datetime.now().isoformat()
                })
            
            # Related topics ekle
            if data.get('RelatedTopics'):
                for topic in data.get('RelatedTopics', [])[:num_results-1]:
                    if isinstance(topic, dict) and topic.get('Text'):
                        results.append({
                            'title': topic.get('Text', '')[:100] + '...',
                            'snippet': topic.get('Text', ''),
                            'link': topic.get('FirstURL', ''),
                            'source': 'DuckDuckGo Related',
                            'searchTime': datetime.now().isoformat()
                        })
            
            return results[:num_results]
            
        except Exception as e:
            print(f"DuckDuckGo arama hatası: {e}")
            return []
    
    def wikipedia_search(self, query: str, lang: str = 'tr') -> Dict:
        """
        Wikipedia'dan bilgi alır
        """
        try:
            # Wikipedia API
            url = f"https://{lang}.wikipedia.org/api/rest_v1/page/summary/{urllib.parse.quote(query)}"
            
            response = self.session.get(url)
            
            if response.status_code == 200:
                data = response.json()
                return {
                    'title': data.get('title', ''),
                    'snippet': data.get('extract', ''),
                    'link': data.get('content_urls', {}).get('desktop', {}).get('page', ''),
                    'source': 'Wikipedia',
                    'searchTime': datetime.now().isoformat(),
                    'thumbnail': data.get('thumbnail', {}).get('source', '') if data.get('thumbnail') else ''
                }
            
            return {}
            
        except Exception as e:
            print(f"Wikipedia arama hatası: {e}")
            return {}
    
    def news_search(self, query: str) -> List[Dict]:
        """
        Haber sitelerinden güncel bilgi alır
        """
        try:
            # Basit haber arama (RSS feed'ler kullanılabilir)
            news_sources = [
                "https://www.aa.com.tr/tr/rss/default?cat=guncel",
                "https://www.hurriyet.com.tr/rss/anasayfa",
                "https://www.milliyet.com.tr/rss/rssNew/SonDakikaRSS.xml"
            ]
            
            results = []
            
            # Bu basit bir örnek - gerçek uygulamada RSS parser kullanılmalı
            for source in news_sources[:1]:  # Sadece bir kaynak test için
                try:
                    response = self.session.get(source, timeout=5)
                    if response.status_code == 200:
                        # RSS parsing burada yapılabilir
                        results.append({
                            'title': f"Güncel haberler - {query}",
                            'snippet': f"{query} ile ilgili güncel haberler bulundu",
                            'link': source,
                            'source': 'Haber Kaynağı',
                            'searchTime': datetime.now().isoformat()
                        })
                except:
                    continue
            
            return results
            
        except Exception as e:
            print(f"Haber arama hatası: {e}")
            return []
    
    def comprehensive_search(self, query: str, num_results: int = 5) -> List[Dict]:
        """
        Tüm kaynaklardan kapsamlı arama yapar
        """
        all_results = []
        
        print(f"🔍 '{query}' için kapsamlı arama yapılıyor...")
        
        # DuckDuckGo arama
        ddg_results = self.duckduckgo_search(query, num_results=3)
        all_results.extend(ddg_results)
        
        # Wikipedia arama
        wiki_result = self.wikipedia_search(query)
        if wiki_result:
            all_results.append(wiki_result)
        
        # Haber arama
        news_results = self.news_search(query)
        all_results.extend(news_results)
        
        # Sonuçları sınırla
        return all_results[:num_results]
    
    def get_current_info(self, topic: str) -> str:
        """
        Belirli bir konu hakkında güncel bilgi toplar
        """
        search_results = self.comprehensive_search(f"{topic} güncel bilgi", num_results=5)
        
        if not search_results:
            return f"{topic} hakkında bilgi bulunamadı."
        
        info_summary = f"📚 **{topic}** hakkında toplanan bilgiler:\n\n"
        
        for i, result in enumerate(search_results, 1):
            if result.get('snippet'):
                info_summary += f"**{i}. {result.get('source', 'Bilinmeyen Kaynak')}**\n"
                info_summary += f"   📝 {result['snippet'][:200]}...\n"
                if result.get('link'):
                    info_summary += f"   🔗 {result['link']}\n"
                info_summary += "\n"
        
        info_summary += f"🕒 **Arama Zamanı:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        
        return info_summary

# Test fonksiyonu
def test_free_search():
    """
    Ücretsiz arama motorunu test eder
    """
    search_engine = FreeSearchEngine()
    
    print("=== Ücretsiz Arama Motoru Test ===")
    
    # DuckDuckGo test
    print("\n1. DuckDuckGo Testi:")
    ddg_results = search_engine.duckduckgo_search("yapay zeka", num_results=3)
    for result in ddg_results:
        print(f"   • {result.get('title', 'Başlık yok')}")
        print(f"     {result.get('snippet', 'Açıklama yok')[:100]}...")
    
    # Wikipedia test
    print("\n2. Wikipedia Testi:")
    wiki_result = search_engine.wikipedia_search("yapay zeka")
    if wiki_result:
        print(f"   • {wiki_result.get('title', 'Başlık yok')}")
        print(f"     {wiki_result.get('snippet', 'Açıklama yok')[:100]}...")
    
    # Kapsamlı arama test
    print("\n3. Kapsamlı Arama Testi:")
    comprehensive_results = search_engine.comprehensive_search("blockchain teknolojisi", num_results=3)
    for result in comprehensive_results:
        print(f"   • [{result.get('source', 'Kaynak')}] {result.get('title', 'Başlık yok')}")
    
    # Güncel bilgi test
    print("\n4. Güncel Bilgi Testi:")
    current_info = search_engine.get_current_info("Python programlama")
    print(current_info[:300] + "...")

if __name__ == "__main__":
    test_free_search()