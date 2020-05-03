#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
from pprint import pprint
import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
#pprint(enron_data)
#print enron_data["PRENTICE JAMES"]["total_stock_value"]
#pprint(enron_data["SKILLING JEFFREY K"])
#pprint(enron_data["LAY KENNETH L"])
#pprint(enron_data["FASTOW ANDREW S"])

#print len(enron_data["SKILLING JEFFREY K"])

cnt = 0

for i in enron_data:
    if enron_data[i]["total_payments"] == 'NaN':
        #print i
        cnt += 1
print cnt

print float(cnt)/len(enron_data)
        
    
