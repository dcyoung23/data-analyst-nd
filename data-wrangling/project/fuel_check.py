#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
from time import time
from pprint import pprint
import re

osm_file = "phx.osm"
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')

def get_values(value, values):
    if value not in values:
        values[value] = 1
    else:
        values[value] += 1
    return values

def process_map(filename):     
    values = {}
    for event, element in ET.iterparse(filename, events=("start",)):
        if element.tag == "node" or element.tag == "way":
            for tag in element.iter("tag"):
                key = tag.attrib['k']
                value = tag.attrib['v']
                if key[:4] == "fuel":
                    fuel_type = '{}-{}'.format(key,value)
                    values = get_values(fuel_type, values)                    
    return values

def run():
    StartTime = time()
    values = process_map(osm_file)
    pprint(values)
    print "Processing took %f minutes for %i distinct fuel values." % ((time()-StartTime)/float(60), len(values))


if __name__ == '__main__':
    run()
