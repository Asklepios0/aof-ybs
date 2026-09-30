import os
import sys
import socket
import webbrowser
from http.server import SimpleHTTPRequestHandler, HTTPServer

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return '127.0.0.1'

def run(port=8080):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    local_ip = get_local_ip()
    
    # Try preferred port or find available
    server = None
    for p in range(port, port + 10):
        try:
            server = HTTPServer(('0.0.0.0', p), SimpleHTTPRequestHandler)
            port = p
            break
        except OSError:
            continue
            
    if not server:
        print("[!] Port bulunamadı, varsayılan tarayıcıda dosya açılıyor.")
        webbrowser.open(os.path.join(script_dir, 'index.html'))
        return

    print("=" * 65)
    print("   ANADOLU ÜNİVERSİTESİ AÖF YÖNETİM BİLİŞİM SİSTEMLERİ")
    print("                ÇALIŞMA PLATFORMU AKTİF!")
    print("=" * 65)
    print(f" [*] Bilgisayar Erişimi     : http://localhost:{port}")
    print(f" [*] Cep Telefonu / Tablet  : http://{local_ip}:{port}")
    print("-" * 65)
    print(" [i] İpucu: Telefonunuzdan bağlanıp 'Ana Ekrana Ekle' diyerek")
    print("     internetsiz de çalışan mobil uygulama olarak yükleyebilirsiniz!")
    print("=" * 65)
    print(" [*] Tarayıcınız açılıyor...")
    print(" [*] Sunucuyu kapatmak için pencereyi kapatın veya Ctrl+C tuşlayın.\n")
    
    webbrowser.open(f"http://localhost:{port}")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[+] Sunucu kapatıldı. İyi çalışmalar dileriz!")
        server.server_close()

if __name__ == '__main__':
    run()
