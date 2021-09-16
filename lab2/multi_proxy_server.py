#!/usr/bin/env python3
import socket, time, sys
from multiprocessing import Process

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

#get host information
def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname( host )
    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()

    print (f'Ip address of {host} is {remote_ip}')
    return remote_ip

#handle requests
def handleRequest(conn, addr, proxy_end):

    #get the client's request and send to google
    receivedClientData = conn.recv(BUFFER_SIZE)
    print(f"Sending received data {receivedClientData} to Google")
    proxy_end.sendall(receivedClientData)
    proxy_end.shutdown(socket.SHUT_WR)

    #get the response from google and return back to client
    returnData = proxy_end.recv(BUFFER_SIZE)
    print(f"Sending received data {returnData} to client")
    conn.send(returnData)

def main():
    
    #set host to www.google.com and port to 80
    host = 'www.google.com'
    port = 80

    #create socket, bind, and set to listening mode
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        #bind and set listening mode

        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        proxy_start.bind((HOST, PORT))
        proxy_start.listen(2)



        while True:
           
            conn, addr = proxy_start.accept()
            print("Connected by", addr)
            
            
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                

                print("Connecting to Google")
                remote_ip = get_remote_ip(host)

                #connect proxy_end
                proxy_end.connect((remote_ip, port))
                
                p = Process(target=handleRequest, args=(conn, addr, proxy_end))
                p.daemon = True
                p.start()
                print("Started process", p)
                

            
            conn.close()

if __name__ == "__main__":
    main()



