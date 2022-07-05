import os
import socket
import time


BUFF_SIZE = 4096  # 4 KiB


class UDPRequestHandler(object):
    def __init__(self):
        pass

    def handle(self, data):
        print(data)

        data_return = data
        return data_return

    # def __del__(self):
    #     pass


def main(addr_bind, addr_send):
    print("**********main**************")
    udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_server.bind(addr_bind)

    request = UDPRequestHandler()
    handle = request.handle

    while True:
        try:
            data, addr = udp_server.recvfrom(BUFF_SIZE)
            if not data:
                break
            print("get data from:", addr)

            data_send = handle(data)
            udp_server.sendto(data_send, addr_send)

        except Exception as err:
            print("This is error:", err)
            break


if __name__ == "__main__":
    addr_bind = ('192.168.31.36', 43012)
    addr_send = ('192.168.31.35', 43010)
    # addr_recv is addr_bind

    # addr_bind = ('', 43012)
    # addr_send = ('127.0.0.1', 43014)
    main(addr_bind, addr_send)
    print("**********over***************")
    os.system("pause")
