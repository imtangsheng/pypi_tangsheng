from socketserver import ThreadingTCPServer, StreamRequestHandler
import socket
import time

BUFF_SIZE = 4096  # 4 KiB


# The data is too large to send
def recvall(sock):
    data = b''
    while True:
        print("get")
        part = sock.recv(BUFF_SIZE)
        data += part
        if len(part) < BUFF_SIZE:
            # either 0 or end of data
            return part
    print(len(data))
    return part


class MyStreamRequestHandlerr(StreamRequestHandler):
    disable_nagle_algorithm = True

    def handle(self):
        print('Got connection from', self.client_address)
        cliet_host, cliet_port = '192.168.31.35', 43012
        print('*****waiting connertion TCPServer*****')
        cliet_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliet_tcp.connect((cliet_host, cliet_port))

        addr_bind = ('', 43021)
        addr_send = ('127.0.0.1', 43020)

        udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_server.bind(addr_bind)
        # clear data
        recvall(cliet_tcp)

        while True:
            try:
                t1 = time.time()
                data_recv_tcp = recvall(cliet_tcp)
                if not data_recv_tcp:
                    break
                print("tcp get time is:", time.time()-t1)

                t2 = time.time()
                udp_server.sendto(data_recv_tcp, addr_send)
                print("udp sendto time is:", time.time()-t2)

                t3 = time.time()
                data_recv_udp, addr_recv_udp = udp_server.recvfrom(BUFF_SIZE)
                print("udp recvfrom time is:", time.time()-t3)

                t4 = time.time()
                self.request.send(data_recv_udp)
                print("tcp send time is:", time.time()-t4)
                print("tcp:", len(data_recv_tcp), " udp:", len(data_recv_udp))
            except Exception as err:
                print("Error is:", err)
                break
        cliet_tcp.close()
        udp_server.close()


if __name__ == '__main__':
    HOST, PORT = '', 43014
    server = ThreadingTCPServer((HOST, PORT), MyStreamRequestHandlerr)
    server.serve_forever()
