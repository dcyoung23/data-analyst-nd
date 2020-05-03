import pandas as pd
import pandasql
import matplotlib.pyplot as plt

def entries_time_period_bar(turnstile_weather):

    # add new fields
    turnstile_weather['dayofweek'] = pd.DatetimeIndex(turnstile_weather['DATEn']).dayofweek
    turnstile_weather['day'] = pd.DatetimeIndex(turnstile_weather['DATEn']).day

    turnstile_weather['weekday'] = 0
    turnstile_weather.loc[turnstile_weather['dayofweek'] <= 4, 'weekday'] = 1

    q = """
    select *
    ,case
    when Hour <=5 then 1
    when weekday = 0 and Hour >= 6 then 2
    when weekday = 1 and Hour between 10 and 14 then 3
    when weekday = 1 and Hour >= 20 then 4
    when weekday = 1 and Hour between 6 and 9 then 5
    when weekday = 1 and Hour between 15 and 19 then 5
    else 0 end as timeperiod
    from turnstile_weather
    """
    
    #Execute your SQL command against the pandas frame
    turnstile_weather2 = pandasql.sqldf(q.lower(), locals())


    q2 = """
    select time_period,sum(ENTRIESn_hourly) as ENTRIESn_hourly
    from turnstile_weather2
    group by time_period
    """
    
    #Execute your SQL command against the pandas frame
    entries_time_period = pandasql.sqldf(q2.lower(), locals())

    plt.figure()
    plt.title('Turnstile Entries by Time Period')
    plt.ylabel('Turnstile Entries (in millions)')
    plt.xlabel('Time Period')

    y = entries_time_period['ENTRIESn_hourly']/1000000
    x = entries_time_period['time_period']
    labels = ['Late Night','Weekends','Midday','Evening','Rush Hour']

    plt.xticks(x, labels)
    plt.xlim(0,6)
    plt.ylim(0,25)
    plt.bar(x, y,width=0.25,align='center',color='DodgerBlue')

    #print entries_time_period

    return plt


if __name__ == "__main__":
    image = "plot_entries_time_period.png"
    turnstile_weather = pd.read_csv("turnstile_data_master_with_weather.csv")
    plt = entries_time_period_bar(turnstile_weather)
    plt.savefig(image)
    plt.show()
