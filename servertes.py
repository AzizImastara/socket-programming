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

    try:
        angka = int(message)
        print("Request dari client:", angka, "IP client:", client_address)

        if angka % 2 == 0:
            response = "angka " + str(angka) + " merupakan genap"
        else:
            response = "angka " + str(angka) + " merupakan ganjil"
    except ValueError:
        character_count = len(message)
        print("Request dari client:", character_count, "IP client:", client_address)
        response = "Jumlah karakter: " + str(character_count)

    client_socket.sendall(response.encode())

    client_socket.close()
