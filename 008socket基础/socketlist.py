#!/usr/bin/env python
# -*- coding:utf-8 -*-

# import socket
import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            conn = self.request.recv(1024)
            self.request.send(b'Hi')
            print(conn)


server = socketserver.ThreadingTCPServer(('127.0.0.1', 8001), MyServer)
server.serve_forever()
