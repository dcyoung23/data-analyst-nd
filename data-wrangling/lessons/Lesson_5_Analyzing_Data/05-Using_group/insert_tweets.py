#!/usr/bin/env python

import json
from pprint import pprint
from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.twitter

db.tweets.remove({})

with open('twitter.json') as data_file:
    for item in data_file:
        d = json.loads(item)
        db.tweets.insert(d)
        #pprint(d)

pprint(db.tweets.find().count())
#pprint(db.tweets.find_one())
