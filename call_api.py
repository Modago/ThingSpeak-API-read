# call_api.py

import pandas as pd

def call_api(w_type,n_data_pts):
    n_data_str = str(n_data_pts)
    if w_type == 'temperature':
        field_num = '4'
    elif w_type == 'pressure':
        field_num = '6'
    elif w_type == 'rainfall':
        field_num = '5'
    else: #humidity
        field_num = '3'
    # channel 12397
    # https://api.thingspeak.com/channels/707691/fields/1.json?results=2
    url = f'https://api.thingspeak.com/channels/12397/fields/{field_num}.csv?results={n_data_str}'
    df = pd.read_csv(url)

    return df