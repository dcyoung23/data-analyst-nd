#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint

def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.osm
    return db

db = get_db()

doc_count = db.phx.find().count()
node_count = db.phx.find({"type" : "node"}).count()
way_count = db.phx.find({"type" : "way"}).count()
users = db.phx.distinct("created.user")

amenity = db.phx.aggregate([{"$match" : {"amenity" : {"$exists" : 1}}},
                            {"$group" : {"_id" : "$amenity" , "count" : {"$sum" : 1}}},
                            {"$sort" : {"count" : -1}}, {"$limit" : 10}])

parking = db.phx.aggregate([{"$match" : {"amenity" : {"$exists" : 1},"amenity" : "parking"}},
                            {"$match" : {"parking" : {"$exists" : 1}}},
                            {"$group" : {"_id" : "$parking" , "count" : {"$sum" : 1}}},
                            {"$sort" : {"count" : -1}}])

religion = db.phx.aggregate([{"$match" : {"amenity" : {"$exists" : 1},"amenity" : "place_of_worship"}},
                            {"$match" : {"religion" : {"$exists" : 1}}},
                            {"$group" : {"_id" : "$religion" , "count" : {"$sum" : 1}}},
                            {"$sort" : {"count" : -1}}])

fast_food = db.phx.aggregate([{"$match" : {"amenity" : {"$exists" : 1},"amenity" : 'fast_food'}},
                            {"$match" : {"name" : {"$exists" : 1}}},
                            {"$group" : {"_id" : "$name" , "count" : {"$sum" : 1}}},
                            {"$sort" : {"count" : -1}}, {"$limit" : 10}])

restaurant = db.phx.aggregate([{"$match" : {"amenity" : {"$exists" : 1},"amenity" : 'restaurant'}},
                            {"$match" : {"name" : {"$exists" : 1}}},
                            {"$group" : {"_id" : "$name" , "count" : {"$sum" : 1}}},
                            {"$sort" : {"count" : -1}}, {"$limit" : 10}])

cuisine = db.phx.aggregate([{"$match" : {"amenity" : {"$exists" : 1},"amenity" : {"$in" : ['fast_food', 'restaurant']}}},
                            {"$match" : {"cuisine" : {"$exists" : 1}}},
                            {"$group" : {"_id" : "$cuisine" , "count" : {"$sum" : 1}}},
                            {"$sort" : {"count" : -1}}, {"$limit" : 10}])

bicycle = db.phx.aggregate([{"$match" : {"bicycle" : {"$exists" : 1}}},
                            {"$group" : {"_id" : "$bicycle" , "count" : {"$sum" : 1}}},
                            {"$sort" : {"count" : -1}}])

fuel_count = db.phx.find({"amenity" : "fuel"}).count()
fueltype_count = db.phx.find({"fuel_types" : {"$exists" : 1}}).count()


print "Document count: %i" % (doc_count) + '\n'
print "Node count: %i" % (node_count) + '\n'
print "Way count: %i" % (way_count) + '\n'
print "Distinct user count: %i" % (len(users)) + '\n'
print "Total fuel amenities of %i only %i have fuel type data." % (fuel_count, fueltype_count) + '\n'


print "Top 10 amenities:"
for a in amenity:
    item = "{} count = {}".format(a['_id'],a['count'])
    pprint(item)
print '\n'

print "Parking types:"
for p in parking:
    item = "{} count = {}".format(p['_id'],p['count'])
    pprint(item)
print '\n'

print "Religions:"
for r in religion:
    item = "{} count = {}".format(r['_id'],r['count'])
    pprint(item)
print '\n'

print "Top 10 fast food locations:"
for f in fast_food:
    item = "{} count = {}".format(f['_id'],f['count'])
    pprint(item)
print '\n'

print "Top 10 restaurant locations:"
for r in restaurant:
    item = "{} count = {}".format(r['_id'],r['count'])
    pprint(item)
print '\n'

print "Top 10 cuisines:"
for c in cuisine:
    item = "{} count = {}".format(c['_id'],c['count'])
    pprint(item)
print '\n'

print "Bicycle access:"
for b in bicycle:
    item = "{} count = {}".format(b['_id'],b['count'])
    pprint(item)


