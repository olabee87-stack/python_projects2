import requests
import pandas as pd
import numpy as py
from date import dates

def norm_data():
    train_number = 4
    for d in dates:
        url = f"""https://rata.digitraffic.fi/api/v1/trains/{d}/{train_number}"""
        response = requests.get(url)
        json_data = response.json()

        df = pd.read_json(json_data)
        print(df.head())



norm_data()
