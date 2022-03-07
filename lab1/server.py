import socket

port_server = 4364

sock_server = socket.socket()
sock_server.bind(("", port_server))
sock_server.listen(1)

while True:
    sock_client, address_client = sock_server.accept()
    # print(sock_client, address_client)
    random_set = eval(sock_client.recv(1024).decode())
    final_set = []

    for element in random_set:
        if element not in final_set:
            final_set.append(element)

    sock_client.send(str(final_set).encode())

    sock_client.close()
