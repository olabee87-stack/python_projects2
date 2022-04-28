# Load in request
# Load in json
# Load in your url and open it with requests urlopen or with the requests library that you installed with pip

import requests
import json

url = 'http://jsonplaceholder.typicode.com/posts?_limit=5'

response = requests.get(url)
statuscode = response.status_code
data = response.text  # Will print out the format of the page
jsonData = response.json()

for j in jsonData:
    # print(len(j))
    print(j.get('title'))

print(response)
print(statuscode)
# print(data)
#print(jsonData)

