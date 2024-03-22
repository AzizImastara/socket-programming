# Client - Server (Single Thread)

## Soal & Jawaban

1. Membuat sebuah program server yang dapat menerima koneksi dari klien menggunakan protokol TCP. Server ini akan menerima pesan dari klien dan mengirimkan pesan balasan berisi jumlah karakter pada pesan tersebut. Gunakan port 12345 untuk server. Membuat analisa dari hasil program tersebut

### Kode:

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = 'localhost'
PORT = 12345

server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Waiting...")

while True:
    client_socket, client_address = server_socket.accept()
    print("Connection from:", client_address)

    data = client_socket.recv(1024)
    message = data.decode()

    character_count = len(message)
    response = "Jumlah karakter: " + str(character_count)
    
    print("Request dari client :", character_count, "IP client :", client_address)
    client_socket.sendall(response.encode())

    client_socket.close()


### Output


2. Membuat sebuah program klien yang dapat terhubung ke server yang telah dibuat pada soal nomor 1. Klien ini akan mengirimkan pesan ke server berupa inputan dari pengguna dan menampilkan pesan balasan jumlah karakter yang diterima dari server. Membuat analisa dari hasil program tersebut

### Kode:

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = 'localhost'
PORT = 12345

client_socket.connect((HOST, PORT))

pesan = input("Masukkan pesan: ")
client_socket.sendall(pesan.encode())

data = client_socket.recv(1024)
print(data.decode())

client_socket.close()

### Output

Untuk membuat implementasi aplikasi Client-Server Sederhana (Single Thread) pada Python, 
dapat menggunakan modul socket dan threading yang sudah disediakan oleh Python.

Pada code yang saya berikan, server akan menunggu koneksi dari client dan membaca data yang 
dikirimkan oleh client. Kemudian, server akan mengirim balasan ke client dan menutup 
koneksi. Client akan mengirimkan pesan ke server dan menunggu balasan dari server. Setelah 
menerima balasan dari server, koneksi akan ditutup. 

Program tersebut merupakan contoh sederhana dari aplikasi client-server dengan model single
threaded, di mana server hanya mampu melayani satu koneksi pada suatu waktu. Jika 
terdapat lebih dari satu koneksi yang masuk, maka koneksi tersebut akan diantre dan dilayani 
secara berurutan. 

 
