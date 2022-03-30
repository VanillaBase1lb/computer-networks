#!/usr/bin/python3

import pyftpdlib.authorizers
import pyftpdlib.handlers
import pyftpdlib.servers

server_directory = "." # start FTP server from this directory

auth = pyftpdlib.authorizers.DummyAuthorizer()
auth.add_anonymous(server_directory, perm="elradfmw")

handler = pyftpdlib.handlers.FTPHandler
handler.authorizer = auth

server = pyftpdlib.servers.FTPServer(("127.0.0.1", 8099), handler)
server.serve_forever()