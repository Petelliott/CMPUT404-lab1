import requests

#print(requests.__version__)

print(requests.get("https://raw.githubusercontent.com/Petelliott/CMPUT404-lab1/master/script.py").text)
