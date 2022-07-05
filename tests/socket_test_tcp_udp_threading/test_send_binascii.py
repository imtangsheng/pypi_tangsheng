import binascii
import numpy as np
from socket import socket, AF_INET, SOCK_STREAM
import os
import sys

# temp[0] = 'F';
# temp[1] = 'G';
# temp[2] = (char)((0xff00 & 4) >> 0);
# temp[3] = (char)((0xff & 4));
# gIntToByteArry(length, &temp[4]);
# temp[8 + length] = 0xF0;
# memcpy(temp + 8, weight.data(), length);
# send_data(temp, 9 + length);

class FgDataStyle:
    def __init__(self):
        self.bengin = b'FG\x00\x04'
        self.data_len = None
        self.data = None
        self.data_len_style = b'\x00\x00\x00\x00'
        self.data_style = None
        self.end = b'\x00\x00\x00\x00\xF0'
    def set_data(self,data):
        data_len = np.array(4*len(data)+4,dtype = '>u4')
        self.data_len_style = data_len.tobytes()
        self.data_style = data.tobytes()
    def send_data(self,fg_style_send):
        send_data = self.bengin+self.data_len_style+self.data_style+self.end
        fg_style_send(send_data)

    def get_data_from_style(self,fg_style_data):
        for i in range(0,len(fg_style_data)):
            if self.bengin[0] == fg_style_data[i]:
                if self.bengin[1] == fg_style_data[i+1]:
                    self.data_len = np.frombuffer(fg_style_data[(i+2):(i+6)],dtype ='int32')
                    self.data = np.frombuffer(fg_style_data[(i+7):(i+7+4*self.data)],dtype ='float32')
                    if self.end == fg_style_data[i+7+4*self.data+1]:
                        return True
                    else:
                        return False
        return False



if __name__ == "__main__":
import time
npy_path = r"D:\Project\UE4\Shirley\Human_shirly_V3\Content\sound_animation\tests\weight_test_data.npy"
npy_data = np.load(npy_path)
npy_data_f4 = npy_data.astype('<f4')
a.dtype
a.shape
npy_data.shape
npy_data.dtype

data_stype = FgDataStyle()

4*41
ltype = np.array(4*41,dtype = '>u4')
ltype.tobytes('C')
char_type = ltype.tobytes()
len(char_type)
char_type[0]

ltype.tobytes()
data = npy_data[235]
len(data)
data.dtype

ltype = np.array(0.1,dtype = '>f4')
ltype.dtype
ltype.tobytes()

st = data.tobytes()
len(st)
8*41
data_stype.set_data(data)

s_data = data_stype.bengin+data_stype.data_len_style+data_stype.data_style+data_stype.end
len(s_data)
s_data[0:8]
4*41+8
s_data[4*41 +8]
c.sendall(s_data)
s_data[7]
data = npy_data[40]
data = np.array(data,dtype = 'float32')
data.dtype

data_stype.set_data(data)
data_stype.send_data(c.send)

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 43015))
s.listen(3)
print("wait on connection")
c,a = s.accept()
print("go on connection")

data[0]
data[8]

data = npy_data_f4[100]
st = time.time()
data_stype.set_data(data)
time.time()-st
data_stype.send_data(c.sendall)


for i in range(0,300):
    data = npy_data_f4[i]
    data_stype.set_data(data)
    data_stype.send_data(c.sendall)
    time.sleep(0.033333)
# c.sendall(data_stype.bengin + data_stype.data_len_style+data_stype.data_style+data_stype.end)
print("over")
c.close()
os.system("pause")

n = '5'
print(n.zfill(3))
 
t = 'test'
print(t.rjust(10, '0'))
print(t.ljust(10, '0'))


import binascii
import numpy as np
from socket import socket, AF_INET, SOCK_STREAM
import os
import sys
from os.path import abspath, dirname, isfile, join

