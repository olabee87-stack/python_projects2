# Task 2

import requests
import pandas as pd
import json


def print_arrival():
    dates = ['2022-03-01', '2022-03-23']
    # dates_df = pd.DataFrame()

    for i in dates:
        url = f"""https://rata.digitraffic.fi/api/v1/trains/{i}/4"""
        response = requests.get(url)
        json_data = response.json()

        for j in json_data:
            for key in j['timeTableRows']:
                print(key.get('actualTime'))
                print('***************************')
                # print(key.get('type'))


print_arrival()

url_ish = 'https://rata.digitraffic.fi/api/v1/trains/?=2022-03-01&=2022-03-31/3'


