#!/usr/bin/python3

import pickle
import socket
import time
      
sock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_client.connect(("127.0.0.1", 9889))

matrix_original = [[0, 1, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1], [0, 0, 0, 0]]
row_parse = []
column_parse = []

for row in matrix_original:
    count = 0
    for bit in row:
        if bit == 1:
            count = count + 1
    if count % 2 == 0:
        column_parse.append(0)
    else:
        column_parse.append(1)

for i in range(len(matrix_original)):
    count = 0
    for j in range(len(matrix_original)):
        if matrix_original[j][i] == 1:
            count = count + 1
    if count % 2 == 0:
        row_parse.append(0)
    else:
        row_parse.append(1)

matrix_modified = [[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 0, 0]]

data1 = pickle.dumps(matrix_modified)
sock_client.send(data1)
time.sleep(1)

data2 = pickle.dumps(row_parse)
sock_client.send(data2)
time.sleep(1)

data3 = pickle.dumps(column_parse)
sock_client.send(data3)
time.sleep(1)

matrix = pickle.loads(sock_client.recv(1024))
print("The recovered matrix is:")
print(matrix)

sock_client.close() 