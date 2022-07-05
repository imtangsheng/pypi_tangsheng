from socketserver import ThreadingUDPServer, StreamRequestHandler

class MyStreamRequestHandlerr(StreamRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        msg, sock = self.request
        while True:
            sock.sendto(resp.encode('ascii'), self.client_address)

if __name__ == '__main__':
    # serv = TCPServer(('', 20000), EchoHandler)
    # serv.serve_forever()
    address = ("127.0.0.1", 43015)
    server = ThreadingUDPServer(address, MyStreamRequestHandlerr)
    server.serve_forever()