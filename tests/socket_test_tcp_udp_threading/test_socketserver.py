from socketserver import BaseRequestHandler, TCPServer

class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        while True:

            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(b"12"+msg)

if __name__ == '__main__':
    serv = TCPServer(('', 20000), EchoHandler)
    serv.serve_forever()


"""
----------------------------------------
Exception happened during processing of request from ('127.0.0.1', 7213)
Traceback (most recent call last):
  File "C:\Anaconda3\lib\socketserver.py", line 317, in _handle_request_noblock
    self.process_request(request, client_address)
  File "C:\Anaconda3\lib\socketserver.py", line 348, in process_request
    self.finish_request(request, client_address)
  File "C:\Anaconda3\lib\socketserver.py", line 361, in finish_request
    self.RequestHandlerClass(request, client_address, self)
  File "C:\Anaconda3\lib\socketserver.py", line 696, in __init__
    self.handle()
  File "E:\Development\1-Pre-Alpha\sound_animation\tests\test_socket\test_socketserver_client_closed.py", line 11, in handle
    self.request.send(b"12")
ConnectionResetError: [WinError 10054] 远程主机强迫关闭了一个现有的连接。
----------------------------------------

"""