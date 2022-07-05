# -*- coding: utf-8 -*-
"""
    sound_animation/scripts.run_audio_tensorflow
    ~~~~~


    :copyright:facegood © 2019 by the tang.

"""
import os
import sys
print(sys.version)
from os.path import abspath, dirname, isfile, join

sound_animation_path=dirname(dirname(abspath(__file__)))
bin_path =join(sound_animation_path, "bin")
doc_path =join(sound_animation_path, "doc")
examples_path =join(sound_animation_path, "examples")
lib_path =join(sound_animation_path, "lib")
resource_path =join(sound_animation_path, "resource")
scripts_path =join(sound_animation_path, "scripts")
src_path =join(sound_animation_path, "src")
tests_path =join(sound_animation_path, "tests")

caption_path = join(resource_path, "caption")
caption_path_answer = join(caption_path,"answer")
caption_path_question = join(caption_path,"question")
question_path = join(caption_path,"question")
answer_path = join(caption_path,"answer")

mp3_path = join(resource_path,"mp3")
mp3_path_ai_speak = join(mp3_path,"ai_speak")
ai_speak_mp3_path = join(mp3_path,"ai_speak")

package_path = join(resource_path,"package")

wav_path = join(resource_path,"wav")
wav_path_ai_speak = join(wav_path,"ai_speak")
ai_speak_wav_path = join(wav_path,"ai_speak")

sys.path.append(lib_path)


import time
from functools import wraps
import threading
import queue
import multiprocessing
from multiprocessing import Process, Queue


from tgshg.tensorflow.get_wav_data import WavProcess
from tgshg.tensorflow.input_wav_output_lpc import c_lpc
from tgshg.tensorflow.input_lpc_output_predict_by_pb import Predict
from tgshg.tensorflow.input_predict_output_weights import weight_compute

predict = Predict()
lpc_predict = predict.predict


def worker(q_input,q_output,i):
    #  do something
    while 1:
        input_data = q_input.get()
        for output_wav in input_data:
            lpc_s = time.time()
            output_lpc = c_lpc(output_wav)
            lpc_e = time.time()
            p_s = time.time()
            output_predict = lpc_predict(output_lpc)
            p_e = time.time()
            w_s = time.time()
            output_data = weight_compute(output_predict)
            w_e = time.time()  
            print("***************test****:",i)
            print("**********lpc:",lpc_e-lpc_s)
            print("**********predict:",p_e-p_s)
            print("**********weight:",w_e-w_s)
            q_output.put(output_data)

play_wav_path = join(wav_path,"play")
flag_ok_begin_send_socket_data = join(play_wav_path,'ok.log')
def play_wav_file(flag=False):
    if not flag:
        if os.path.exists(flag_ok_begin_send_socket_data):
            os.remove(flag_ok_begin_send_socket_data)
    else:
        if not os.path.isfile(flag_ok_begin_send_socket_data):
            with open(flag_ok_begin_send_socket_data,"w+") as f:
                f.write('1')


class SoundAnimation:
    def __init__(self , cpus ,input_nums):
        if cpus == None:
            cpus = multiprocessing.cpu_count()
        self.cpus = cpus
        self.input_nums = input_nums
        self.init_multiprocessing()

    def init_multiprocessing(self):
        self.q_input = [Queue() for i in range(0, self.cpus)]
        self.q_output = [Queue() for i in range(0, self.cpus)]
        self.process = []
        for i in range(0, self.cpus):
            self.process.append(Process(target=worker,args=(self.q_input[i], self.q_output[i], i)))
    def start_multiprocessing(self):
        for i in range(0, self.cpus):
            self.process[i].start()
    def stop_multiprocessing(self):
        for i in range(0, self.cpus):
            self.process[i].terminate()

    def get_input_date(self,input_date):
        input_data_nums = [
            input_date[i:i+self.input_nums]
            for i in range(0,len(input_date), self.input_nums)
        ]
        
        self.flag_nums = len(input_data_nums)
        for i in range(0, self.cpus):
            self.q_input[i].put(input_data_nums[i::self.cpus])
    
    def get_output_data(self,q_output_data):
        num = 0
        flag_end = True
        while flag_end:
            for i in range(0,self.cpus):
                num+=1
                for data in self.q_output[i].get():
                    q_output_data.put(data)
                if num == self.flag_nums:
                    flag_end = False
                    break
                elif num == 1:
                    play_wav_file(flag=True)

from tgshg.socket_ue4 import FgServerForPython as Fg


class SocketReatime:
    def __init__(self,socket_Fg,fps):
        self.socket_Fg = socket_Fg
        self.one_fps = float(1.0 / fps)  # One frame per second
        self.q_socket = queue.Queue()

    def socket_output_data(self):
        self.send_index = 0
        def send_data():
            self.send_index += 1
            # print("index:",self.send_index)
            if not self.q_socket.empty():
                data = self.q_socket.get()
                # print(data)
                # play_wav_file(flag=True)
                for i in range(len(data)):
                    data[i] = float(data[i])
                the_weights = str(data).replace('[', '')
                the_weights = the_weights.replace(']', '')
                the_weights = the_weights.replace(' ', ',') + ",0"
                self.socket_Fg.SendData(the_weights, 6)
            else:
                pass
                print("Empty")
                play_wav_file(flag=False)

        while self.thread_is_alive:
            time.sleep(self.one_fps)
            send_data()
    def socket_send_start(self):
        self.thread_is_alive =True
        self.thread = threading.Thread(None,target = self.socket_output_data)
        self.thread.start()

    def socket_send_stop(self):
        self.thread_is_alive = False


def get_files_names(path_dir, f_extension='.wav'):
    f_list = os.listdir(path_dir)
    return [
        os.path.splitext(i)[0] for i in f_list
        if os.path.splitext(i)[1] == f_extension
    ]

next_wav_index = len(get_files_names(ai_speak_wav_path,'.wav'))

def has_new_wav():
    global next_wav_index
    wav_index = len(get_files_names(ai_speak_wav_path,'.wav'))

    if wav_index == next_wav_index:
        return False
    elif wav_index == (next_wav_index+1):
        next_wav_index +=1
        return os.path.join(ai_speak_wav_path ,str(wav_index) +".wav")
    elif wav_index == 0:
        next_wav_index = 0
        return False
    else:
        return False

import socket
def is_use(port=43013):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(('127.0.0.1', int(port)))
        s.shutdown(2)  # shutdown参数表示后续可否读写
        return True
    except Exception as e:
        # print(port, 'not used')
        return False


if __name__ == "__main__":
    print(sys.version)
    # s = time.time()
    socket_Fg = Fg.FgServerForBP("FgSocket")
    # s.listen(0)  # 等待客户端连接
    socket_Fg.Listen(43013)
    while not socket_Fg.IsConnected():
        time.sleep(1)
        print("******等待客户端连接*******")

    while True:
        print("******等待语音数据*******")
        time.sleep(1)


    socket_Fg.Close()

# 22%
