# Gerekli kütüphaneleri yükleme
import torch
from unsloth import FastLanguageModel
from datasets import load_dataset
from trl import SFTTrainer
from transformers import TrainingArguments

# Modeli ve tokenizer'ı yükleme
# Model olarak küçük ama güçlü olan Mistral 7B'yi seçelim.
max_seq_length = 2048
dtype = None # Bfloat16 için None, float16 için torch.float16
load_in_4bit = True

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/mistral-7b-instruct-v0.2-bnb-4bit",
    max_seq_length = max_seq_length,
    dtype = dtype,
    load_in_4bit = load_in_4bit,
)

# LoRA ile modelin eğitilebilir katmanlarını ayarlama
model = FastLanguageModel.get_peft_model(
    model,
    r = 16,
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj",],
    lora_alpha = 16,
    lora_dropout = 0,
    bias = "none",
    use_gradient_checkpointing = "unsloth",
    random_state = 3407,
)

# Hugging Face Hub'dan veri seti yükleme
# Bu, sohbet formatında bir veri setidir.
# Örneğin, "tatsu-lab/alpaca" veri setini kullanabiliriz.
dataset = load_dataset("json", data_files="eğitim_verisi.json", split="train")

# Veriyi modelin anlayacağı formata dönüştürme
def format_instruction(sample):
    # Bu fonksiyon, veri setinizdeki her örneği,
    # modelin anlayacağı bir diyalog formatına dönüştürür.
    instruction = sample['instruction']
    input_text = sample['input']
    output_text = sample['output']
    
    # Veri setinizdeki anahtarlar ('instruction', 'input', 'output') farklıysa,
    # yukarıdaki anahtarları değiştirmeniz gerekebilir.
    
    formatted_string = f"""### Talimat:
{instruction}

### Girdi:
{input_text}

### Yanıt:
{output_text}
"""
    return {"text": formatted_string}

# Veri setini formatlama
processed_dataset = dataset.map(format_instruction)

# Eğitim parametrelerini ayarlama
training_args = TrainingArguments(
    output_dir="./turkish-mistral-7b-finetuned",
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    warmup_steps=5,
    max_steps=60,
    learning_rate=2e-4,
    fp16=not torch.cuda.is_bf16_supported(),
    bf16=torch.cuda.is_bf16_supported(),
    logging_steps=1,
    optim="adamw_8bit",
    weight_decay=0.01,
    lr_scheduler_type="linear",
    seed=3407,
    save_strategy="steps",
    save_steps=30,
    evaluation_strategy="no",
    report_to="none",
)

# SFT Trainer'ı kurma
trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=processed_dataset,
    dataset_text_field="text",
    max_seq_length=max_seq_length,
    dataset_num_proc=2,
    packing=False,
    args=training_args,
)

# Eğitimi başlatma
print("Eğitim başlıyor...")
trainer_stats = trainer.train()

# Modeli kaydetme
print("Model kaydediliyor...")
model.save_pretrained("turkish-mistral-7b-final")
tokenizer.save_pretrained("turkish-mistral-7b-final")

# Eğitim istatistiklerini yazdırma
print(f"Eğitim tamamlandı!")
print(f"Toplam eğitim süresi: {trainer_stats.metrics['train_runtime']:.2f} saniye")
print(f"Saniye başına örnek: {trainer_stats.metrics['train_samples_per_second']:.2f}")

# Test fonksiyonu
def test_model(prompt):
    """Eğitilmiş modeli test etmek için fonksiyon"""
    FastLanguageModel.for_inference(model)
    
    inputs = tokenizer(
        [prompt],
        return_tensors="pt"
    ).to("cuda")
    
    outputs = model.generate(
        **inputs,
        max_new_tokens=256,
        use_cache=True,
        temperature=0.7,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Örnek test
print("\n=== Model Testi ===")
test_prompt = """### Talimat:
Yapay zekanın avantajları nelerdir?

### Girdi:
Yapay Zeka

### Yanıt:
"""

result = test_model(test_prompt)
print(f"Test sonucu:\n{result}")

print("\nEğitim ve test tamamlandı! Model 'turkish-mistral-7b-final' klasörüne kaydedildi.")