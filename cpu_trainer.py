# CPU Modunda Model Eğitimi
import json
import torch
from transformers import (
    AutoTokenizer, 
    AutoModelForCausalLM, 
    TrainingArguments, 
    Trainer,
    DataCollatorForLanguageModeling
)
from datasets import Dataset
import os
from datetime import datetime

class CPUTrainer:
    """
    CPU modunda model eğitimi için sınıf
    """
    
    def __init__(self):
        self.model_name = "microsoft/DialoGPT-small"  # CPU için küçük model
        self.output_dir = "./cpu-trained-model"
        self.tokenizer = None
        self.model = None
        
    def load_model_and_tokenizer(self):
        """
        Model ve tokenizer'ı yükler
        """
        print("📥 Model ve tokenizer yükleniyor...")
        
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForCausalLM.from_pretrained(self.model_name)
            
            # Pad token ekle
            if self.tokenizer.pad_token is None:
                self.tokenizer.pad_token = self.tokenizer.eos_token
            
            print("✅ Model ve tokenizer başarıyla yüklendi!")
            return True
            
        except Exception as e:
            print(f"❌ Model yükleme hatası: {e}")
            return False
    
    def prepare_dataset(self):
        """
        Eğitim verisini hazırlar
        """
        print("📚 Eğitim verisi hazırlanıyor...")
        
        try:
            # Eğitim verisini yükle
            with open("eğitim_verisi.json", 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Veriyi dönüştür
            texts = []
            for item in data:
                instruction = item.get("instruction", "")
                input_text = item.get("input", "")
                output = item.get("output", "")
                
                # Basit format
                if input_text:
                    text = f"Soru: {instruction} {input_text} Cevap: {output}"
                else:
                    text = f"Soru: {instruction} Cevap: {output}"
                
                texts.append(text)
            
            # Dataset oluştur
            dataset = Dataset.from_dict({"text": texts})
            
            # Tokenize et
            def tokenize_function(examples):
                return self.tokenizer(
                    examples["text"], 
                    truncation=True, 
                    padding=True, 
                    max_length=512
                )
            
            tokenized_dataset = dataset.map(tokenize_function, batched=True)
            
            print(f"✅ {len(texts)} örnek hazırlandı!")
            return tokenized_dataset
            
        except Exception as e:
            print(f"❌ Veri hazırlama hatası: {e}")
            return None
    
    def train_model(self):
        """
        Modeli eğitir
        """
        print("🏋️ Model eğitimi başlıyor...")
        
        # Model ve tokenizer yükle
        if not self.load_model_and_tokenizer():
            return False
        
        # Veriyi hazırla
        train_dataset = self.prepare_dataset()
        if train_dataset is None:
            return False
        
        # Eğitim parametreleri
        training_args = TrainingArguments(
            output_dir=self.output_dir,
            overwrite_output_dir=True,
            num_train_epochs=3,
            per_device_train_batch_size=2,
            save_steps=500,
            save_total_limit=2,
            prediction_loss_only=True,
            logging_steps=100,
            logging_dir='./logs',
            no_cuda=True,  # CPU modunda çalış
            dataloader_num_workers=0,  # Windows için
            report_to=None  # Wandb kapalı
        )
        
        # Data collator
        data_collator = DataCollatorForLanguageModeling(
            tokenizer=self.tokenizer,
            mlm=False,
        )
        
        # Trainer oluştur
        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=train_dataset,
            data_collator=data_collator,
        )
        
        try:
            # Eğitimi başlat
            print("⏳ Eğitim başlatılıyor... (Bu işlem uzun sürebilir)")
            trainer.train()
            
            # Modeli kaydet
            print("💾 Model kaydediliyor...")
            trainer.save_model()
            self.tokenizer.save_pretrained(self.output_dir)
            
            print("✅ Eğitim başarıyla tamamlandı!")
            print(f"📁 Model kaydedildi: {self.output_dir}")
            
            return True
            
        except Exception as e:
            print(f"❌ Eğitim hatası: {e}")
            return False
    
    def test_model(self):
        """
        Eğitilmiş modeli test eder
        """
        if not os.path.exists(self.output_dir):
            print("❌ Eğitilmiş model bulunamadı!")
            return
        
        try:
            print("🧪 Model test ediliyor...")
            
            # Eğitilmiş modeli yükle
            tokenizer = AutoTokenizer.from_pretrained(self.output_dir)
            model = AutoModelForCausalLM.from_pretrained(self.output_dir)
            
            # Test soruları
            test_questions = [
                "Soru: Yapay zeka nedir? Cevap:",
                "Soru: Python programlama dilinin avantajları nelerdir? Cevap:",
                "Soru: Sağlıklı beslenmenin önemi nedir? Cevap:"
            ]
            
            print("\n🎯 **Test Sonuçları:**")
            print("-" * 50)
            
            for i, question in enumerate(test_questions, 1):
                inputs = tokenizer.encode(question, return_tensors='pt')
                
                with torch.no_grad():
                    outputs = model.generate(
                        inputs, 
                        max_length=inputs.shape[1] + 100,
                        num_return_sequences=1,
                        temperature=0.7,
                        do_sample=True,
                        pad_token_id=tokenizer.eos_token_id
                    )
                
                response = tokenizer.decode(outputs[0], skip_special_tokens=True)
                answer = response[len(question):].strip()
                
                print(f"\n{i}. {question}")
                print(f"   Yanıt: {answer[:200]}...")
            
        except Exception as e:
            print(f"❌ Test hatası: {e}")

def main():
    """
    Ana eğitim fonksiyonu
    """
    print("🚀 CPU Modunda Model Eğitimi Başlatılıyor...")
    
    trainer = CPUTrainer()
    
    # Eğitimi başlat
    success = trainer.train_model()
    
    if success:
        # Modeli test et
        trainer.test_model()
        
        print("\n✅ Tüm işlemler tamamlandı!")
        print("💡 Artık AI sohbet modunda eğitilmiş modeli kullanabilirsiniz.")
    else:
        print("\n❌ Eğitim başarısız oldu!")

if __name__ == "__main__":
    main()