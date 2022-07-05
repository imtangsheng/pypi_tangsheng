import socket
import time


BUFF_SIZE = 4096


def recvall(sock):
    data = b''
    while True:
        print("get")
        part = sock.recv(BUFF_SIZE)
        data += part
        if len(part) < BUFF_SIZE:
            # either 0 or end of data
            break
    print(len(data))
    return data


def main(addr='127.0.0.1', port=20000):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    client.connect((addr, port))

    print('connection from {}'.format(addr))

    while True:
        st1 = time.time()
        points_binascii = recvall(client)
        print("one1 time is:", time.time() - st1)
        if not points_binascii:
            break


if __name__ == '__main__':
    main(addr='192.168.3.101', port=43014)

