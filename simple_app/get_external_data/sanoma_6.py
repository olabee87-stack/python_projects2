import requests
from datetime import datetime
import pandas as pd
from date import dates



def get_arrival():
    for d in dates:
        url = f"""https://rata.digitraffic.fi/api/v1/trains/{d}/4"""
        response = requests.get(url)
        json_data = response.json()

        for j in json_data:
            for key in j['timeTableRows']:
                if key.get('type') != 'ARRIVAL' or key.get('actualTime') is None:
                    continue
                my_list = []
                for t in (key.get('actualTime').split('T')[1].split('.')[0]):
                    print(t)
                    time_obj = datetime.strptime(t, '%H:%M:%S.%f').time()
                    return my_list.append(time_obj)












print(get_arrival())
