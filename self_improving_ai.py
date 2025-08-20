# Kendini Geliştiren AI Sistemi
import json
import torch
from datetime import datetime
from typing import Dict, List, Any
from unsloth import FastLanguageModel
from search_engine import GoogleSearchEngine
from free_search_engine import FreeSearchEngine
from api_config import is_api_configured
import os
import pickle

class SelfImprovingAI:
    def __init__(self, model_path: str = "turkish-mistral-7b-final"):
        """
        Kendini geliştiren AI sistemini başlatır
        """
        self.model_path = model_path
        
        # Arama motorunu seç (Google API varsa Google, yoksa ücretsiz)
        if is_api_configured():
            print("🔍 Google Search API kullanılıyor")
            self.search_engine = GoogleSearchEngine()
            self.search_type = "google"
        else:
            print("🔍 Ücretsiz arama motoru kullanılıyor")
            self.search_engine = FreeSearchEngine()
            self.search_type = "free"
        
        self.knowledge_base = self.load_knowledge_base()
        self.learning_history = []
        self.model = None
        self.tokenizer = None
        
        # Modeli yükle
        self.load_model()
        
    def load_model(self):
        """
        Eğitilmiş modeli yükler
        """
        try:
            print("Model yükleniyor...")
            self.model, self.tokenizer = FastLanguageModel.from_pretrained(
                model_name=self.model_path,
                max_seq_length=2048,
                dtype=None,
                load_in_4bit=True,
            )
            FastLanguageModel.for_inference(self.model)
            print("Model başarıyla yüklendi!")
        except Exception as e:
            print(f"Model yükleme hatası: {e}")
            print("Varsayılan model yükleniyor...")
            self.model, self.tokenizer = FastLanguageModel.from_pretrained(
                model_name="unsloth/mistral-7b-instruct-v0.2-bnb-4bit",
                max_seq_length=2048,
                dtype=None,
                load_in_4bit=True,
            )
            FastLanguageModel.for_inference(self.model)
    
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
    
    def generate_response(self, instruction: str, input_text: str = "") -> str:
        """
        Kullanıcı sorusuna yanıt üretir
        """
        # Önce bilgi tabanında ara
        cached_response = self.search_knowledge_base(instruction)
        if cached_response:
            return f"{cached_response}\n\n[Bilgi Kaynağı: Öğrenilmiş Bilgi Tabanı]"
        
        # Model ile yanıt üret
        prompt = f"""### Talimat:
{instruction}

### Girdi:
{input_text}

### Yanıt:
"""
        
        inputs = self.tokenizer([prompt], return_tensors="pt").to("cuda")
        
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=256,
                temperature=0.7,
                do_sample=True,
                pad_token_id=self.tokenizer.eos_token_id
            )
        
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Sadece yanıt kısmını al
        if "### Yanıt:" in response:
            response = response.split("### Yanıt:")[-1].strip()
        
        return response
    
    def search_knowledge_base(self, query: str) -> str:
        """
        Bilgi tabanında arama yapar
        """
        query_lower = query.lower()
        for fact_key, fact_value in self.knowledge_base["learned_facts"].items():
            if any(keyword in query_lower for keyword in fact_key.lower().split()):
                return fact_value["content"]
        return None
    
    def enhance_with_search(self, question: str) -> str:
        """
        Google arama ile yanıtı geliştirir
        """
        print(f"🔍 '{question}' için güncel bilgi aranıyor...")
        
        # Arama motorunda ara
        if self.search_type == "google":
            search_results = self.search_engine.search(question, num_results=3)
        else:
            search_results = self.search_engine.comprehensive_search(question, num_results=3)
        
        if not search_results:
            return self.generate_response(question)
        
        # Arama sonuçlarını bilgi tabanına ekle
        search_info = ""
        for result in search_results:
            search_info += f"• {result['title']}: {result['snippet']}\n"
        
        # Bilgi tabanını güncelle
        self.learn_new_information(question, search_info, "google_search")
        
        # Model yanıtı ile arama sonuçlarını birleştir
        model_response = self.generate_response(question)
        
        enhanced_response = f"""
{model_response}

📊 **Güncel Bilgiler:**
{search_info}

🕒 **Son Güncelleme:** {datetime.now().strftime('%Y-%m-%d %H:%M')}
"""
        
        return enhanced_response
    
    def learn_new_information(self, topic: str, information: str, source: str):
        """
        Yeni bilgiyi öğrenir ve bilgi tabanına ekler
        """
        learning_entry = {
            "topic": topic,
            "information": information,
            "source": source,
            "learned_at": datetime.now().isoformat(),
            "confidence": 0.8
        }
        
        # Bilgi tabanına ekle
        topic_key = topic.lower().replace(" ", "_")
        self.knowledge_base["learned_facts"][topic_key] = {
            "content": information,
            "source": source,
            "learned_at": datetime.now().isoformat()
        }
        
        # Öğrenme geçmişine ekle
        self.learning_history.append(learning_entry)
        
        # Bilgi tabanını kaydet
        self.save_knowledge_base()
        
        print(f"✅ Yeni bilgi öğrenildi: {topic}")
    
    def self_improve(self):
        """
        Kendini geliştirme sürecini başlatır
        """
        print("🚀 Kendini geliştirme süreci başlatılıyor...")
        
        # Son öğrenilen bilgileri analiz et
        recent_topics = []
        for entry in self.learning_history[-10:]:  # Son 10 öğrenme
            recent_topics.append(entry["topic"])
        
        # Popüler konular hakkında güncel bilgi al
        popular_topics = [
            "yapay zeka son gelişmeler",
            "teknoloji haberleri 2024",
            "bilim son dakika",
            "programlama yenilikleri"
        ]
        
        for topic in popular_topics:
            try:
                current_info = self.search_engine.get_current_info(topic)
                self.learn_new_information(topic, current_info, "self_improvement")
                print(f"📚 {topic} hakkında bilgi güncellendi")
            except Exception as e:
                print(f"❌ {topic} güncellenirken hata: {e}")
        
        # İyileştirme logunu güncelle
        improvement_log = {
            "timestamp": datetime.now().isoformat(),
            "topics_updated": len(popular_topics),
            "total_learned_facts": len(self.knowledge_base["learned_facts"])
        }
        
        self.knowledge_base["improvement_log"].append(improvement_log)
        self.save_knowledge_base()
        
        print("✨ Kendini geliştirme süreci tamamlandı!")
    
    def get_stats(self) -> Dict:
        """
        AI sisteminin istatistiklerini döndürür
        """
        return {
            "total_learned_facts": len(self.knowledge_base["learned_facts"]),
            "learning_sessions": len(self.learning_history),
            "last_update": self.knowledge_base.get("last_update", "Hiç güncellenmedi"),
            "improvement_sessions": len(self.knowledge_base.get("improvement_log", [])),
            "knowledge_base_size": len(str(self.knowledge_base))
        }
    
    def interactive_chat(self):
        """
        Etkileşimli sohbet modu
        """
        print("🤖 Kendini Geliştiren AI Sistemi Aktif!")
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
                # Özel arama komutu
                search_query = user_input[4:].strip()
                response = self.enhance_with_search(search_query)
                print(f"\n🤖 AI: {response}")
            else:
                # Normal soru-cevap
                if "güncel" in user_input.lower() or "son" in user_input.lower():
                    response = self.enhance_with_search(user_input)
                else:
                    response = self.generate_response(user_input)
                
                print(f"\n🤖 AI: {response}")

# Ana çalıştırma fonksiyonu
def main():
    """
    Ana program
    """
    print("🚀 Kendini Geliştiren AI Sistemi Başlatılıyor...")
    
    # AI sistemini başlat
    ai_system = SelfImprovingAI()
    
    # İlk kendini geliştirme
    ai_system.self_improve()
    
    # Etkileşimli mod
    ai_system.interactive_chat()

if __name__ == "__main__":
    main()