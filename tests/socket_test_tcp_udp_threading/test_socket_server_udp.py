import socket
import time


def main(address=1, backlog=5):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    sock.bind(('', 20000))
    # print('Got connection from {}'.format(client_addr))
    msg2 = b'123'
    # addr = ('127.0.0.1', 40138)
    
    while True:
        t1 = time.time()
        data, addr = sock.recvfrom(2048)
        print(len(data))
        print("one1 time is:", time.time() - t1)
        if not data:
            print("client has exist")
            break
    sock.close()

if __name__ == '__main__':
    main()

"""
one1 time is: 0.0019953250885009766
3
one1 time is: 0.001994609832763672
3
one1 time is: 0.0019943714141845703
3
one1 time is: 0.0019807815551757812
3
one1 time is: 0.0010192394256591797
3

one1 time is: 0.0
3
one1 time is: 0.0009961128234863281
3
one1 time is: 0.0
3
one1 time is: 0.0
3
one1 time is: 0.0
3
one1 time is: 0.0
3
one1 time is: 0.0
3
one1 time is: 0.0
3
one1 time is: 0.0
3
one1 time is: 0.0

C++
2
one1 time is: 0.010708808898925781
2
one1 time is: 0.01739358901977539
2
one1 time is: 0.012499570846557617
2
one1 time is: 0.017364978790283203
2
one1 time is: 0.014684677124023438
2
one1 time is: 0.01731419563293457
2
one1 time is: 0.01088404655456543
2
one1 time is: 0.019432783126831055
2
one1 time is: 0.01038289070129394
"""