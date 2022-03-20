#!/usr/bin/python3

import pickle
import socket
import time
      
sock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_client.connect(("127.0.0.1", 9889))

original_string = "Hello I am under the water"
modified_string = "Hello I am undes the water"
original_string_ascii = []
modified_string_ascii = []
original_string_ascii_binary = []
modified_string_ascii_binary = []

for character in original_string:
    original_string_ascii.append(ord(character))
# print(original_string_ascii)
for ascii_code in original_string_ascii:
    binary_ascii_code = [int(x) for x in list('{0:0b}'.format(ascii_code))]
    for i in range(len(binary_ascii_code), 8):
        binary_ascii_code.insert(0, 0)
    original_string_ascii_binary.append(binary_ascii_code)
# print(original_string_ascii_binary)

for character in modified_string:
    modified_string_ascii.append(ord(character))
# print(modified_string_ascii)
for ascii_code in modified_string_ascii:
    binary_ascii_code = [int(x) for x in list('{0:0b}'.format(ascii_code))]
    for i in range(len(binary_ascii_code), 8):
        binary_ascii_code.insert(0, 0)
    modified_string_ascii_binary.append(binary_ascii_code)
# print(modified_string_ascii_binary)

matrix_original = original_string_ascii_binary
# matrix_original = [[0, 1, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]]
# matrix_original = [[0, 1, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1], [0, 0, 0, 0]]
row_parse = []
column_parse = []

for i in range(len(matrix_original)):
    count = 0
    for j in range(len(matrix_original[i])):
        if(matrix_original[i][j] == 1):
            count = count + 1

    if(count % 2 == 0):
        row_parse.append(0)
    else:
        row_parse.append(1)

for i in range(len(matrix_original[0])):
    count = 0
    for j in range(len(matrix_original)):
        if matrix_original[j][i] == 1:
            count = count + 1
    if count % 2 == 0:
        column_parse.append(0)
    else:
        column_parse.append(1)

matrix_modified = modified_string_ascii_binary
# matrix_modified = [[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]]
# matrix_modified = [[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 0, 0]]

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
# print("The recovered matrix is:")
# print(matrix)

ascii_string = []
for binary_ascii_code in matrix:
    ascii_code = int("".join(str(x) for x in binary_ascii_code), 2)
    ascii_string.append(ascii_code)
# print(ascii_matrix)

recovered_string = ""
for ascii_code in ascii_string:
    # recovered_string.append(chr(ascii_code))
    recovered_string = recovered_string + chr(ascii_code)

print("The recovered string is:")
print(recovered_string)

sock_client.close() 