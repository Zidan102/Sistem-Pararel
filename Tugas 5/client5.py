import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

def terima_pesan(client_socket):
    while True:
        try:
            pesan = client_socket.recv(1024).decode()
            if pesan:
                print(f"\n{pesan}")
        except:
            print("\n[ERROR] Terputus dari server.")
            client_socket.close()
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((HOST, PORT))
        print(f"[TERHUBUNG] ke server {HOST}:{PORT}")
    except:
        print("[GAGAL] Tidak dapat terhubung ke server.")
        return

    thread = threading.Thread(target=terima_pesan, args=(client_socket,))
    thread.start()

    while True:
        pesan = input("")
        if pesan.lower() == "keluar":
            print("[DISKONEKSI] Kamu keluar dari chat.")
            client_socket.close()
            break
        try:
            client_socket.send(pesan.encode())
        except:
            print("[ERROR] Tidak dapat mengirim pesan.")
            break

if __name__ == "__main__":
    start_client()
