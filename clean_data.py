# clean_data.py

import pandas as pd
import numpy as np

def clean_data(df):
    data_col = df.iloc[:,2]
    data = np.array(data_col)

    return data