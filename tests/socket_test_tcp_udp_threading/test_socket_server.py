import socket
import time


def main(address=('', 20000), backlog=5):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    sock.bind(address)
    sock.listen(backlog)
    client_sock, client_addr = sock.accept()
    print('Got connection from {}'.format(client_addr))
    msg2 = b'123'
    while True:
        time.sleep(0.001)
        client_sock.sendall(msg2)


if __name__ == '__main__':
    main()

"""
one1 time is: 0.039188385009765625
get
12
one1 time is: 0.04019451141357422
get
12
one1 time is: 0.03909444808959961
get
12

no_delay client
one1 time is: 0.04008603096008301
get
9
one1 time is: 0.0390925407409668
get
12
one1 time is: 0.040120601654052734
get
12
one1 time is: 0.04012584686279297
get

no_delay server
one1 time is: 0.01097249984741211
get
3
one1 time is: 0.00997471809387207
get
3
one1 time is: 0.006978750228881836
get
3
one1 time is: 0.010091543197631836
get
3
one1 time is: 0.01006317138671875
get

one1 time is: 0.0010180473327636719
get
3
one1 time is: 0.0
get
3
one1 time is: 0.0009975433349609375
get
3
one1 time is: 0.000997304916381836
get
3
one1 time is: 0.0010161399841308594
get
3
one1 time is: 0.0009970664978027344
get

one1 time is: 0.0
get
300
one1 time is: 0.000997304916381836
get
216
one1 time is: 0.000997304916381836
one1 time is: 0.0
get
141
one1 time is: 0.0009975433349609375
get
3
one1 time is: 0.0
get
123
one1 time is: 0.0
get
3
one1 time is: 0.0
get
111
one1 time is: 0.0
get
3
one1 time is: 0.0009970664978027344
get
144
one1 time is: 0.0
get
3
one1 time is: 0.0
get
120
one1 time is: 0.0
get
3
one1 time is: 0.000997304916381836
get
108
one1 time is: 0.0
get
"""