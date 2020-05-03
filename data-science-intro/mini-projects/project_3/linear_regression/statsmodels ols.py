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
df['day'] = pd.DatetimeIndex(df['DATEn']).day

df['Weekday'] = 0
df.loc[df['Dayofweek'] <= 4, 'Weekday'] = 1

df['Timeperiod'] = 0
df.loc[(df['Hour'] <= 5), 'Timeperiod'] = 1 #Late night
df.loc[(df['Weekday'] == 0) & (df['Hour'] >= 6) & (df['Hour'] <= 23), 'Timeperiod'] = 2 #Weekends
df.loc[(df['Weekday'] == 1) & (df['Hour'] >= 10) & (df['Hour'] <= 14), 'Timeperiod'] = 3 #Midday
df.loc[(df['Weekday'] == 1) & (df['Hour'] >= 21) & (df['Hour'] <= 23), 'Timeperiod'] = 4 #Evening
df.loc[(df['Weekday'] == 1) & (df['Hour'] >= 6) & (df['Hour'] <= 9), 'Timeperiod'] = 5 #Rushhour
df.loc[(df['Weekday'] == 1) & (df['Hour'] >= 15) & (df['Hour'] <= 20), 'Timeperiod'] = 5 #Rushhour

dummy_units = pd.get_dummies(df['UNIT'], prefix='unit')
dummy_time = pd.get_dummies(df['Timeperiod'], prefix='time')
dummy_combined = dummy_units.join(dummy_time)

values = df[['ENTRIESn_hourly']] # response
features = df[['EXITSn_hourly', 'rain', 'meantempi']].join(dummy_combined) # predictor
features = sm.add_constant(features)  # Adds a constant term to the predictor

print features.head()

est = sm.OLS(values, features).fit()
df['ENTRIESn_hourly_predict'] = est.predict(features)
print est.summary()

print df.head()
output_filename = "turnstile_data_master_with_weather_predict.csv"
df.to_csv(output_filename)

'''
grouped_data = turnstile_master.groupby('DATEn').ENTRIESn_hourly.sum()
df['ENTRIESn_hourly'] = df.groupby('A')['values'].transform(np.sum)
print grouped_data

gg = ggplot(grouped_data,aes(x='DATEn',y='ENTRIESn_hourly')) + geom_point() + geom_line() + ggtitle('Hourly Entries by Date') + xlab('Date') + ylab('Entries')
image = "plot.png"
ggsave(image, gg, width=11, height=8)


grouped_data = turnstile_master.groupby('DATEn')#.ENTRIESn_hourly.sum()

gg = ggplot(grouped_data,aes(x='Date',y='ENTRIESn_hourly')) + geom_point() + geom_line() + ggtitle('Hourly Entries by Date') + xlab('Date') + ylab('Entries')
image = "plot.png"
ggsave(image, gg, width=11, height=8)
    
#,color='teamID'
'''

'''
ypred = est.predict(X)
print(ypred)

fig, ax = plt.subplots()
ax.plot(x1, y, 'o', label="Data")
ax.plot(x1, , 'b-', label="True")
ax.plot(np.hstack((x1, x1n)), np.hstack((ypred, ynewpred)), 'r', label="OLS prediction")
ax.legend(loc="best");
'''
