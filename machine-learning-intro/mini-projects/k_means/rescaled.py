import pickle
from sklearn import preprocessing
import numpy as np
import sys
sys.path.append("../tools/")

from pprint import pprint

def scaled_feature(feature, f):

    ### load in the dict of dicts containing all the data on each person in the dataset
    data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
    ### there's an outlier--remove it! 
    data_dict.pop("TOTAL", 0)

    #print data_dict.itervalues().next()
    data = []
    for item in enumerate(data_dict):
        #print item
        value = data_dict[item[1]][feature]
        #print value
        if value != "NaN":
            data.append(float(value))

    #pprint(salary)

    mn = float(min(data))
    mx = float(max(data))
    rng = mx - mn

    #print mn
    #print mx
    #print rng

    arr = np.array(data)
    min_max_scaler = preprocessing.MinMaxScaler()
    data_minmax = min_max_scaler.fit_transform(arr)
    #print salary_arr
    #print salary_minmax

    output = (f - mn) / rng

    return output

print scaled_feature('salary', 200000.0)
print scaled_feature('exercised_stock_options', 1000000.0)


    


