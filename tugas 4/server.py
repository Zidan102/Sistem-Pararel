import socket

# Konfigurasi server
HOST = '127.0.0.1'  # localhost
PORT = 65432        # Port bebas, asal sama dengan client

# Buat socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind ke alamat & port
server_socket.bind((HOST, PORT))

# Server siap menerima koneksi
server_socket.listen()
print(f"Server berjalan di {HOST}:{PORT} ...")

# Terima koneksi client
conn, addr = server_socket.accept()
print(f"Terhubung dengan client: {addr}")

with conn:
    while True:
        data = conn.recv(1024)  # Menerima data max 1024 bytes
        if not data:
            break
        pesan = data.decode()
        print(f"Pesan dari client: {pesan}")

        # Balasan ke client
        balasan = f"Pesan '{pesan}' sudah diterima server."
        conn.sendall(balasan.encode())
