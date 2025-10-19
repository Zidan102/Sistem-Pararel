import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

clients = []

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handle_client(client_socket, address):
    print(f"[TERHUBUNG] {address} bergabung ke chat.")
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            print(f"[PESAN dari {address}] {message.decode()}")
            broadcast(message, client_socket)
        except:
            # Jika client disconnect
            print(f"[PUTUS] Koneksi dari {address} terputus.")
            clients.remove(client_socket)
            client_socket.close()
            break

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[MENUNGGU KONEKSI] Server berjalan di {HOST}:{PORT}")

    while True:
        client_socket, address = server.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.start()
        print(f"[AKTIF] Jumlah client: {len(clients)}")

if __name__ == "__main__":
    start_server()
