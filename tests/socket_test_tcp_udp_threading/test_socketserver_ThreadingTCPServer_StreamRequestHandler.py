from socketserver import BaseRequestHandler, TCPServer
from socketserver import ThreadingTCPServer, StreamRequestHandler


class MyStreamRequestHandlerr(StreamRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        while True:

            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(b"12"+msg)


class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        while True:

            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(b"12"+msg)

if __name__ == '__main__':
    # serv = TCPServer(('', 20000), EchoHandler)
    # serv.serve_forever()
    server = ThreadingTCPServer(('',43019), MyStreamRequestHandlerr)
    server.serve_forever()