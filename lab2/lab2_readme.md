Q1:
import the socket module and run the line below to create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Q2:
ServerSocket is created to bind to a port and listen for a connect from a client. So, a server just waits for a conversation and doesn't start one.
ClientSocket is created to connect to a listen ing server. The client initiates the connection.

Q3:
reuse the same bind port by running the code below
proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

Q4:
accept incoming connections by the code below
conn, addr = proxy_start.accept()
print("Connected by", addr)

Info I got:
Connected by ('127.0.0.1', 54155)
The second value "54155" may vary each time I run

Q5:

After the server sends www.google.com the request, the following data is returned by recv()

HTTP/1.0 200 OK\r\nDate: Wed, 15 Sep 2021 02:31:30 GMT\r\nExpires: -1\r\nCache-Control: private, max-age=0\r\nContent-Type: text/html; charset=ISO-8859-1\r\nP3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."\r\nServer: gws\r\nX-XSS-Protection: 0\r\nX-Frame-Options: SAMEORIGIN\r\nSet-Cookie: 1P_JAR=2021-09-15-02; expires=Fri, 15-Oct-2021 02:31:31 GMT; path=/; domain=.google.com; Secure\r\nSet-Cookie: NID=223=ZFtxKpoU6LqXXoqbcJe6g1fPRwCF1Lg5it_OQ7wsQCrdPB15DTEovX9EjiXt1Ezy7HZBNn47lmJmc0MdyA5M0r9mkmNtgLDhuEFx4yvwhDdS_hpSiOjesGJ5BJeMX7mSJTqZ2t8Jz-Rf_Sk7B_TTqcZMJoXT3z1r7s95w14pSZc; expires=Thu, 17-Mar-2022 02:31:30 GMT; path=/; domain=.google.com; HttpOnly\r\nAccept-Ranges: none\r\nVary: Accept-Encoding\r\n\r\n<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en-CA"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script nonce="Qr1xdT7M2pSIjba2hWmbcw==">(functi'

Q6:
https://github.com/IvanZyf666/CMPUT404_lab_ivan/blob/main/lab2/proxy_client.py
https://github.com/IvanZyf666/CMPUT404_lab_ivan/blob/main/lab2/proxy_server.py
https://github.com/IvanZyf666/CMPUT404_lab_ivan/blob/main/lab2/echo_server.py


