# Çalışan AI Sistemi - Kütüphane Bağımlılığı Olmadan
import json
import os
import re
import random
from datetime import datetime
from typing import Dict, List

class WorkingAISystem:
    """
    Tam çalışan AI sistemi - transformers gerektirmez
    """
    
    def __init__(self):
        print("🤖 Çalışan AI Sistemi başlatılıyor...")
        
        # Arama motorunu ayarla
        self.setup_search_engine()
        
        # Sistem bileşenleri
        self.knowledge_base = self.load_knowledge_base()
        self.learning_history = []
        self.training_data = self.load_training_data()
        
        # Yanıt şablonları
        self.response_templates = self.load_response_templates()
        
        print("✅ AI Sistemi hazır!")
    
    def setup_search_engine(self):
        """
        Arama motorunu ayarlar
        """
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
            print(f"⚠️ Arama motoru ayarlanırken hata: {e}")
            # Basit arama motoru oluştur
            self.search_engine = None
            self.search_type = "none"
    
    def load_knowledge_base(self) -> Dict:
        """
        Bilgi tabanını yükler
        """
        kb_file = "knowledge_base.json"
        if os.path.exists(kb_file):
            try:
                with open(kb_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                pass
        
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
        try:
            self.knowledge_base["last_update"] = datetime.now().isoformat()
            with open("knowledge_base.json", 'w', encoding='utf-8') as f:
                json.dump(self.knowledge_base, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"⚠️ Bilgi tabanı kaydetme hatası: {e}")
    
    def load_training_data(self) -> List[Dict]:
        """
        Eğitim verisini yükler
        """
        try:
            with open("eğitim_verisi.json", 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠️ Eğitim verisi yükleme hatası: {e}")
            return []
    
    def load_response_templates(self) -> Dict:
        """
        Yanıt şablonlarını yükler
        """
        return {
            "greeting": [
                "Merhaba! Size nasıl yardımcı olabilirim?",
                "Selam! Hangi konuda bilgi almak istiyorsunuz?",
                "İyi günler! Sorularınızı bekliyorum.",
                "Hoş geldiniz! Ben AI asistanınızım."
            ],
            "thanks": [
                "Rica ederim! Başka sorunuz var mı?",
                "Memnun oldum yardımcı olabildiğim için!",
                "Her zaman! Başka bir konuda yardım edebilir miyim?"
            ],
            "unknown": [
                "Bu konu hakkında daha fazla bilgi edinmek için araştırma yapayım.",
                "İlginç bir soru! Size daha detaylı bilgi verebilmek için araştırayım.",
                "Bu konuda güncel bilgi almak için arama yapacağım."
            ],
            "search_intro": [
                "Bu konu hakkında güncel bilgi arıyorum...",
                "Size en güncel bilgileri getiriyorum...",
                "Araştırma yapıyorum, lütfen bekleyin..."
            ]
        }
    
    def calculate_similarity(self, text1: str, text2: str) -> float:
        """
        İki metin arasındaki benzerliği hesaplar
        """
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())
        
        if not words1 or not words2:
            return 0.0
        
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        return len(intersection) / len(union) if union else 0.0
    
    def find_best_training_match(self, question: str) -> Dict:
        """
        Eğitim verisinde en iyi eşleşmeyi bulur
        """
        best_match = None
        best_score = 0.0
        
        question_clean = re.sub(r'[^\w\s]', '', question.lower())
        
        for item in self.training_data:
            instruction = item.get("instruction", "")
            input_text = item.get("input", "")
            
            # Instruction ile karşılaştır
            instruction_score = self.calculate_similarity(question_clean, instruction)
            
            # Input ile karşılaştır
            input_score = self.calculate_similarity(question_clean, input_text) if input_text else 0
            
            # Toplam skor
            total_score = max(instruction_score, input_score)
            
            if total_score > best_score and total_score > 0.2:  # Minimum eşik
                best_score = total_score
                best_match = item
        
        return best_match if best_match else None
    
    def search_knowledge_base(self, query: str) -> str:
        """
        Bilgi tabanında arama yapar
        """
        query_lower = query.lower()
        query_words = set(query_lower.split())
        
        best_match = None
        best_score = 0.0
        
        for fact_key, fact_value in self.knowledge_base["learned_facts"].items():
            fact_words = set(fact_key.lower().replace('_', ' ').split())
            score = len(query_words.intersection(fact_words)) / len(query_words.union(fact_words))
            
            if score > best_score and score > 0.3:
                best_score = score
                best_match = fact_value["content"]
        
        return best_match
    
    def generate_response(self, question: str) -> str:
        """
        Soruya yanıt üretir
        """
        question_lower = question.lower()
        
        # Selamlama kontrolü
        greetings = ["merhaba", "selam", "iyi günler", "nasılsın", "hey", "hoş geldin"]
        if any(greeting in question_lower for greeting in greetings):
            return random.choice(self.response_templates["greeting"])
        
        # Teşekkür kontrolü
        thanks = ["teşekkür", "sağol", "eyvallah", "mersi"]
        if any(thank in question_lower for thank in thanks):
            return random.choice(self.response_templates["thanks"])
        
        # Bilgi tabanında ara
        kb_response = self.search_knowledge_base(question)
        if kb_response:
            return f"{kb_response}\n\n💡 [Kaynak: Öğrenilmiş Bilgi Tabanı]"
        
        # Eğitim verisinde ara
        training_match = self.find_best_training_match(question)
        if training_match:
            response = training_match.get("output", "")
            if response:
                return f"{response}\n\n📚 [Kaynak: Eğitim Verisi]"
        
        # Varsayılan yanıt
        return random.choice(self.response_templates["unknown"])
    
    def enhance_with_search(self, question: str) -> str:
        """
        Arama ile yanıtı geliştirir
        """
        print(f"🔍 '{question}' için güncel bilgi aranıyor...")
        
        # Temel yanıtı al
        base_response = self.generate_response(question)
        
        if not self.search_engine:
            return base_response + "\n\n⚠️ Arama motoru mevcut değil."
        
        try:
            # Arama yap
            if self.search_type == "google":
                search_results = self.search_engine.search(question, num_results=3)
            else:
                search_results = self.search_engine.comprehensive_search(question, num_results=3)
            
            if search_results:
                search_info = "\n\n📊 **Güncel Bilgiler:**\n"
                for i, result in enumerate(search_results, 1):
                    title = result.get('title', 'Başlık yok')[:80]
                    snippet = result.get('snippet', 'Açıklama yok')[:150]
                    link = result.get('link', '')
                    
                    search_info += f"\n**{i}. {title}**\n"
                    search_info += f"   {snippet}...\n"
                    if link:
                        search_info += f"   🔗 {link}\n"
                
                # Bilgi tabanını güncelle
                self.learn_new_information(question, search_info, "search_enhancement")
                
                enhanced_response = base_response + search_info
                enhanced_response += f"\n\n🕒 **Arama Zamanı:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                
                return enhanced_response
            else:
                return base_response + "\n\n⚠️ Güncel bilgi bulunamadı."
            
        except Exception as e:
            print(f"⚠️ Arama hatası: {e}")
            return base_response + f"\n\n⚠️ Arama hatası: {str(e)[:100]}"
    
    def learn_new_information(self, topic: str, information: str, source: str):
        """
        Yeni bilgiyi öğrenir
        """
        try:
            learning_entry = {
                "topic": topic,
                "information": information,
                "source": source,
                "learned_at": datetime.now().isoformat()
            }
            
            topic_key = re.sub(r'[^\w\s]', '', topic.lower()).replace(' ', '_')[:50]
            self.knowledge_base["learned_facts"][topic_key] = {
                "content": information,
                "source": source,
                "learned_at": datetime.now().isoformat()
            }
            
            self.learning_history.append(learning_entry)
            self.save_knowledge_base()
            
            print(f"✅ Yeni bilgi öğrenildi: {topic[:50]}...")
            
        except Exception as e:
            print(f"⚠️ Öğrenme hatası: {e}")
    
    def self_improve(self):
        """
        Kendini geliştirme süreci
        """
        print("🚀 Kendini geliştirme süreci başlatılıyor...")
        
        if not self.search_engine:
            print("❌ Arama motoru mevcut değil, kendini geliştirme yapılamıyor.")
            return
        
        popular_topics = [
            "yapay zeka son gelişmeler 2024",
            "teknoloji haberleri güncel",
            "Python programlama yenilikleri",
            "bilim son dakika haberleri",
            "blockchain teknolojisi güncel"
        ]
        
        improved_count = 0
        for topic in popular_topics:
            try:
                print(f"📚 {topic} araştırılıyor...")
                current_info = self.search_engine.get_current_info(topic)
                
                if current_info and len(current_info) > 100:
                    self.learn_new_information(topic, current_info, "self_improvement")
                    improved_count += 1
                    print(f"✅ {topic} güncellendi")
                else:
                    print(f"⚠️ {topic} için yeterli bilgi bulunamadı")
                    
            except Exception as e:
                print(f"❌ {topic} güncellenirken hata: {e}")
        
        # İyileştirme logunu güncelle
        improvement_log = {
            "timestamp": datetime.now().isoformat(),
            "topics_updated": improved_count,
            "total_learned_facts": len(self.knowledge_base["learned_facts"])
        }
        
        self.knowledge_base["improvement_log"].append(improvement_log)
        self.save_knowledge_base()
        
        print(f"✨ Kendini geliştirme tamamlandı! {improved_count} konu güncellendi.")
    
    def get_stats(self) -> Dict:
        """
        Sistem istatistikleri
        """
        return {
            "total_learned_facts": len(self.knowledge_base["learned_facts"]),
            "learning_sessions": len(self.learning_history),
            "last_update": self.knowledge_base.get("last_update", "Hiç güncellenmedi"),
            "search_type": self.search_type,
            "training_data_size": len(self.training_data),
            "system_mode": "Çalışan AI Sistemi",
            "improvement_sessions": len(self.knowledge_base.get("improvement_log", []))
        }
    
    def interactive_chat(self):
        """
        Etkileşimli sohbet modu
        """
        print("\n🤖 Çalışan AI Sistemi Aktif!")
        print("Komutlar:")
        print("  • 'çıkış' - Programdan çık")
        print("  • 'istatistik' - Sistem istatistikleri")
        print("  • 'geliştir' - Kendini geliştirme başlat")
        print("  • 'ara: [konu]' - Güncel bilgi ara")
        print("  • 'temizle' - Bilgi tabanını temizle")
        print("-" * 60)
        
        while True:
            try:
                user_input = input("\n👤 Siz: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['çıkış', 'exit', 'quit', 'bye']:
                    print("👋 Görüşmek üzere! Tekrar bekleriz.")
                    break
                
                elif user_input.lower() in ['istatistik', 'stats', 'stat']:
                    stats = self.get_stats()
                    print("\n📊 **Sistem İstatistikleri:**")
                    print("-" * 40)
                    for key, value in stats.items():
                        print(f"   📈 {key}: {value}")
                
                elif user_input.lower() in ['geliştir', 'improve', 'öğren']:
                    self.self_improve()
                
                elif user_input.lower().startswith('ara:'):
                    search_query = user_input[4:].strip()
                    if search_query:
                        response = self.enhance_with_search(search_query)
                        print(f"\n🤖 AI: {response}")
                    else:
                        print("❌ Arama sorgusu boş!")
                
                elif user_input.lower() in ['temizle', 'clear', 'reset']:
                    confirm = input("Bilgi tabanını temizlemek istediğinizden emin misiniz? (e/h): ")
                    if confirm.lower() == 'e':
                        self.knowledge_base = {
                            "learned_facts": {},
                            "search_history": [],
                            "improvement_log": [],
                            "last_update": datetime.now().isoformat()
                        }
                        self.save_knowledge_base()
                        print("✅ Bilgi tabanı temizlendi!")
                    else:
                        print("❌ İşlem iptal edildi.")
                
                else:
                    # Normal soru-cevap
                    if any(keyword in user_input.lower() for keyword in ["güncel", "son", "yeni", "2024", "şimdi"]):
                        response = self.enhance_with_search(user_input)
                    else:
                        response = self.generate_response(user_input)
                    
                    print(f"\n🤖 AI: {response}")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Program kullanıcı tarafından sonlandırıldı.")
                break
            except Exception as e:
                print(f"\n❌ Hata oluştu: {e}")
                print("💡 Lütfen tekrar deneyin.")

def main():
    """
    Ana program
    """
    print("🚀 Çalışan AI Sistemi Başlatılıyor...")
    print("=" * 60)
    
    try:
        ai_system = WorkingAISystem()
        ai_system.interactive_chat()
    except Exception as e:
        print(f"❌ Sistem başlatma hatası: {e}")
        print("💡 Lütfen gerekli dosyaların mevcut olduğundan emin olun.")

if __name__ == "__main__":
    main()