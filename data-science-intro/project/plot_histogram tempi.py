import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def entries_histogram(turnstile_weather):

    plt.figure()
    plt.title('Histogram of Hourly Turnstile Entries by Temperature')
    plt.ylabel('Frequency')
    plt.xlabel('Temperature')
    plt.xlim(40, 100)
    plt.ylim(0, 10000)

    data = turnstile_weather['tempi']
 
    bins = 10
    data.hist(color='LightSkyBlue', bins=bins) # your code here to plot a historgram for hourly entries when it is not raining
    plt.legend()

    return plt

if __name__ == "__main__":
    image = "plot_tempi.png"
    turnstile_weather = pd.read_csv("turnstile_weather_v2.csv")
    plt = entries_histogram(turnstile_weather)
    plt.savefig(image)
    plt.show()


