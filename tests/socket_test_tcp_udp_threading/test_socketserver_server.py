import os
import sys
import time
import socket
import socketserver
from socketserver import ThreadingTCPServer, StreamRequestHandler

"""
https://github.com/python/cpython/blob/3.7/Lib/socketserver.py

self.connection = self.request
    # Disable nagle algorithm for this socket, if True.
    # Use only when wbufsize != 0, to avoid small packets.
    disable_nagle_algorithm = False
if self.disable_nagle_algorithm:
            self.connection.setsockopt(socket.IPPROTO_TCP,
                                       socket.TCP_NODELAY, True)
"""
class MyTCPHandler(StreamRequestHandler):
    # disable_nagle_algorithm = True
    def handle(self):
        # self.disable_nagle_algorithm = True
        print("{} wrote:".format(self.client_address[0]))
        # setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        # self.request.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        # sock = self.connection
        # sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        send_msg = b'1'*1500
        len(send_msg)
        while True:
            try:
                time.sleep(0.001)
                self.request.send(send_msg)
            except Exception as inst:
                # print(err)
                print("Error123:", inst)
                break


if __name__ == '__main__':
    print(sys.version)
    HOST, PORT = '', 20000
    print('***********************')
    # Create the server, binding to localhost on port 43013
    server = ThreadingTCPServer((HOST, PORT), MyTCPHandler)


    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    print("******等待连接*******")
    ip, port = server.server_address
    print('ip is:', ip)
    print('port is:', port)
    server.serve_forever()
    print('********over***********')
    os.system("pause")

"""
one1 time is: 0.009075641632080078
get
3
one1 time is: 0.011029243469238281
get
3
one1 time is: 0.01006937026977539
get
3
one1 time is: 0.009974479675292969
get
"""

800*4