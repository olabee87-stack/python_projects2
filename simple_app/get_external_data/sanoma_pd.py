import requests
import pandas as pd
import numpy as np
from date import dates

def get_Arrival_avg():
    for d in dates:
        url = f"""https://rata.digitraffic.fi/api/v1/trains/{d}/4"""
        response = requests.get(url)
        json_data = response.json()

        for j in json_data:
            for key in j['timeTableRows']:
                print(key.get('actualTime'))


get_Arrival_avg()



