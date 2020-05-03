import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def entries_histogram(turnstile_weather):

    plt.figure()
    plt.title('Histogram of Hourly Turnstile Entries for Rain vs. No Rain')
    plt.ylabel('Frequency')
    plt.xlabel('Hourly Turnstile Entries')
    plt.xlim(0, 6000)
    no_rain = turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain'] == 0]
    rain = turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain'] == 1]
    no_rain.hist(color='b', label='No Rain',bins=200) # your code here to plot a historgram for hourly entries when it is not raining
    rain.hist(color='g', label='Rain', alpha=.75,bins=200) # your code here to plot a historgram for hourly entries when it is raining
    plt.legend()    
    return plt


if __name__ == "__main__":
    image = "plot_rain.png"
    turnstile_weather = pd.read_csv("turnstile_data_master_with_weather.csv")
    plt = entries_histogram(turnstile_weather)
    plt.savefig(image)
    #plt.show()


