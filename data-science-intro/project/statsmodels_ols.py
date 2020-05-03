import numpy as np
import pandas as pd
import pandasql
import statsmodels.api as sm
from time_period import time_period

# Load data
input_filename = "turnstile_weather_v2.csv"
df = pd.read_csv(input_filename)

# Add Time Period 
df = time_period(df)

# Create dummy units and combine
dummy_units = pd.get_dummies(df['UNIT'], prefix='unit')
dummy_hour = pd.get_dummies(df['time_period'], prefix='time')
dummy_combined = dummy_units.join(dummy_hour)

values = df[['ENTRIESn_hourly']] # response
features = df[['rain', 'tempi', 'wspdi']].join(dummy_combined) # predictor
features = sm.add_constant(features)  # Adds a constant term to the predictor

#features = features.drop('unit_R034', 1)

mod = sm.OLS(values, features)
res = mod.fit()
print res.summary()

#print res.params
#print res.rsquared

df['ENTRIESn_hourly_predict'] = res.predict(features)

#print df.head()



