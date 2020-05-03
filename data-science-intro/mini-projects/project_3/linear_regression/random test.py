import numpy as np
import scipy
import scipy.stats
import pandas as pd
from random import sample

input_filename = "turnstile_data_master_with_weather.csv"
turnstile_weather = pd.read_csv(input_filename)
    
rain = turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain'] == 1]
no_rain = turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain'] == 0]

#rain_n = np.random.choice(rain.index.values, 2000)
#no_rain_n = np.random.choice(no_rain.index.values, 2000)

n = 2000
rain = sample(turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain'] == 1],n)
no_rain = sample(turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain'] == 0],n)

print scipy.stats.shapiro(rain)[0]
print scipy.stats.shapiro(no_rain)[0]
