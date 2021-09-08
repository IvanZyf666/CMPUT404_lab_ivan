import requests

print("requests version:", requests.__version__)

r = requests.get('https://www.google.com/') # get google homepage 

print(r.text)
# what should I print?
