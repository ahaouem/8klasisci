import socket
import struct

#target host address
target_host = "192.168.88.1"

#create raw socket
client = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

#create packet header
packet_header = struct.pack('!BBHHH', 8, 0, 0, 1, 0)

#create packet data
packet_data = b"Hello World!"

#create packet
packet = packet_header + packet_data

while True:
    #send packet to target
    client.sendto(packet, (target_host, 0))