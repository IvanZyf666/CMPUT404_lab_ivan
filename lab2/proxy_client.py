#!/usr/bin/env python3

import socket, time
from multiprocessing import Process
from multiprocessing import Pool

#define address, buffer size

HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 1024

payload = "GET / HTTP/1.0\r\nHOST: www.google.com\r\n\r\n"

def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname( host )
    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()

    print (f'Ip address of {host} is {remote_ip}')
    return remote_ip

def connect(addr):
    #create socket, connect, and receive data


    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(addr)
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR) #shutdown() is different from close()

        full_data = s.recv(BUFFER_SIZE)
        print(full_data)
    
    except Exception as e:
        print(e)
    finally:
        s.close()

def main():
    connect((get_remote_ip(HOST),PORT))
    

if __name__ == "__main__":
    main()
    

