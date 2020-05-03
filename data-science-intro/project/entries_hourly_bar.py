import pandas as pd
import pandasql
import matplotlib.pyplot as plt

def entries_hourly_bar(turnstile_weather):


    q = """
    select hour as Hour,sum(ENTRIESn_hourly) as ENTRIESn_hourly
    from turnstile_weather
    group by hour
    """
    
    #Execute your SQL command against the pandas frame
    entries_hourly = pandasql.sqldf(q, locals())

    plt.figure()
    plt.title('Turnstile Entries by Hour')
    plt.ylabel('Turnstile Entries (in millions)')
    plt.xlabel('Hour')

    y = entries_hourly['ENTRIESn_hourly']/1000000
    x = entries_hourly['Hour']

    plt.xticks(range(0,24))
    plt.xlim((-1,23))
    plt.bar(x, y,width=0.7,align='center',color='DodgerBlue')

    #print entries_hourly

    return plt

if __name__ == "__main__":
    image = "plot_entries_hour.png"
    turnstile_weather = pd.read_csv("turnstile_weather_v2.csv")
    plt = entries_hourly_bar(turnstile_weather)
    plt.savefig(image)
    plt.show()
