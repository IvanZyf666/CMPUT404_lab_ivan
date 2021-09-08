1. github url: https://github.com/IvanZyf666
2. requests version: 2.26.0
3. virtualenv version: 20.7.2
4. A virtual environment is a way to have multiple, parallel instances of the Python interpreter, each with different package sets and different configurations. Each virtual environment contains a discrete copy of the Python interpreter, including copies of its support utilities. The packages installed in each virtual environment are seen only in that virtual environment and no other. Even large, complex packages with platform-dependent binaries can be corralled off from each other in virtual environments.

5. StatusCode: 301, must visit the url with www: http://www.google.com/



6.
Status code: 301 with curl http://google.com/teapot 
Status code: 418 with curl http://www.google.com/teapot 
both curl -i and curl -iL
```
HTTP/2 418
content-type: text/html; charset=ISO-8859-1
date: Mon, 06 Sep 2021 22:28:11 GMT
server: gws
cache-control: private
x-xss-protection: 0
x-frame-options: SAMEORIGIN
alt-svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-T051=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"
accept-ranges: none
vary: Accept-Encoding

<!doctype html><html lang="en"> <script nonce="xZ7R/0Uf69CAD7dxPp/TWw==">(function(H){H.className=H.className.replace(/\bgoogle\b/,'google-js')})(document.documentElement)</script> <meta charset="utf-8"> <meta content="initial-scale=1, minimum-scale=1, width=device-width" name="viewport"> <title>Error 418 (I&#8217;m a teapot)!?</title> <link href="//www.gstatic.com/teapot/teapot.min.css" rel="stylesheet" nonce="xZ7R/0Uf69CAD7dxPp/TWw=="> <a href="https://www.google.com/"><span aria-label="Google" id="logo"></span></a> <p><b>418.</b> <ins>I&#8217;m a teapot.</ins></p> <p>The requested entity body is short and stout. <ins>Tip me over and pour me out.</ins></p> <div id="teaset"><div id="teabot"></div><div id="teacup"></div></div> <script src="//www.gstatic.com/teapot/teapot.min.js" nonce="xZ7R/0Uf69CAD7dxPp/TWw=="></script> </html>
```

7.
curl -ik https://webdocs.cs.ualberta.ca/~hindle1/1.py
curl -ik -X POST -d "X=Y" https://webdocs.cs.ualberta.ca/~hindle1/1.py

Question:

Q5. what url must you visit? not google.com? http://www.google.com, add www but Idk why
got 301 if curl -i http://google.com 
got 200 if curl -i http://www.google.com
on terminal/ssh lab machine
but looks both 200 on my vscode terminal



under Q6, get google homepage

Modify your Python script so that it downloads itself from GitHub and prints out its own source code from GitHub. ???
