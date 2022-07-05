import socket
import time


BUFF_SIZE = 4096


def main(addr='127.0.0.1', port=20000):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # client.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    address = ('192.168.31.36', 20000)
    msg = b'123'
    while True:
        # time.sleep(0.001)
        client.sendto(msg, address)


if __name__ == '__main__':
    main(addr='192.168.31.36')

"""
one1 time is: 0.0
3
one1 time is: 0.0
3
one1 time is: 0.0
3
one1 time is: 0.000997304916381836
3
one1 time is: 0.0
3
one1 time is: 0.0
3
"""