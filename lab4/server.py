#!/usr/bin/python3

import pyftpdlib.authorizers
import pyftpdlib.handlers
import pyftpdlib.servers

auth = pyftpdlib.authorizers.DummyAuthorizer()
auth.add_anonymous("/mnt/storage", perm="elradfmw")
auth.add_user("yuvraj", "password", "/mnt/storage", perm="elradfmw")

handler = pyftpdlib.handlers.FTPHandler
handler.authorizer = auth

server = pyftpdlib.servers.FTPServer(("127.0.0.1", 8099), handler)
server.serve_forever()