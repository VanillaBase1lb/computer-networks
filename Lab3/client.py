#Client side
import socket
import random
import pickle
import time
      
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",4364))

#generate N*N matrix N=4
mat=[]
mat=[[1,0,1,1],[1,0,1,1],[1,1,0,0],[1,1,1,1]]

# row parsing list
row_parse=[]
row_parse=[0, 0, 1, 1]

#column parsing list
col_parse=[]
col_parse=[1, 1, 0, 0]

#modified mat with error is
modified_mat=[[1,0,1,1],[1,1,1,1],[1,1,0,0],[1,1,1,1]]

#sending the modified matrix
# data1=str(modified_mat)
# data1=data1.encode()
data1=pickle.dumps(modified_mat)
s.send(data1)

#adding 1 sec time for correct execution
time.sleep(1)

#sending the row parsing list
# data2=str(row_parse)
# data2=data2.encode()
data2=pickle.dumps(row_parse)
s.send(data2)

#adding 1 sec time for correct execution
time.sleep(1)

#sending the column parsing list
# data3=str(col_parse)
# data3=data3.encode()
data3=pickle.dumps(col_parse)
s.send(data3)

matrix=pickle.loads(s.recv(1024))
print("The recovered matrix is:")
print(matrix)



s.close() 