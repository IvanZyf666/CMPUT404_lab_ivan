1. github url: https://github.com/IvanZyf666
2. requests version on my system: 2.26.0
3. requests version in the virtualenv: 2.26.0
4. A virtual environment is a way to have multiple, parallel instances of the Python interpreter, each with different package sets and different configurations. Each virtual environment contains a discrete copy of the Python interpreter, including copies of its support utilities. The packages installed in each virtual environment are seen only in that virtual environment and no other. Even large, complex packages with platform-dependent binaries can be corralled off from each other in virtual environments.

5. StatusCode: 301, must visit the url with www: http://www.google.com/



6.
curl http://google.com/teapot 
result: status code: 301

curl -i http://google.com/teapot 
result: status code: 301 with HTTP/1.1

curl -iL http://google.com/teapot 
result: status code: 301 with HTTP/1.1
        status code: 418 with HTTP/2

curl -i http://www.google.com/teapot 
result: status code: 418 with HTTP/1.1

curl -iL http://www.google.com/teapot 
result: status code: 418 with HTTP/1.1
        
7.
tried:
curl -ik https://webdocs.cs.ualberta.ca/~hindle1/1.py
curl -ik -X POST -d "X=Y" https://webdocs.cs.ualberta.ca/~hindle1/1.py

difference:
the first one I got <DT> REQUEST_METHOD <DD> GET
the second one I got <DT> REQUEST_METHOD <DD> POST
The -X POST method is used to send a post request.
(if I don't use -X POST, it sends a get request)

8.
My raw URL: https://github.com/IvanZyf666/CMPUT404_lab_ivan/blob/main/script.py