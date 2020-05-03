#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from time import time
from pprint import pprint

json_file = "phx.json"

def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.osm
    return db

db = get_db()

def remove_data():
    # remove all existing documents for complete reload
    records = db.phx.find().count()
    db.phx.remove({})
    return records
    
def load_data(file_in):
    with open(file_in) as data_file:
        for item in data_file:
            d = json.loads(item)
            db.phx.insert(d)
    records = db.phx.find().count()
    return records

def run(purge = True):
    StartTime = time()
    if purge == True:
        records_removed = remove_data()
        print "Processing took %f minutes to remove %i documents" % ((time()-StartTime)/float(60), records_removed)

    records_loaded = load_data(json_file)
    print "Processing took %f minutes to load %i records" % ((time()-StartTime)/float(60), records_loaded)

if __name__ == "__main__":
    run(True)

