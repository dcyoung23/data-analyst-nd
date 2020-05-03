import numpy as np
import scipy
import scipy.stats
import pandas as pd

def mann_whitney_plus_means(turnstile_weather):

    rain = turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain'] == 1]
    no_rain = turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain'] == 0]

    with_rain_mean = rain.mean()
    with_rain_median = rain.median()
    without_rain_mean = no_rain.mean()
    without_rain_median = no_rain.median()
    
    U, p = scipy.stats.mannwhitneyu(rain, no_rain, use_continuity=True)

    two_tail_p = p * 2

    return with_rain_mean, with_rain_median, without_rain_mean, without_rain_median, U, p, two_tail_p

if __name__ == "__main__":
    input_filename = "turnstile_data_master_with_weather.csv"
    turnstile_master = pd.read_csv(input_filename)
    with_rain_mean, with_rain_median, without_rain_mean, without_rain_median, U, p, two_tail_p = mann_whitney_plus_means(turnstile_master)

    print "Two-Tail p-Value: {0}\nRainy Day Mean: {1}\nNon-Rainy Mean: {2}".format(two_tail_p, with_rain_mean, without_rain_mean)

    alpha = .05

    if two_tail_p < alpha:
        print 'Reject the null hypothesis'

    else:
        print 'Accept the null hypothesis'

