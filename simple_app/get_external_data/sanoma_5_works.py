import requests
from datetime import datetime
from datetime import time
from date import dates



def get_arrival():
    for d in dates:
        url = f"""https://rata.digitraffic.fi/api/v1/trains/{d}/4"""
        response = requests.get(url)
        json_data = response.json()

        for j in json_data:
            for key in j['timeTableRows']:
                if key.get('type') != 'ARRIVAL' or key.get('actualTime') == None:
                    continue
                time_str = (key.get('actualTime').split('T')[1].split('.')[0])
                time_obj = datetime.strptime(time_str, '%H:%M:%S').time()
                #avg_arrival =
                print((time_obj))


get_arrival()
