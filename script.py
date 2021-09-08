import requests

print("requests version:", requests.__version__)

r = requests.get('https://www.google.com/') # get google homepage 

print(r.text)

new_r = requests.get('https://raw.githubusercontent.com/IvanZyf666/CMPUT404_lab_ivan/main/script.py')

print(new_r.text)