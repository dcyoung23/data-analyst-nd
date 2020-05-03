import pandas as pd
from datetime import datetime
from ggplot import *

turnstile_weather = pd.read_csv('turnstile_data_master_with_weather.csv')
daysn = []

def get_day(date):
    return datetime.strftime(datetime.strptime(date,'%Y-%m-%d').date(),'%a')

for the_date in turnstile_weather['DATEn']:
    daysn.append(get_day(the_date))

turnstile_weather['Dayn'] = daysn

grouped = turnstile_weather.groupby('Dayn',as_index=False).sum()
plot = ggplot(grouped, aes(x='Dayn',y='ENTRIESn_hourly')) + \
       geom_bar(aes(weight='ENTRIESn_hourly'), fill='blue')

image = "plot.png"
ggsave(image, plot, width=11, height=8)


