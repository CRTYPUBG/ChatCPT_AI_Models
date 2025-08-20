# Konfigürasyon dosyası - Eğitim parametrelerini buradan yönetebilirsiniz

# Model konfigürasyonu
MODEL_CONFIG = {
    "model_name": "unsloth/mistral-7b-instruct-v0.2-bnb-4bit",
    "max_seq_length": 2048,
    "dtype": None,  # Bfloat16 için None, float16 için torch.float16
    "load_in_4bit": True,
}

# LoRA konfigürasyonu
LORA_CONFIG = {
    "r": 16,
    "target_modules": ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj"],
    "lora_alpha": 16,
    "lora_dropout": 0,
    "bias": "none",
    "use_gradient_checkpointing": "unsloth",
    "random_state": 3407,
}

# Eğitim konfigürasyonu
TRAINING_CONFIG = {
    "output_dir": "./turkish-mistral-7b-finetuned",
    "per_device_train_batch_size": 2,
    "gradient_accumulation_steps": 4,
    "warmup_steps": 5,
    "max_steps": 60,
    "learning_rate": 2e-4,
    "weight_decay": 0.01,
    "lr_scheduler_type": "linear",
    "seed": 3407,
    "save_strategy": "steps",
    "save_steps": 30,
    "evaluation_strategy": "no",
    "logging_steps": 1,
    "optim": "adamw_8bit",
    "report_to": "none",
}

# Veri konfigürasyonu
DATA_CONFIG = {
    "train_file": "eğitim_verisi.json",
    "dataset_num_proc": 2,
    "packing": False,
}

# Test konfigürasyonu
TEST_CONFIG = {
    "max_new_tokens": 256,
    "temperature": 0.7,
    "do_sample": True,
}