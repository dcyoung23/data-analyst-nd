import pandas as pd
import pandasql
import matplotlib.pyplot as plt
from time_period import time_period

def entries_day_line(turnstile_weather):

    # Add Time Period 
    turnstile_weather = time_period(turnstile_weather)

    q = """
    select day_week as Day_Week,sum(ENTRIESn_hourly) as ENTRIESn_hourly
    from turnstile_weather
    group by day_week
    """
    
    #Execute your SQL command against the pandas frame
    entries_day = pandasql.sqldf(q, locals())

    plt.figure()
    plt.title('Turnstile Entries by Day (5/1/2011 - 5/31/2011)')
    plt.ylabel('Turnstile Entries (in millions)')
    plt.xlabel('Day of Week')

    y = entries_day['ENTRIESn_hourly']/1000000
    x = entries_day['Day_Week']
    labels = ['Mon','Tue','Wed','Thur','Fri', 'Sat', 'Sun']

    plt.xticks(x, labels)
    plt.xlim(-1,7)
    plt.ylim(0,25)
    plt.plot(x,y,marker='.',linestyle='--')

    #print entries_day

    return plt

if __name__ == "__main__":
    image = "plot_entries_day.png"
    turnstile_weather = pd.read_csv("turnstile_weather_v2.csv")
    plt = entries_day_line(turnstile_weather)
    plt.savefig(image)
    plt.show()
