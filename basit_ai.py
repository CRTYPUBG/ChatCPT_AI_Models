#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Basit AI Sistemi - Kesinlikle Çalışır!
Hiçbir karmaşık kütüphane gerektirmez
"""

import json
import os
import random
import re
from datetime import datetime

class BasitAI:
    def __init__(self):
        print("🤖 Basit AI Sistemi başlatılıyor...")
        
        # Eğitim verisini yükle
        self.egitim_verisi = self.egitim_verisi_yukle()
        
        # Bilgi tabanı
        self.bilgi_tabani = self.bilgi_tabani_yukle()
        
        # Arama motoru
        self.arama_motoru = self.arama_motoru_ayarla()
        
        print("✅ AI Sistemi hazır!")
    
    def egitim_verisi_yukle(self):
        """Eğitim verisini yükler"""
        try:
            with open("eğitim_verisi.json", 'r', encoding='utf-8') as f:
                data = json.load(f)
            print(f"📚 {len(data)} eğitim verisi yüklendi")
            return data
        except:
            print("⚠️ Eğitim verisi yüklenemedi, varsayılan veriler kullanılacak")
            return [
                {
                    "instruction": "Merhaba nasılsın?",
                    "input": "Selamlama",
                    "output": "Merhaba! Ben bir AI asistanıyım. Size nasıl yardımcı olabilirim?"
                }
            ]
    
    def bilgi_tabani_yukle(self):
        """Bilgi tabanını yükler"""
        try:
            with open("knowledge_base.json", 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {
                "learned_facts": {},
                "last_update": datetime.now().isoformat()
            }
    
    def bilgi_tabani_kaydet(self):
        """Bilgi tabanını kaydeder"""
        try:
            self.bilgi_tabani["last_update"] = datetime.now().isoformat()
            with open("knowledge_base.json", 'w', encoding='utf-8') as f:
                json.dump(self.bilgi_tabani, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"⚠️ Bilgi tabanı kaydetme hatası: {e}")
    
    def arama_motoru_ayarla(self):
        """Arama motorunu ayarlar"""
        try:
            # Google API kontrolü
            from api_config import is_api_configured
            if is_api_configured():
                from search_engine import GoogleSearchEngine
                print("🔍 Google Search API aktif")
                return GoogleSearchEngine()
            else:
                print("🔍 Ücretsiz arama modu")
                return None
        except:
            print("🔍 Arama motoru yok - sadece eğitim verisi kullanılacak")
            return None
    
    def kelime_benzerlik(self, metin1, metin2):
        """İki metin arasındaki benzerliği hesaplar"""
        kelimeler1 = set(metin1.lower().split())
        kelimeler2 = set(metin2.lower().split())
        
        if not kelimeler1 or not kelimeler2:
            return 0
        
        ortak = kelimeler1.intersection(kelimeler2)
        toplam = kelimeler1.union(kelimeler2)
        
        return len(ortak) / len(toplam) if toplam else 0
    
    def en_iyi_cevap_bul(self, soru):
        """Eğitim verisinde en iyi cevabı bulur"""
        en_iyi_skor = 0
        en_iyi_cevap = None
        
        soru_temiz = re.sub(r'[^\w\s]', '', soru.lower())
        
        for veri in self.egitim_verisi:
            instruction = veri.get("instruction", "")
            input_text = veri.get("input", "")
            output = veri.get("output", "")
            
            # Instruction ile karşılaştır
            skor1 = self.kelime_benzerlik(soru_temiz, instruction)
            
            # Input ile karşılaştır
            skor2 = self.kelime_benzerlik(soru_temiz, input_text) if input_text else 0
            
            # En yüksek skoru al
            skor = max(skor1, skor2)
            
            if skor > en_iyi_skor and skor > 0.1:  # Minimum eşik
                en_iyi_skor = skor
                en_iyi_cevap = output
        
        return en_iyi_cevap, en_iyi_skor
    
    def bilgi_tabaninda_ara(self, soru):
        """Bilgi tabanında arama yapar"""
        soru_kelimeler = set(soru.lower().split())
        
        for anahtar, bilgi in self.bilgi_tabani["learned_facts"].items():
            anahtar_kelimeler = set(anahtar.lower().replace('_', ' ').split())
            
            if soru_kelimeler.intersection(anahtar_kelimeler):
                return bilgi.get("content", "")
        
        return None
    
    def cevap_uret(self, soru):
        """Ana cevap üretme fonksiyonu"""
        soru_kucuk = soru.lower()
        
        # Selamlama kontrolü
        selamlamalar = ["merhaba", "selam", "iyi günler", "nasılsın", "hey"]
        if any(selam in soru_kucuk for selam in selamlamalar):
            cevaplar = [
                "Merhaba! Size nasıl yardımcı olabilirim?",
                "Selam! Hangi konuda bilgi almak istiyorsunuz?",
                "İyi günler! Ben AI asistanınızım.",
                "Hoş geldiniz! Sorularınızı bekliyorum."
            ]
            return random.choice(cevaplar)
        
        # Teşekkür kontrolü
        tesekkurler = ["teşekkür", "sağol", "mersi", "eyvallah"]
        if any(tesekkur in soru_kucuk for tesekkur in tesekkurler):
            return "Rica ederim! Başka sorunuz var mı?"
        
        # Bilgi tabanında ara
        bilgi_cevabi = self.bilgi_tabaninda_ara(soru)
        if bilgi_cevabi:
            return f"{bilgi_cevabi}\n\n💡 [Kaynak: Öğrenilmiş Bilgi]"
        
        # Eğitim verisinde ara
        egitim_cevabi, skor = self.en_iyi_cevap_bul(soru)
        if egitim_cevabi and skor > 0.2:
            return f"{egitim_cevabi}\n\n📚 [Kaynak: Eğitim Verisi - Benzerlik: {skor:.2f}]"
        
        # Varsayılan cevaplar
        varsayilan_cevaplar = [
            "Bu konu hakkında daha fazla bilgi edinmek için araştırma yapabilirim.",
            "İlginç bir soru! Size daha detaylı bilgi verebilmek için araştırayım.",
            "Bu konuda güncel bilgi almak istiyorsanız 'ara: [konu]' yazabilirsiniz.",
            "Maalesef bu soruya kesin bir yanıt veremiyorum. Başka bir şekilde sorar mısınız?"
        ]
        
        return random.choice(varsayilan_cevaplar)
    
    def arama_yap(self, konu):
        """Arama yapar ve sonuçları döndürür"""
        if not self.arama_motoru:
            return "⚠️ Arama motoru mevcut değil. Sadece eğitim verisi kullanılıyor."
        
        try:
            print(f"🔍 '{konu}' araştırılıyor...")
            
            # Google arama
            sonuclar = self.arama_motoru.search(konu, num_results=3)
            
            if sonuclar:
                arama_bilgisi = f"📊 **'{konu}' için güncel bilgiler:**\n\n"
                
                for i, sonuc in enumerate(sonuclar, 1):
                    baslik = sonuc.get('title', 'Başlık yok')[:80]
                    aciklama = sonuc.get('snippet', 'Açıklama yok')[:150]
                    link = sonuc.get('link', '')
                    
                    arama_bilgisi += f"**{i}. {baslik}**\n"
                    arama_bilgisi += f"   {aciklama}...\n"
                    if link:
                        arama_bilgisi += f"   🔗 {link}\n"
                    arama_bilgisi += "\n"
                
                # Bilgi tabanına kaydet
                self.yeni_bilgi_ogren(konu, arama_bilgisi, "google_arama")
                
                arama_bilgisi += f"🕒 **Arama Zamanı:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                
                return arama_bilgisi
            else:
                return f"❌ '{konu}' hakkında bilgi bulunamadı."
                
        except Exception as e:
            return f"⚠️ Arama hatası: {str(e)[:100]}"
    
    def yeni_bilgi_ogren(self, konu, bilgi, kaynak):
        """Yeni bilgiyi öğrenir ve kaydeder"""
        try:
            konu_anahtar = re.sub(r'[^\w\s]', '', konu.lower()).replace(' ', '_')[:50]
            
            self.bilgi_tabani["learned_facts"][konu_anahtar] = {
                "content": bilgi,
                "source": kaynak,
                "learned_at": datetime.now().isoformat()
            }
            
            self.bilgi_tabani_kaydet()
            print(f"✅ Yeni bilgi öğrenildi: {konu[:30]}...")
            
        except Exception as e:
            print(f"⚠️ Öğrenme hatası: {e}")
    
    def kendini_gelistir(self):
        """Kendini geliştirme süreci"""
        print("🚀 Kendini geliştirme başlatılıyor...")
        
        if not self.arama_motoru:
            print("❌ Arama motoru yok, kendini geliştirme yapılamıyor.")
            return
        
        konular = [
            "yapay zeka 2024 gelişmeler",
            "teknoloji haberleri güncel",
            "Python programlama yenilikleri",
            "bilim haberleri son dakika"
        ]
        
        basarili = 0
        for konu in konular:
            try:
                print(f"📚 {konu} araştırılıyor...")
                sonuc = self.arama_yap(konu)
                if "güncel bilgiler" in sonuc:
                    basarili += 1
                    print(f"✅ {konu} güncellendi")
                else:
                    print(f"⚠️ {konu} güncellenemedi")
            except Exception as e:
                print(f"❌ {konu} hatası: {e}")
        
        print(f"✨ Kendini geliştirme tamamlandı! {basarili}/{len(konular)} konu güncellendi.")
    
    def istatistikler(self):
        """Sistem istatistiklerini gösterir"""
        stats = {
            "Eğitim Verisi Sayısı": len(self.egitim_verisi),
            "Öğrenilen Bilgi Sayısı": len(self.bilgi_tabani["learned_facts"]),
            "Son Güncelleme": self.bilgi_tabani.get("last_update", "Bilinmiyor"),
            "Arama Motoru": "Google API" if self.arama_motoru else "Yok",
            "Sistem Durumu": "Aktif ✅"
        }
        
        print("\n📊 **Sistem İstatistikleri:**")
        print("-" * 40)
        for anahtar, deger in stats.items():
            print(f"   📈 {anahtar}: {deger}")
    
    def sohbet_baslat(self):
        """Ana sohbet döngüsü"""
        print("\n🤖 Basit AI Sistemi Aktif!")
        print("=" * 50)
        print("Komutlar:")
        print("  • 'çıkış' - Programdan çık")
        print("  • 'istatistik' - Sistem bilgileri")
        print("  • 'geliştir' - Kendini geliştir")
        print("  • 'ara: [konu]' - Güncel bilgi ara")
        print("=" * 50)
        
        while True:
            try:
                kullanici_girisi = input("\n👤 Siz: ").strip()
                
                if not kullanici_girisi:
                    continue
                
                # Çıkış kontrolü
                if kullanici_girisi.lower() in ['çıkış', 'exit', 'quit', 'bye']:
                    print("👋 Görüşmek üzere!")
                    break
                
                # İstatistik kontrolü
                elif kullanici_girisi.lower() in ['istatistik', 'stats']:
                    self.istatistikler()
                
                # Kendini geliştirme kontrolü
                elif kullanici_girisi.lower() in ['geliştir', 'improve']:
                    self.kendini_gelistir()
                
                # Arama kontrolü
                elif kullanici_girisi.lower().startswith('ara:'):
                    arama_konusu = kullanici_girisi[4:].strip()
                    if arama_konusu:
                        sonuc = self.arama_yap(arama_konusu)
                        print(f"\n🤖 AI: {sonuc}")
                    else:
                        print("❌ Arama konusu boş!")
                
                # Normal soru-cevap
                else:
                    cevap = self.cevap_uret(kullanici_girisi)
                    print(f"\n🤖 AI: {cevap}")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Program sonlandırıldı.")
                break
            except Exception as e:
                print(f"\n❌ Hata: {e}")
                print("💡 Lütfen tekrar deneyin.")

def main():
    """Ana program"""
    print("🚀 Basit AI Sistemi")
    print("=" * 30)
    
    try:
        ai = BasitAI()
        ai.sohbet_baslat()
    except Exception as e:
        print(f"❌ Sistem hatası: {e}")
        print("💡 Gerekli dosyaları kontrol edin.")

if __name__ == "__main__":
    main()