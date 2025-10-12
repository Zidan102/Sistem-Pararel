import socket

# Konfigurasi client (sesuaikan dengan server)
HOST = '127.0.0.1'  # alamat IP server
PORT = 65432        # port server

# Buat socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect ke server
client_socket.connect((HOST, PORT))
print(f"Terhubung ke server {HOST}:{PORT}")

while True:
    pesan = input("Ketik pesan (atau 'exit' untuk keluar): ")
    if pesan.lower() == 'exit':
        break

    # Kirim pesan ke server
    client_socket.sendall(pesan.encode())

    # Terima balasan dari server
    data = client_socket.recv(1024)
    print(f"Balasan dari server: {data.decode()}")

client_socket.close()