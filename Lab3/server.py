import pickle
import socket

client_count = 1
sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_server.bind(("",4364))
sock_server.listen(client_count)
print("Started listening for %i clients" % client_count)
sock_client,address_client = sock_server.accept()
print("Connection accepted from client")

matrix_received = pickle.loads(sock_client.recv(1024))
print("The received matrix is:")
print(matrix_received)

row_parity_original = pickle.loads(sock_client.recv(1024))
print("Row parity bits:")
print(row_parity_original)

column_parity_original = pickle.loads(sock_client.recv(1024))
print("Column parity bits:")
print(column_parity_original)

row_parity_calculated = []
col_parity_calculated = []

for i in range(len(matrix_received)):
    count = 0
    for j in range(len(matrix_received[i])):
        if(matrix_received[i][j] == 1):
            count = count + 1

    if(count % 2 != 0):
        row_parity_calculated.append(0)
    else:
        row_parity_calculated.append(1)

for i in range(len(matrix_received)):
    count = 0
    for j in range(len(matrix_received[i])):
        if(matrix_received[j][i] == 1):
            count = count + 1

    if(count % 2 != 0):
        col_parity_calculated.append(0)
    else:
        col_parity_calculated.append(1)   

row_error = 0
col_error = 0
l = 0
m = 0
for k in range(len(row_parity_calculated)):
    if(row_parity_calculated[l] != row_parity_original[l]):
       row_error = l
    l = l + 1   
for k in range(len(col_parity_calculated)):
    if(col_parity_calculated[m] != column_parity_original[m]):
       col_error = m
    m = m + 1

corrected_matrix = matrix_received
if(corrected_matrix[row_error][col_error] == 1):
    corrected_matrix[row_error][col_error] = 0
else:
    corrected_matrix[row_error][col_error] = 1

print("Corrected matrix:")
print(corrected_matrix)

matrix = pickle.dumps(corrected_matrix)
sock_client.send(matrix)

sock_client.close()