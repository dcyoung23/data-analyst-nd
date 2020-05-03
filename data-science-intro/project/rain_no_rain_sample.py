import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from random import sample

turnstile_weather = pd.read_csv("turnstile_weather_v2.csv")

n = 1000
no_rain = pd.DataFrame(sample(turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain'] == 0],n))
rain = pd.DataFrame(sample(turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain'] == 1],n))
    
print no_rain.describe()
print rain.describe()
