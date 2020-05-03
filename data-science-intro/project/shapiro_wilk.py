import numpy as np
import pandas as pd
from scipy import stats
from random import sample

def shapiro_wilk(turnstile_weather, rain):

    # random sample from data to avoid p-value warning
    #n = 1000
    #data = sample(turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain'] == rain],n)

    data = turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain'] == rain]

    W, p = stats.shapiro(data)

    return W, p

if __name__ == "__main__":
    input_filename = "turnstile_weather_v2.csv"
    turnstile_master = pd.read_csv(input_filename)

    # input to change between rain 1 and no rain 0
    rain_input = 1
    W, p = shapiro_wilk(turnstile_master, rain_input)

    print "Shapiro-Wilk Test Statistic: {0}\np-Value: {1}".format(W, p)
