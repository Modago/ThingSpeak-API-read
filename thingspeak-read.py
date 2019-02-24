# thingspeak-read.py

# use Python to read a set of datapoints off of ThingSpeak.com and
# then plot the data with matplotlib.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


from user_input import user_input
from call_api import call_api
from clean_data import clean_data
from plot_data import plot_data

w_type, n_data_pts = user_input()
df = call_api(w_type,n_data_pts)
data = clean_data(df)
plot_data(data,w_type)
