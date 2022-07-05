#!/usr/bin/env python36
# -*- coding: utf-8 -*-
"""
    tensorflow.weights_animation.py
    ~~~~~~~~~~~~~
    Defines api by tensorflow 

    :copyright: © 2019 by the facegood team.
    :license: BSD, see LICENSE for more details.
"""
import os
import numpy as np
import tensorflow as tf
from tensorflow.python.platform import gfile

curret_pb_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'package/weights_animation.pb')

class WeightsAnimation:
    def __init__(self, pb_path=curret_pb_path):
        self.sess = tf.Session()
        with gfile.FastGFile(pb_path, 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            self.sess.graph.as_default()
            tf.import_graph_def(graph_def, name='')
        self.sess.run(tf.global_variables_initializer())

        self.initdata()

    def initdata(self):
        self.input_x = self.sess.graph.get_tensor_by_name('Placeholder_1:0')
        self.out = self.sess.graph.get_tensor_by_name('dense_2/BiasAdd:0')
        self.is_training = self.sess.graph.get_tensor_by_name('Placeholder_3:0')
        

    def func_mean(self,data):
        # data = np.load('0428_002_ReVertex_87_train_input[1-19200].npy')
        data_x = data[:,[x for x in range(0,data.shape[1],2)]]
        data_y = data[:,[x for x in range(1,data.shape[1],2)]]
        mean_x = np.mean(data_x)
        mean_y = np.mean(data_y)
        sigma_x = np.std(data_x) #X的标准差
        sigma_y = np.std(data_y) #Y的标准差
        data[:,[x for x in range(0,data.shape[1],2)]] = (data[:,[x for x in range(0,data.shape[1],2)]] - mean_x)/sigma_x
        data[:,[x for x in range(1,data.shape[1],2)]] = (data[:,[x for x in range(1,data.shape[1],2)]] - mean_y)/sigma_y
        return data

    def get_weights(self, input_data):
        data = self.func_mean(input_data)
        vertex_relative = self.sess.run(self.out, feed_dict={self.input_x:data, self.is_training: False})
        return vertex_relative


pb_path = r"D:\Project\UE4\Shirley\Human_shirly_V3\Content\sound_animation\lib\tgshg\tensorflow\package\weights_animation.pb"
pb_WeightsAnimation = WeightsAnimation(pb_path)
get_weights = pb_WeightsAnimation.get_weights

from socket import socket, AF_INET, SOCK_STREAM
s_streamer = socket(AF_INET, SOCK_STREAM)
s_streamer.connect(('192.168.31.35', 43012))

class ClientStreamer:
    def __init__(self,addr,port):
        self.addr = addr
        self.port = port
        self.client = socket(AF_INET,SOCK_STREAM)
        self.client.connect((addr,port))
    
    def recv_data(self):
        output_data=self.client.recv(8192)
        return output_data


def get_data(inputdata):
    print(inputdata)
    outputdata = b"1234567890"
    return outputdata

from socketserver import BaseRequestHandler, TCPServer
def send_from(arr, dest):
    view = memoryview(arr).cast('B')
    while len(view):
        nsent = dest.send(view)
        view = view[nsent:]

def recv_into(arr, source):
    view = memoryview(arr).cast('B')
    while len(view):
        nrecv = source.recv_into(view)
        view = view[nrecv:]

class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        while True:
            msg = self.request.recv(8192)
            if not msg:
                break
            output_data = get_data(msg)
            self.request.send(output_data)

if __name__ == '__main__':
    print('***********************')
    print('Can connection from 2000')
    serv = TCPServer(('', 20000), EchoHandler)
    serv.serve_forever()
    print('********over***********')

