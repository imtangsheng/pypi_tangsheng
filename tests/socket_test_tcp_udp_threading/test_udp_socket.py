from socket import socket, AF_INET, SOCK_DGRAM
import time


def time_server(address):
        sock = socket(AF_INET, SOCK_DGRAM)
        sock.bind(address)
        addr = ('192.168.31.35', 43019)
        sock.sendto(b'2143', addr)


if __name__ == '__main__':
        time_server(('', 20001))
