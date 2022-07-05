from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 25000))
s.listen(1)
c,a = s.accept()



from socket import *
c = socket(AF_INET, SOCK_STREAM)
c.connect(('localhost', 43014))

data1 = c.recv(4096)
print(len(data1))




# Server
import numpy
a = numpy.arange(0.0, 50000000.0)
send_from(a, c)

   
# Client
import numpy
a = numpy.zeros(shape=50000000, dtype=float)
a[0:10]
array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.])
recv_into(a, c)
a[0:10]
array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.])

