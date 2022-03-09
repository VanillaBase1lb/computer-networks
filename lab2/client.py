from itertools import count
import socket
import random

port_client = 4364
sock_client = socket.socket()
sock_client.connect(("127.0.0.1", port_client))

random_count = random.randint(25, 100)
random_set = [random.randint(1, 100) for i in range(random_count)]
# print(random_set)

sock_client.send(str(random_set).encode())

final_set = eval(sock_client.recv(1024).decode())
duplicate_set = []

for element in final_set:
    if random_set.count(element) > 1:
        duplicate_set.append(element)

print("The original set of numbers randomly generated:")
print(random_set)
print()
print("The final set without any repeated numbers is:")
print(final_set)
print()
print("The set of repeated numbers is:")
print(duplicate_set)
sock_client.close()
