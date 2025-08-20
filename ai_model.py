#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI Model Sistemi - Eğitilebilir ve Kullanılabilir
Gerçek bir AI modeli gibi çalışır
"""

import json
import os
import pickle
import random
import re
import math
from datetime import datetime
from collections import defaultdict, Counter

class AIModel:
    def __init__(self, model_name="ChatCPT-3.0"):
        self.model_name = model_name
        self.model_version = "3.0"
        self.model_path = f"./models/{model_name}"
        
        # Model parametreleri
        self.vocabulary = {}  # Kelime sözlüğü
        self.word_embeddings = {}  # Kelime vektörleri
        self.response_patterns = {}  # Yanıt kalıpları
        self.context_memory = []  # Bağlam hafızası
        self.learning_rate = 0.01
        self.confidence_threshold = 0.3
        
        # Eğitim verileri
        self.training_data = []
        self.knowledge_base = {}
        
        print(f"🤖 ChatCPT 3.0 Model '{model_name}' başlatılıyor...")
        print("🚀 ChatCPT 3.0 - Türkçe Yapay Zeka Modeli")
        self.load_or_create_model()
    
    def load_or_create_model(self):
        """Model yükler veya yeni oluşturur"""
        if os.path.exists(f"{self.model_path}/model.pkl"):
            self.load_model()
        else:
            print("📚 ChatCPT 3.0 modeli oluşturuluyor...")
        print("🧠 Türkçe dil modeli eğitiliyor...")
            self.create_new_model()
            self.train_initial_model()
    
    def create_new_model(self):
        """Yeni model oluşturur"""
        os.makedirs(self.model_path, exist_ok=True)
        
        # Eğitim verisini yükle
        self.load_training_data()
        
        # Kelime sözlüğü oluştur
        self.build_vocabulary()
        
        # Kelime vektörleri oluştur
        self.create_word_embeddings()
        
        print("✅ ChatCPT 3.0 modeli başarıyla oluşturuldu!")
        print("🎯 Türkçe konuşma AI'ı hazır!")
    
    def load_training_data(self):
        """Eğitim verisini yükler"""
        try:
            with open("eğitim_verisi.json", 'r', encoding='utf-8') as f:
                self.training_data = json.load(f)
            print(f"📖 {len(self.training_data)} eğitim verisi yüklendi")
        except Exception as e:
            print(f"⚠️ Eğitim verisi yüklenemedi: {e}")
            self.training_data = []
    
    def build_vocabulary(self):
        """Kelime sözlüğü oluşturur"""
        word_freq = Counter()
        
        for item in self.training_data:
            # Tüm metinleri birleştir
            text = f"{item.get('instruction', '')} {item.get('input', '')} {item.get('output', '')}"
            words = self.tokenize(text)
            word_freq.update(words)
        
        # Sık kullanılan kelimeleri sözlüğe ekle
        for word, freq in word_freq.most_common(5000):  # En sık 5000 kelime
            if freq > 1:  # En az 2 kez geçen kelimeler
                self.vocabulary[word] = len(self.vocabulary)
        
        print(f"📝 {len(self.vocabulary)} kelimelik sözlük oluşturuldu")
    
    def tokenize(self, text):
        """Metni kelimelere ayırır"""
        # Türkçe karakterleri koruyarak tokenize et
        text = text.lower()
        words = re.findall(r'\b\w+\b', text)
        return words
    
    def create_word_embeddings(self):
        """Kelime vektörleri oluşturur"""
        embedding_dim = 100  # Vektör boyutu
        
        for word in self.vocabulary:
            # Rastgele vektör oluştur (gerçek uygulamada Word2Vec/GloVe kullanılır)
            vector = [random.uniform(-0.1, 0.1) for _ in range(embedding_dim)]
            self.word_embeddings[word] = vector
        
        print(f"🔢 {len(self.word_embeddings)} kelime vektörü oluşturuldu")
    
    def train_initial_model(self):
        """İlk model eğitimini yapar"""
        print("🏋️ ChatCPT 3.0 eğitimi başlıyor...")
        print("📖 Türkçe dil kalıpları öğreniliyor...")
        
        # Yanıt kalıplarını öğren
        for item in self.training_data:
            instruction = item.get('instruction', '')
            input_text = item.get('input', '')
            output = item.get('output', '')
            
            # Giriş ve çıkış arasındaki ilişkiyi öğren
            input_pattern = self.extract_pattern(f"{instruction} {input_text}")
            
            if input_pattern not in self.response_patterns:
                self.response_patterns[input_pattern] = []
            
            self.response_patterns[input_pattern].append({
                'response': output,
                'confidence': 1.0,
                'usage_count': 0
            })
        
        print(f"🧠 ChatCPT 3.0: {len(self.response_patterns)} Türkçe yanıt kalıbı öğrenildi")
        print("✨ ChatCPT 3.0 eğitimi tamamlandı!")
        self.save_model()
    
    def extract_pattern(self, text):
        """Metinden kalıp çıkarır"""
        words = self.tokenize(text)
        # Önemli kelimeleri al (stop words'leri filtrele)
        stop_words = {'bir', 'bu', 'şu', 've', 'ile', 'için', 'olan', 'olarak', 'ne', 'nedir', 'nasıl'}
        important_words = [w for w in words if w not in stop_words and len(w) > 2]
        
        # En önemli 3-5 kelimeyi al
        return ' '.join(important_words[:5])
    
    def calculate_similarity(self, text1, text2):
        """İki metin arasındaki benzerliği hesaplar"""
        words1 = set(self.tokenize(text1))
        words2 = set(self.tokenize(text2))
        
        if not words1 or not words2:
            return 0.0
        
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        return len(intersection) / len(union)
    
    def predict(self, input_text, context=None):
        """Girişe göre yanıt tahmin eder"""
        input_pattern = self.extract_pattern(input_text)
        
        best_response = None
        best_confidence = 0.0
        
        # Kalıp eşleştirme
        for pattern, responses in self.response_patterns.items():
            similarity = self.calculate_similarity(input_pattern, pattern)
            
            if similarity > best_confidence and similarity > self.confidence_threshold:
                best_confidence = similarity
                # En çok kullanılan yanıtı seç
                best_response = max(responses, key=lambda x: x['usage_count'])['response']
        
        # Eğer kalıp bulunamazsa, eğitim verisinde direkt ara
        if not best_response:
            best_response, best_confidence = self.search_training_data(input_text)
        
        # Bağlam hafızasına ekle
        self.context_memory.append({
            'input': input_text,
            'output': best_response,
            'confidence': best_confidence,
            'timestamp': datetime.now().isoformat()
        })
        
        # Hafızayı sınırla (son 10 etkileşim)
        if len(self.context_memory) > 10:
            self.context_memory = self.context_memory[-10:]
        
        return best_response, best_confidence
    
    def search_training_data(self, query):
        """Eğitim verisinde arama yapar"""
        best_match = None
        best_score = 0.0
        
        for item in self.training_data:
            instruction = item.get('instruction', '')
            input_text = item.get('input', '')
            output = item.get('output', '')
            
            # Instruction ile karşılaştır
            score1 = self.calculate_similarity(query, instruction)
            score2 = self.calculate_similarity(query, input_text) if input_text else 0
            
            score = max(score1, score2)
            
            if score > best_score:
                best_score = score
                best_match = output
        
        return best_match, best_score
    
    def fine_tune(self, new_data):
        """Modeli yeni verilerle ince ayar yapar"""
        print("🔧 Model ince ayar yapılıyor...")
        
        for item in new_data:
            instruction = item.get('instruction', '')
            input_text = item.get('input', '')
            output = item.get('output', '')
            
            # Yeni kalıp öğren
            input_pattern = self.extract_pattern(f"{instruction} {input_text}")
            
            if input_pattern not in self.response_patterns:
                self.response_patterns[input_pattern] = []
            
            self.response_patterns[input_pattern].append({
                'response': output,
                'confidence': 1.0,
                'usage_count': 0
            })
        
        # Eğitim verisine ekle
        self.training_data.extend(new_data)
        
        print(f"✅ {len(new_data)} yeni veri ile model güncellendi")
        self.save_model()
    
    def learn_from_interaction(self, user_input, expected_output):
        """Kullanıcı etkileşiminden öğrenir"""
        new_data = [{
            'instruction': user_input,
            'input': '',
            'output': expected_output
        }]
        
        self.fine_tune(new_data)
        print(f"🧠 Yeni etkileşim öğrenildi: '{user_input[:30]}...'")
    
    def save_model(self):
        """Modeli kaydeder"""
        try:
            model_data = {
                'model_name': self.model_name,
                'vocabulary': self.vocabulary,
                'word_embeddings': self.word_embeddings,
                'response_patterns': self.response_patterns,
                'training_data': self.training_data,
                'context_memory': self.context_memory,
                'metadata': {
                    'created_at': datetime.now().isoformat(),
                    'version': '3.0',
                    'model_name': 'ChatCPT 3.0',
                    'description': 'Türkçe Yapay Zeka Modeli',
                    'training_samples': len(self.training_data),
                    'vocabulary_size': len(self.vocabulary),
                    'language': 'Turkish',
                    'capabilities': ['chat', 'search', 'learn', 'context_memory']
                }
            }
            
            with open(f"{self.model_path}/model.pkl", 'wb') as f:
                pickle.dump(model_data, f)
            
            print(f"💾 Model kaydedildi: {self.model_path}")
            
        except Exception as e:
            print(f"❌ Model kaydetme hatası: {e}")
    
    def load_model(self):
        """Modeli yükler"""
        try:
            with open(f"{self.model_path}/model.pkl", 'rb') as f:
                model_data = pickle.load(f)
            
            self.model_name = model_data['model_name']
            self.vocabulary = model_data['vocabulary']
            self.word_embeddings = model_data['word_embeddings']
            self.response_patterns = model_data['response_patterns']
            self.training_data = model_data['training_data']
            self.context_memory = model_data.get('context_memory', [])
            
            metadata = model_data.get('metadata', {})
            print(f"📥 ChatCPT 3.0 Model yüklendi: {self.model_name}")
            print(f"   � Vertsiyon: {metadata.get('version', '3.0')}")
            print(f"   �  Eğitim örnekleri: {metadata.get('training_samples', 0)}")
            print(f"   📝 Türkçe kelime sayısı: {metadata.get('vocabulary_size', 0)}")
            print(f"   🧠 Yanıt kalıbı: {len(self.response_patterns)}")
            print(f"   🌍 Dil: {metadata.get('language', 'Turkish')}")
            
        except Exception as e:
            print(f"❌ Model yükleme hatası: {e}")
            self.create_new_model()
    
    def get_model_info(self):
        """Model bilgilerini döndürür"""
        return {
            'model_name': self.model_name,
            'vocabulary_size': len(self.vocabulary),
            'response_patterns': len(self.response_patterns),
            'training_samples': len(self.training_data),
            'context_memory': len(self.context_memory),
            'model_path': self.model_path
        }
    
    def export_model(self, export_path):
        """Modeli dışa aktarır"""
        try:
            import shutil
            shutil.copytree(self.model_path, export_path)
            print(f"📤 Model dışa aktarıldı: {export_path}")
        except Exception as e:
            print(f"❌ Dışa aktarma hatası: {e}")

class AIModelInterface:
    """AI Model kullanım arayüzü"""
    
    def __init__(self):
        self.model = AIModel()
        self.setup_search_engine()
    
    def setup_search_engine(self):
        """Arama motorunu ayarlar"""
        try:
            from api_config import is_api_configured
            if is_api_configured():
                from search_engine import GoogleSearchEngine
                self.search_engine = GoogleSearchEngine()
                print("🔍 Google Search API aktif")
            else:
                self.search_engine = None
                print("🔍 Arama motoru yok")
        except:
            self.search_engine = None
    
    def chat(self, user_input):
        """Sohbet fonksiyonu"""
        # Özel komutları kontrol et
        if user_input.lower().startswith('ara:'):
            return self.search_and_learn(user_input[4:].strip())
        
        # Model ile tahmin yap
        response, confidence = self.model.predict(user_input)
        
        if response and confidence > 0.3:
            return f"{response}\n\n🤖 [ChatCPT 3.0 - Güven: {confidence:.2f}]"
        else:
            return "Bu konu hakkında daha fazla bilgi edinmek için 'ara: [konu]' yazabilirsiniz."
    
    def search_and_learn(self, query):
        """Arama yapar ve öğrenir"""
        if not self.search_engine:
            return "⚠️ Arama motoru mevcut değil."
        
        try:
            print(f"🔍 '{query}' araştırılıyor...")
            results = self.search_engine.search(query, num_results=3)
            
            if results:
                search_info = f"📊 **'{query}' hakkında güncel bilgiler:**\n\n"
                
                for i, result in enumerate(results, 1):
                    title = result.get('title', 'Başlık yok')[:80]
                    snippet = result.get('snippet', 'Açıklama yok')[:150]
                    
                    search_info += f"**{i}. {title}**\n"
                    search_info += f"   {snippet}...\n\n"
                
                # Modeli güncelle
                self.model.learn_from_interaction(query, search_info)
                
                return search_info
            else:
                return f"❌ '{query}' hakkında bilgi bulunamadı."
                
        except Exception as e:
            return f"⚠️ Arama hatası: {str(e)[:100]}"
    
    def train_with_new_data(self, new_training_file):
        """Yeni verilerle eğitim yapar"""
        try:
            with open(new_training_file, 'r', encoding='utf-8') as f:
                new_data = json.load(f)
            
            self.model.fine_tune(new_data)
            return f"✅ {len(new_data)} yeni veri ile model eğitildi!"
            
        except Exception as e:
            return f"❌ Eğitim hatası: {e}"
    
    def get_stats(self):
        """İstatistikleri döndürür"""
        return self.model.get_model_info()
    
    def interactive_mode(self):
        """Etkileşimli mod"""
        print(f"\n🤖 ChatCPT 3.0 - Türkçe AI Modeli Aktif!")
        print("🚀 ChatCPT 3.0 v3.0 - Gelişmiş Türkçe Yapay Zeka")
        print("=" * 60)
        print("Komutlar:")
        print("  • 'çıkış' - Programdan çık")
        print("  • 'bilgi' - Model bilgileri")
        print("  • 'ara: [konu]' - Arama yap ve öğren")
        print("  • 'eğit: [dosya]' - Yeni verilerle eğit")
        print("=" * 50)
        
        while True:
            try:
                user_input = input("\n👤 Siz: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['çıkış', 'exit', 'quit']:
                    print("👋 ChatCPT 3.0 kaydediliyor ve çıkılıyor...")
                    print("💾 ChatCPT 3.0 modeli güvenli bir şekilde kaydedildi!")
                    self.model.save_model()
                    break
                
                elif user_input.lower() in ['bilgi', 'info']:
                    stats = self.get_stats()
                    print("\n📊 **ChatCPT 3.0 Model Bilgileri:**")
                    print("🚀 Model: ChatCPT 3.0 - Türkçe AI")
                    print("📅 Versiyon: 3.0")
                    for key, value in stats.items():
                        print(f"   📈 {key}: {value}")
                
                elif user_input.lower().startswith('eğit:'):
                    file_path = user_input[5:].strip()
                    result = self.train_with_new_data(file_path)
                    print(f"\n🤖 AI: {result}")
                
                else:
                    response = self.chat(user_input)
                    print(f"\n🤖 AI: {response}")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Program sonlandırıldı.")
                self.model.save_model()
                break
            except Exception as e:
                print(f"\n❌ Hata: {e}")

def display_chatcpt_banner():
    """ChatCPT 3.0 banner'ını gösterir"""
    banner = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║           🤖 ChatCPT 3.0 - TÜRKÇE AI MODELİ 🚀              ║
║                                                              ║
║                    Versiyon: 3.0                             ║
║                                                              ║
║  ✨ Gelişmiş Türkçe Dil Modeli                               ║
║  🧠 Akıllı Yanıt Sistemi                                     ║
║  🔍 Google Arama Entegrasyonu                                ║
║  📚 Sürekli Öğrenme Yeteneği                                 ║
║  💾 Model Kaydetme ve Yükleme                                ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""
    print(banner)

def main():
    """Ana program"""
    display_chatcpt_banner()
    
    try:
        ai_interface = AIModelInterface()
        ai_interface.interactive_mode()
    except Exception as e:
        print(f"❌ ChatCPT 3.0 sistem hatası: {e}")
        print("💡 Lütfen gerekli dosyaların mevcut olduğundan emin olun.")

if __name__ == "__main__":
    main()