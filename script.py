import requests

print("requests version:", requests.__version__)

# get google homepage 
r = requests.get('https://www.google.com/') 

# let the script print out its own source from github
new_r = requests.get('https://raw.githubusercontent.com/IvanZyf666/CMPUT404_lab_ivan/main/script.py')

print(new_r.text)