#!/usr/bin/env python3
import socket
import time
from multiprocessing import Process

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def handleEcho(conn, addr):
    print("Connected by", addr)
            
    #receive data, then send it back
    full_data = conn.recv(BUFFER_SIZE)
    
    #back the request from client to client
    conn.sendall(full_data)
    conn.shutdown(socket.SHUT_WR)
    conn.close()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        #reuse the same bind port
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)
        
        #continuously listen for connections
        while True:
            #listens for incoming connections
            conn, addr = s.accept()

            #multiprocessing to handle multi echo
            p = Process(target=handleEcho, args=(conn, addr))
            p.daemon = True
            p.start()
            print("Started process", p)
            
        

if __name__ == "__main__":
    main()
