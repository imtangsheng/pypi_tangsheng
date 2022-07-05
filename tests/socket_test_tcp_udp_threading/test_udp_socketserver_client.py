from socket import socket, AF_INET, SOCK_DGRAM
import time

s = socket(AF_INET, SOCK_DGRAM)
s.sendto(b'12345'*100, ('192.168.31.36', 43019))

0
s.sendto(b'12345'*100, ("localhost", 9999))
s.sendto(b'123456'*100, ('127.0.0.1', 9999))

s
data = s.recvfrom(1024)
data[1]
(b'Wed Aug 15 20:35:08 2012', ('127.0.0.1', 20000))

from socket import socket, AF_INET, SOCK_DGRAM
import time
sock = socket(AF_INET, SOCK_DGRAM)

sock.bind(('127.0.0.1', 43011))
sock.recvfrom(8192)

def time_server(address):
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(address)
    while True:
        msg, addr = sock.recvfrom(8192)
        print('Got message from', addr)
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), addr)

if __name__ == '__main__':
    time_server(('', 20000))