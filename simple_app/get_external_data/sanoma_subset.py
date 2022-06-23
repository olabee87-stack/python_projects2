import requests
from date import dates

def get_arrival():
    for d in dates:
        url = f"""https://rata.digitraffic.fi/api/v1/trains/{d}/4"""
        response = requests.get(url)
        json_data = response.json()

        for j in json_data:
            for key in j['timeTableRows']:
                if key.get('type') == 'ARRIVAL' :
                    print(key.get(len('actualTime')))
                    subset_a = key.get('actualTime'[5])
                    subset_b = key.get('actualTime'[11:19])
                    arrival_time = f"""{subset_a}"""
                    #print(arrival_time)



get_arrival()


