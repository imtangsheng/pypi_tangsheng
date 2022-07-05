from socketserver import ThreadingTCPServer, StreamRequestHandler
import socket
import time

BUFF_SIZE = 4096  # 4 KiB


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


def test():
    cliet_host, cliet_port = '192.168.31.35', 43014
    print('*****waiting connertion TCPServer*****')
    cliet_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliet_tcp.connect((cliet_host, cliet_port))
    while True:
        try:
            t1 = time.time()
            data_recv = recvall(cliet_tcp)
            if not data_recv:
                break
            print("time is:", time.time() - t1)
        except Exception as err:
            print("Error is:", err)
            break


if __name__ == '__main__':
    test()
