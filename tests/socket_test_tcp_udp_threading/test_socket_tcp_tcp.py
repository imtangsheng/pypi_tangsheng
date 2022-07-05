from socketserver import ThreadingTCPServer, StreamRequestHandler
import socket


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


class MyStreamRequestHandlerr(StreamRequestHandler):
    disable_nagle_algorithm = True

    def handle(self):
        print('Got connection from', self.client_address)
        self.connection.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)
        cliet_host, cliet_port = '127.0.0.1', 43012
        print('*****waiting connertion TCPServer*****')
        cliet_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliet_tcp.connect((cliet_host, cliet_port))
        while True:
            try:
                data_recv = recvall(cliet_tcp)
                if not data_recv:
                    break
                self.request.send(data_recv)
            except Exception as err:
                print("Error is:", err)
                break


if __name__ == '__main__':
    HOST, PORT = '', 43014
    print('************')
    server = ThreadingTCPServer((HOST, PORT), MyStreamRequestHandlerr)
    server.serve_forever()
