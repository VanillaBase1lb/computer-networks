import socket
import pickle
import time
      
sock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_client.connect(("127.0.0.1", 4364))

mat = []
mat = [[1, 0, 1, 1], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 1, 1]]

row_parse = [0, 0, 1, 1]

col_parse = [1, 1, 0, 0]

modified_mat = [[1, 0, 1, 1], [1, 1, 1, 1], [1, 1, 0, 0], [1, 1, 1, 1]]

data1 = pickle.dumps(modified_mat)
sock_client.send(data1)
time.sleep(1)

data2 = pickle.dumps(row_parse)
sock_client.send(data2)
time.sleep(1)

data3 = pickle.dumps(col_parse)
sock_client.send(data3)
time.sleep(1)

matrix = pickle.loads(sock_client.recv(1024))
print("The recovered matrix is:")
print(matrix)

sock_client.close() 