import numpy as np
import pandas as pd
import scipy
import statsmodels.api as sm


def predictions(weather_turnstile):
    # load the dataset
    turnstile_master = pd.read_csv(weather_turnstile)

    dummy_units = pd.get_dummies(turnstile_master['UNIT'], prefix='unit')
    dummy_hours = pd.get_dummies(turnstile_master['Hour'], prefix='hour')
    dummy_combined = dummy_units.join(dummy_hours)

    turnstile_master['dayofweek'] = pd.DatetimeIndex(turnstile_master['DATEn']).dayofweek
    turnstile_master['weekday'] = 0
    turnstile_master.loc[turnstile_master['dayofweek'] <= 4, 'weekday'] = 1
    turnstile_master['day'] = pd.DatetimeIndex(turnstile_master['DATEn']).day

    values = turnstile_master[['ENTRIESn_hourly']] # response
    features = turnstile_master[['weekday', 'rain', 'mintempi', 'fog']].join(dummy_combined) # predictor
    features = sm.add_constant(features)  # Adds a constant term to the predictor

    est = sm.OLS(values, features).fit()
    prediction = est.predict(features)

    return prediction

input_filename = "turnstile_data_master_with_weather.csv"

print predictions(input_filename)

