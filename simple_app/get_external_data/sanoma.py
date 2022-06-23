import requests
from date import dates

def get_arrival():
    for d in dates:
        url = f"""https://rata.digitraffic.fi/api/v1/trains/{d}/4"""
        response = requests.get(url)
        json_data = response.json()

        for j in json_data:
            for key in j['timeTableRows']:
                if key.get('type') == 'ARRIVAL' and key.get('actualTime') != None:
                    print(key.get(len('actualTime')))




get_arrival()

