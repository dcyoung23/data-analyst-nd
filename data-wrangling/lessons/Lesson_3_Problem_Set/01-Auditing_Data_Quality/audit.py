#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a cleaning idea and then clean it up.
In the first exercise we want you to audit the datatypes that can be found in some particular fields in the dataset.
The possible types of values can be:
- 'NoneType' if the value is a string "NULL" or an empty string ""
- 'list', if the value starts with "{"
- 'int', if the value can be cast to int
- 'float', if the value can be cast to float, but is not an int
- 'str', for all other values

The audit_file function should return a dictionary containing fieldnames and a SET of the types
that can be found in the field. e.g.
{"field1: set([float, int, str]),
 "field2: set([str]),
  ....
}

The audit_file function should return a dictionary containing fieldnames and the datatypes that can be found in the field.
All the data initially is a string, so you have to do some checks on the values first.

"""
import codecs
import csv
import json
import pprint

#fieldname = "name"
CITIES = 'cities.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label", "isPartOf_label", "areaCode", "populationTotal", 
          "elevation", "maximumElevation", "minimumElevation", "populationDensity", "wgs84_pos#lat", "wgs84_pos#long", 
          "areaLand", "areaMetro", "areaUrban"]

#for field in FIELDS:
#    print field


def skip_lines(input_file, skip):
    for i in range(0, skip):
        next(input_file)

def is_float(s):
    try:
        s = s.replace(",","")
        float(s)
        return True
    except ValueError:
        return False

def is_int(s):
    try:
        s = s.replace(",","")
        int(s)
        return True
    except ValueError:
        return False
    
'''
- 'NoneType' if the value is a string "NULL" or an empty string ""
- 'list', if the value starts with "{"
- 'int', if the value can be cast to int
- 'float', if the value can be cast to float, but is not an int
- 'str', for all other values
Test = set(["A", "B"])
print Test
Test.add("C")
print Test
Test.add("A")
print Test
'''

def audit_file(filename, fields):
    fieldtypes = {}

    for field in fields:
        fieldtypes[field] = set()
    
    input_file = csv.DictReader(open(filename))
    skip_lines(input_file, 3)
    
    nrows = 0

    for row in input_file:
        for fieldname, value in row.iteritems():
            v = value.strip()
            if fieldname in fieldtypes:
                if v == "NULL" or v == "":
                    fieldtypes[fieldname].add('NoneType')
                elif v[:1] == "{":
                    fieldtypes[fieldname].add('list')
                elif is_int(v) == True:
                    fieldtypes[fieldname].add('int')
                elif is_float(v) == True:
                    fieldtypes[fieldname].add('float')
                else:
                    fieldtypes[fieldname].add('str')

    nrows += 1

    return fieldtypes


def test():
    fieldtypes = audit_file(CITIES, FIELDS)
    
    pprint.pprint(fieldtypes)

    #assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    #assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])
    
if __name__ == "__main__":
    test()


'''
v = row[fieldname]
v = v.strip()
#print v
#print fieldname + ": " + v
if v == "NULL" or v == "":
    new_set.add('NoneType')
elif v[:1] == "{":
    new_set.add('list')
elif is_int(v) == True:
    new_set.add('int')
elif is_float(v) == True:
    new_set.add('float')
else:
    new_set.add('str')

fieldtypes[fieldname] = new_set
print fieldtypes
'''