__file__ = r"D:\Project\UE4\Shirley\Human_shirly_V3\Content\sound_animation\tests\test.py"
sound_animation_path=dirname(dirname(abspath(__file__)))

lib_path =join(sound_animation_path, "lib")
sys.path.append(lib_path)


class FgDataStyle:
    def __init__(self):
        self.bengin = b'FG'
        self.data_len = None
        self.data = None
        self.data_len_style = b'\x00\x00\x00\x00'
        self.data_style = None
        self.end = b'\x00\x00\x00\x00\xF0'
    def set_data(self,data):
        data_len = np.array(len(data),dtype = 'int32')
        self.data_len_style = data_len.tobytes()
        self.data_style = data.tobytes()
    def send_data(self,fg_style_send):
        fg_style_send(self.bengin+self.data_len_style+self.data_style+self.end)

    def get_data_from_style(self,fg_style_data):
        for i in range(0,len(fg_style_data)):
            if self.bengin[0] == fg_style_data[i]:
                if self.bengin[1] == fg_style_data[i+1]:
                    self.data_len = np.frombuffer(fg_style_data[(i+2):(i+6)],dtype ='int32')
                    self.data = np.frombuffer(fg_style_data[(i+7):(i+7+4*self.data)],dtype ='float32')
                    if self.end == fg_style_data[i+7+4*self.data+1]:
                        return True
                    else:
                        return False
        return False


from tgshg.socket_ue4 import FgServerForPython as Fg


if __name__ == "__main__":
import time
npy_path = r"D:\Project\UE4\Shirley\Human_shirly_V3\Content\sound_animation\tests\weight_test_data.npy"
npy_data = np.load(npy_path)
npy_data_f4 = npy_data.astype('f4')
npy_data_f4[100]
data_stype = FgDataStyle()

fg.set_data(npy_data_f4[100])
fg.send_data(c.sendall)
    
    # s = socket(AF_INET, SOCK_STREAM)
    # s.bind(('', 43015))
    # s.listen(1)
    # print("wait on connection")

    # c,a = s.accept()
    
print("go on connection")
socket_Fg = Fg.FgServerForBP("FgSocket")
socket_Fg.Listen(43014)
socket_Fg.IsConnected()
while not socket_Fg.IsConnected():
    time.sleep(1)
    print("******等待客户端连接*******")

data = npy_data[300]
data[7]
for i in range(len(data)):
    data[i] = float(data[i])
the_weights = str(data).replace('[', '')
the_weights = the_weights.replace(']', '')
the_weights = the_weights.replace(' ', ',') + ",0"
socket_Fg.SendData(the_weights, 6)
time.sleep(0.033)

from socket import *
c = socket(AF_INET, SOCK_STREAM)
c.connect(('localhost', 43014))

data1 = c.recv(4096)
data1
import numpy as np
np.save("socket.npy",data1)

data1[0:8]
data1[4:8]

len(data1)

8+4*41
len(data)
a = data1[168:172]
b = data1[172:176]
b
len(a)
a
np.frombuffer(a,dtype ='float32')

data[40]
data1[176:177]

data1[172:177]

data1[0:1]

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 43015))
s.listen(1)
c,a = s.accept()

c.sendall(data1)

for j in range(0,300):
    data = npy_data[j]
    for i in range(len(data)):
        data[i] = float(data[i])
    the_weights = str(data).replace('[', '')
    the_weights = the_weights.replace(']', '')
    the_weights = the_weights.replace(' ', ',') + ",0"
    socket_Fg.SendData(the_weights, 6)
    time.sleep(0.033)
socket_Fg.Close()

    # for i in range(1000,1600):
    #     data = npy_data[i]
    #     data_stype.set_data(data)
    #     data_stype.send_data(c.send)
        
    #     time.sleep(0.033)
    # c.sendall(data_stype.bengin + data_stype.data_len_style+data_stype.data_style+data_stype.end)
    print("over")
    os.system("pause")
    # c.close()