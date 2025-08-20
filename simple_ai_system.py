# Basit AI Sistemi - CPU Modunda Çalışır
import json
import os
from datetime import datetime
from typing import Dict, List
import requests

# Unsloth olmadan çalışacak basit sistem
class SimpleAISystem:
    def __init__(self):
        """
        Basit AI sistemini başlatır (CPU modunda)
        """
        print("🤖 Basit AI Sistemi başlatılıyor...")
        
        # Arama motorunu seç
        try:
            from api_config import is_api_configured
            if is_api_configured():
                print("🔍 Google Search API kullanılıyor")
                from search_engine import GoogleSearchEngine
                self.search_engine = GoogleSearchEngine()
                self.search_type = "google"
            else:
                print("🔍 Ücretsiz arama motoru kullanılıyor")
                from free_search_engine import FreeSearchEngine
                self.search_engine = FreeSearchEngine()
                self.search_type = "free"
        except Exception as e:
            print(f"⚠️ Arama motoru yüklenirken hata: {e}")
            from free_search_engine import FreeSearchEngine
            self.search_engine = FreeSearchEngine()
            self.search_type = "free"
        
        self.knowledge_base = self.load_knowledge_base()
        self.learning_history = []
        
        # Basit yanıt şablonları
        self.response_templates = self.load_response_templates()
    
    def load_knowledge_base(self) -> Dict:
        """
        Bilgi tabanını yükler
        """
        kb_file = "knowledge_base.json"
        if os.path.exists(kb_file):
            with open(kb_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {
            "learned_facts": {},
            "search_history": [],
            "improvement_log": [],
            "last_update": datetime.now().isoformat()
        }
    
    def save_knowledge_base(self):
        """
        Bilgi tabanını kaydeder
        """
        self.knowledge_base["last_update"] = datetime.now().isoformat()
        with open("knowledge_base.json", 'w', encoding='utf-8') as f:
            json.dump(self.knowledge_base, f, ensure_ascii=False, indent=2)
    
    def load_response_templates(self) -> Dict:
        """
        Yanıt şablonlarını yükler
        """
        return {
            "greeting": [
                "Merhaba! Size nasıl yardımcı olabilirim?",
                "Selam! Hangi konuda bilgi almak istiyorsunuz?",
                "İyi günler! Sorularınızı bekliyorum."
            ],
            "search_intro": [
                "Bu konu hakkında güncel bilgi arıyorum...",
                "Size en güncel bilgileri getiriyorum...",
                "Araştırma yapıyorum, lütfen bekleyin..."
            ],
            "no_info": [
                "Üzgünüm, bu konu hakkında yeterli bilgi bulamadım.",
                "Bu konuda şu anda bilgim yok, araştırma yapayım.",
                "Maalesef bu soruya kesin bir yanıt veremiyorum."
            ]
        }
    
    def generate_simple_response(self, question: str) -> str:
        """
        Basit kural tabanlı yanıt üretir
        """
        question_lower = question.lower()
        
        # Selamlama kontrolü
        greetings = ["merhaba", "selam", "iyi günler", "nasılsın", "hey"]
        if any(greeting in question_lower for greeting in greetings):
            return "Merhaba! Ben kendini geliştiren bir AI asistanıyım. Size nasıl yardımcı olabilirim?"
        
        # Bilgi tabanında ara
        cached_response = self.search_knowledge_base(question)
        if cached_response:
            return f"{cached_response}\n\n[Kaynak: Öğrenilmiş Bilgi Tabanı]"
        
        # Eğitim verisinden ara
        training_response = self.search_training_data(question)
        if training_response:
            return training_response
        
        # Varsayılan yanıt
        return "Bu konu hakkında daha fazla bilgi edinmek için güncel arama yapayım."
    
    def search_knowledge_base(self, query: str) -> str:
        """
        Bilgi tabanında arama yapar
        """
        query_lower = query.lower()
        for fact_key, fact_value in self.knowledge_base["learned_facts"].items():
            if any(keyword in query_lower for keyword in fact_key.lower().split()):
                return fact_value["content"]
        return None
    
    def search_training_data(self, question: str) -> str:
        """
        Eğitim verisinde arama yapar
        """
        try:
            with open("eğitim_verisi.json", 'r', encoding='utf-8') as f:
                training_data = json.load(f)
            
            question_lower = question.lower()
            
            # En iyi eşleşmeyi bul
            best_match = None
            best_score = 0
            
            for item in training_data:
                instruction = item.get("instruction", "").lower()
                input_text = item.get("input", "").lower()
                
                # Basit kelime eşleştirme
                question_words = set(question_lower.split())
                instruction_words = set(instruction.split())
                input_words = set(input_text.split())
                
                # Eşleşme skoru hesapla
                instruction_score = len(question_words.intersection(instruction_words))
                input_score = len(question_words.intersection(input_words))
                total_score = instruction_score + input_score
                
                if total_score > best_score:
                    best_score = total_score
                    best_match = item
            
            if best_match and best_score > 0:
                return best_match.get("output", "")
            
        except Exception as e:
            print(f"Eğitim verisi arama hatası: {e}")
        
        return None
    
    def enhance_with_search(self, question: str) -> str:
        """
        Arama ile yanıtı geliştirir
        """
        print(f"🔍 '{question}' için güncel bilgi aranıyor...")
        
        # Önce basit yanıt üret
        simple_response = self.generate_simple_response(question)
        
        try:
            # Arama yap
            if self.search_type == "google":
                search_results = self.search_engine.search(question, num_results=3)
            else:
                search_results = self.search_engine.comprehensive_search(question, num_results=3)
            
            if search_results:
                # Arama sonuçlarını ekle
                search_info = "\n\n📊 **Güncel Bilgiler:**\n"
                for i, result in enumerate(search_results, 1):
                    search_info += f"{i}. **{result.get('title', 'Başlık yok')}**\n"
                    search_info += f"   {result.get('snippet', 'Açıklama yok')}\n"
                    if result.get('link'):
                        search_info += f"   🔗 {result['link']}\n"
                    search_info += "\n"
                
                # Bilgi tabanını güncelle
                self.learn_new_information(question, search_info, "search_enhancement")
                
                enhanced_response = simple_response + search_info
                enhanced_response += f"\n🕒 **Son Güncelleme:** {datetime.now().strftime('%Y-%m-%d %H:%M')}"
                
                return enhanced_response
            
        except Exception as e:
            print(f"Arama hatası: {e}")
        
        return simple_response
    
    def learn_new_information(self, topic: str, information: str, source: str):
        """
        Yeni bilgiyi öğrenir
        """
        learning_entry = {
            "topic": topic,
            "information": information,
            "source": source,
            "learned_at": datetime.now().isoformat()
        }
        
        # Bilgi tabanına ekle
        topic_key = topic.lower().replace(" ", "_")
        self.knowledge_base["learned_facts"][topic_key] = {
            "content": information,
            "source": source,
            "learned_at": datetime.now().isoformat()
        }
        
        self.learning_history.append(learning_entry)
        self.save_knowledge_base()
        
        print(f"✅ Yeni bilgi öğrenildi: {topic}")
    
    def self_improve(self):
        """
        Kendini geliştirme süreci
        """
        print("🚀 Kendini geliştirme süreci başlatılıyor...")
        
        popular_topics = [
            "yapay zeka son gelişmeler",
            "teknoloji haberleri 2024",
            "Python programlama yenilikleri",
            "bilim son dakika"
        ]
        
        for topic in popular_topics:
            try:
                current_info = self.search_engine.get_current_info(topic)
                self.learn_new_information(topic, current_info, "self_improvement")
                print(f"📚 {topic} hakkında bilgi güncellendi")
            except Exception as e:
                print(f"❌ {topic} güncellenirken hata: {e}")
        
        print("✨ Kendini geliştirme süreci tamamlandı!")
    
    def get_stats(self) -> Dict:
        """
        Sistem istatistikleri
        """
        return {
            "total_learned_facts": len(self.knowledge_base["learned_facts"]),
            "learning_sessions": len(self.learning_history),
            "last_update": self.knowledge_base.get("last_update", "Hiç güncellenmedi"),
            "search_type": self.search_type,
            "system_mode": "CPU (Basit Mod)"
        }
    
    def interactive_chat(self):
        """
        Etkileşimli sohbet modu
        """
        print("🤖 Basit AI Sistemi Aktif!")
        print("Komutlar: 'çıkış' - çık, 'istatistik' - stats, 'geliştir' - self improve")
        print("-" * 50)
        
        while True:
            user_input = input("\n👤 Siz: ").strip()
            
            if user_input.lower() in ['çıkış', 'exit', 'quit']:
                print("👋 Görüşmek üzere!")
                break
            elif user_input.lower() in ['istatistik', 'stats']:
                stats = self.get_stats()
                print("\n📊 **Sistem İstatistikleri:**")
                for key, value in stats.items():
                    print(f"   {key}: {value}")
            elif user_input.lower() in ['geliştir', 'improve']:
                self.self_improve()
            elif user_input.lower().startswith('ara:'):
                search_query = user_input[4:].strip()
                response = self.enhance_with_search(search_query)
                print(f"\n🤖 AI: {response}")
            else:
                # Normal soru-cevap
                if "güncel" in user_input.lower() or "son" in user_input.lower():
                    response = self.enhance_with_search(user_input)
                else:
                    response = self.generate_simple_response(user_input)
                
                print(f"\n🤖 AI: {response}")

# Test fonksiyonu
def main():
    """
    Ana program
    """
    print("🚀 Basit AI Sistemi Başlatılıyor...")
    
    try:
        ai_system = SimpleAISystem()
        ai_system.interactive_chat()
    except Exception as e:
        print(f"❌ Sistem hatası: {e}")
        print("💡 Gerekli kütüphanelerin kurulu olduğundan emin olun")

if __name__ == "__main__":
    main()