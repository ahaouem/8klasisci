import socket

# Ustawienia klienta
IP_ADDRESS = "192.168.31.21"
PORT = 1234

# Tworzymy gniazdo
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Łączymy się z serwerem
client_socket.connect((IP_ADDRESS, PORT))

# Wysyłamy dane do serwera
client_socket.send(b'Wiadomosc od klienta')

# Odbieramy dane od serwera
data = client_socket.recv(1024).decode()
print("Otrzymano od serwera: %s" % data)

# Zamykamy połączenie
client_socket.close()