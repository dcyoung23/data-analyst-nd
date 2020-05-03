from pandas import *
import pandasql
from ggplot import *

def plot_weather_data(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.  
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.  

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station
     * Which stations have more exits or entries at different times of day

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
     
    You can check out:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
     
    To see all the columns and data points included in the turnstile_weather 
    dataframe. 
     
    However, due to the limitation of our Amazon EC2 server, we are giving you about 1/3
    of the actual data in the turnstile_weather dataframe
    '''

    turnstile_weather['Dayofweek'] = pandas.DatetimeIndex(turnstile_weather['DATEn']).dayofweek
    temp = turnstile_weather.groupby('Dayofweek',as_index=False).sum()['ENTRIESn_hourly']
    d = {'Dayofweek' : temp.index, 'ENTRIESn_hourly' : temp.values}
    tw_s = pandas.DataFrame(d)
    
    plot = ggplot(tw_s, aes(x='Dayofweek', y = 'ENTRIESn_hourly')) + geom_bar(aes(x='Dayofweek', weight = 'ENTRIESn_hourly'))
    return plot


if __name__ == "__main__":
    image = "plot.png"

    #with open(image, "wb") as f:

    input_filename = "turnstile_data_master_with_weather.csv"
    df = pandas.read_csv(input_filename)
    gg =  plot_weather_data(df)
    ggsave(image, gg, width=11, height=8)
    #ggsave(f, gg)


