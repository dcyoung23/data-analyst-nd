import pandas as pd
import pandasql
import matplotlib.pyplot as plt
from time_period import time_period

def entries_time_period_bar(turnstile_weather):

    # Add Time Period 
    turnstile_weather = time_period(turnstile_weather)

    q = """
    select time_period as Time_Period,sum(ENTRIESn_hourly) as ENTRIESn_hourly
    from turnstile_weather
    group by time_period
    """
    
    #Execute your SQL command against the pandas frame
    entries_time_period = pandasql.sqldf(q, locals())

    plt.figure()
    plt.title('Turnstile Entries by Time Period')
    plt.ylabel('Turnstile Entries (in millions)')
    plt.xlabel('Time Period')

    y = entries_time_period['ENTRIESn_hourly']/1000000
    x = entries_time_period['Time_Period']
    labels = ['Late Night','Weekends','Midday','Evening','Rush Hour']

    plt.xticks(x, labels)
    plt.xlim(0,6)
    plt.ylim(0,25)
    plt.bar(x, y,width=0.25,align='center',color='DodgerBlue')

    #print entries_time_period

    return plt

if __name__ == "__main__":
    image = "plot_entries_time_period.png"
    turnstile_weather = pd.read_csv("turnstile_weather_v2.csv")
    plt = entries_time_period_bar(turnstile_weather)
    plt.savefig(image)
    plt.show()
