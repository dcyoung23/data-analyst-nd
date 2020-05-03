import numpy as np
import pandas as pd
from random import sample

df = pd.DataFrame({'col1':['A','A','A','B','B','B'], 'col2':['C','D','D','D','C','C'], 'col3':[.1,.2,.4,.6,.8,1]})

#print df

g = df.groupby('col1')
#print g.get_group('A')

#g.get_group('A')['col1'].unique()

#sum(g.get_group('A')['col2'])

predict_sum = g.sum().reset_index()

#print predict_sum.select_dtypes(include=['float64'])

# given data frame df

# create random index
rindex =  np.array(sample(xrange(len(df)), 2))

# get 10 random rows from df
dfr = df.ix[rindex]

#print rindex

print df.loc[sample(df.index, 2)]

