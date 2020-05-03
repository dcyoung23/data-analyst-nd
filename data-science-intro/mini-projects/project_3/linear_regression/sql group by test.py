# load numpy and pandas for data manipulation
import numpy as np
import pandas as pd
import pandasql

# load statsmodels
import statsmodels.api as sm

# load matplotlib/ggplot for plots
import matplotlib.pyplot as plt
from ggplot import *

# load random
from random import sample

# load the dataset
input_filename = "turnstile_data_master_with_weather.csv"
df = pd.read_csv(input_filename)

# add new fields
df['Dayofweek'] = pd.DatetimeIndex(df['DATEn']).dayofweek
df['Weekday'] = 0
df.loc[df['Dayofweek'] <= 4, 'Weekday'] = 1
df['day'] = pd.DatetimeIndex(df['DATEn']).day

df = df[['UNIT','Dayofweek', 'Hour', 'ENTRIESn_hourly']]

q = """
select UNIT, Dayofweek, Hour, SUM(ENTRIESn_hourly) as ENTRIESn_hourly
from df
group by UNIT, Dayofweek, Hour
"""
    
#Execute your SQL command against the pandas frame
turnstile_master = pandasql.sqldf(q, locals())

print turnstile_master

output_filename = "turnstile_data_master_with_weather_grouped.csv"
turnstile_master.to_csv(output_filename)
