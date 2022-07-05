from socket import socket, AF_INET, SOCK_STREAM
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 20000))
s.send(b'Hello')

s.send(b's123')
s.recv(145)
s.close()

print("er")


ss = socket(AF_INET, SOCK_STREAM)
ss.connect(('localhost', 20000))
ss.send(b'ss123')
ss.recv(145)
ss.close()


Within a client, you would do this:

from socket import socket, AF_INET, SOCK_STREAM

secret_key = b'peekaboo'

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 18000))
client_authenticate(s, secret_key)
s.send(b'Hello World')
resp = s.recv(1024)
resp

from socket import socket, AF_INET, SOCK_STREAM
s = socket(AF_INET, SOCK_STREAM)
s.connect(('192.168.31.35', 43012))
s.send(b'Hello')
s.connect(('192.168.31.35', 43012))

s.send(b's123')
s.recv(102400000)