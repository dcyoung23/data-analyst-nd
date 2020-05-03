import numpy as np
import scipy
import scipy.stats
import pandas as pd


def mann_whitney_plus_means(turnstile_weather):
    '''
    This function will consume the turnstile_weather dataframe containing our final turnstile-Subway data. This 
    function should return the mean number of entries with rain, the mean number of entries without rain, and the
    Mann-Whitney U statistic and p-value.  You should feel free to use scipy's Mann-Whitney implementation, and also
    might find it useful to use numpy's mean function.  Here's some documentation on that:

    http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
    '''

    rain = turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain'] == 1]
    no_rain = turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain'] == 0]

    with_rain_mean = rain.mean()
    with_rain_median = rain.median()
    without_rain_mean = no_rain.mean()
    without_rain_median = no_rain.median()
    
    U, p = scipy.stats.mannwhitneyu(rain, no_rain, use_continuity=True)

    two_tail_p = round(p * 2,4)
    #rain_n = np.random.choice(rain.index.values, 2000)
    #print scipy.stats.shapiro(rain_n)[1]
    #print scipy.stats.shapiro(no_rain)[1]

    return with_rain_mean, with_rain_median, without_rain_mean, without_rain_median, U, p, two_tail_p

if __name__ == "__main__":
    input_filename = "turnstile_data_master_with_weather.csv"
    turnstile_master = pd.read_csv(input_filename)
    student_output = mann_whitney_plus_means(turnstile_master)

    print student_output

    


