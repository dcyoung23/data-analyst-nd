import pandas as pd
import pandasql

def time_period(turnstile_weather):

    q = """
    select *
    ,case
    when hour <=5 then 1
    when weekday = 0 and hour >= 6 then 2
    when weekday = 1 and hour between 10 and 14 then 3
    when weekday = 1 and hour >= 20 then 4
    when weekday = 1 and hour between 6 and 9 then 5
    when weekday = 1 and hour between 15 and 19 then 5
    else 0 end as time_period
    from turnstile_weather
    """
    
    #Execute your SQL command against the pandas frame
    time_period = pandasql.sqldf(q, locals())
    
    return time_period
