# plot data.py

import numpy as np
import matplotlib.pyplot as plt

def plot_data(data,w_type):
    plt.plot(data)
    plt.xlabel('Data Point Number')
    plt.ylabel(w_type)
    plt.title(f'Plot of {} from ThingSpeak.com')
    plt.show()
