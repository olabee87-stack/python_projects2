import requests
url = 'https://www.tokmanni.fi/poytakynttila-bolsius-13-x-6-8-cm-rustic-jade-v-8717847154668'

response = requests.get(url)
data = response

jsonData = data.json()

for j in jsonData:
    print(j.get('price'))