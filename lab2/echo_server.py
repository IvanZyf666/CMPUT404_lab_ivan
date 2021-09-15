#!/usr/bin/env python3
import socket
import time

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)
        
        #continuously listen for connections
        """
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            
            #recieve data, wait a bit, then send it back
            full_data = conn.recv(BUFFER_SIZE)
            time.sleep(0.5)
            conn.sendall(full_data)
            conn.close()
        """
        while True:
            #TODO Q4: accept incoming connections from proxy_start, print info about connection
            conn, addr = s.accept()
            print("Connected by", addr)
            
            
            
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:


                #establish "end" of proxy (connect)
                # now for the multiprocessing...

                # TODO: think get remote IP from google
                

                print("Connecting to Google")
                remote_ip = get_remote_ip(host)

                #connect proxy_end
                proxy_end.connect((remote_ip, port))

                #send data
                send_full_data = conn.recv(BUFFER_SIZE)
                print(f"Sending received data {send_full_data} to google")
                proxy_end.sendall(send_full_data)

                #shut down at the end
                proxy_end.shutdown(socket.SHUT_WR)

                data = proxy_end.recv(BUFFER_SIZE)
                print(f"Sending received data {data} to client")

                #send data back
                conn.send(data)
            
            conn.close()

if __name__ == "__main__":
    main()
