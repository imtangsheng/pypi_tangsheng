# -*- coding: utf-8 -*-
"""
    sound_animation/lib.test_landmark2weights_88points_67weigths
    ~~~~~



    :copyright:facegood © 2019 by the tang.

"""
import os
import sys

import time
import socket
BUFF_SIZE = 4096  # 4 KiB


def main(addr_bind, addr_send):
    print("**********main**************")
    udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_server.bind(addr_bind)

    while True:
        try:
            t1 = time.time()
            data, addr = udp_server.recvfrom(BUFF_SIZE)
            if not data:
                break
            print("get data from:", addr)
            print("t1 get time is:", time.time()-t1)
            print(data)

            t6 = time.time()
            udp_server.sendto(data, addr_send)
            print("t6 get time is:", time.time()-t6)

            # t2 = time.time()
            # flag, points_data = get_points_from_binascii(data)
            # print("t2 get time is:", time.time()-t2)
            # if flag:
            #     t3 = time.time()
            #     points_data = points_data_mean(points_data)
            #     print("t3 get time is:", time.time()-t3)

            #     t4 = time.time()
            #     weights_data = get_weights(points_data)
            #     print("t4 get time is:", time.time()-t4)

            #     t5 = time.time()
            #     data_send = get_send_data(weights_data)
            #     print("t5 get time is:", time.time()-t5)

            #     t6 = time.time()
            #     udp_server.sendto(data_send, addr_send)
            #     print("t6 get time is:", time.time()-t6)

        except Exception as err:
            print("This is error:", err)
            break


if __name__ == '__main__':
    print(sys.version)
    addr_bind = ('', 43020)
    addr_send = ('127.0.0.1', 43021)
    # addr_recv is addr_bind

    # addr_bind = ('', 43012)
    # addr_send = ('127.0.0.1', 43014)
    main(addr_bind, addr_send)

    print('********over***********')
    os.system("pause")
