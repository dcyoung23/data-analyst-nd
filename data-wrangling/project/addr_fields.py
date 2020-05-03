#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
from time import time
from pprint import pprint
import re
from city_data import process_html, get_items

# add fields to research
fields = ["country", "city", "state", "postcode"]
osm_file = "phx.osm"

def get_values(value, values):
    if value not in values:
        values[value] = 1
    else:
        values[value] += 1
    return values

def process_map(filename, fields):
    addr_pre = "addr:"
    combined = {}
    for field in fields:
        addr_field = addr_pre + field       
        values = {}
        for event, element in ET.iterparse(filename, events=("start",)):
            if element.tag == "node" or element.tag == "way":
                for tag in element.iter("tag"):
                    if tag.attrib['k'] == addr_field:
                        values = get_values(tag.attrib['v'], values)
        combined[field] = values                      
    return combined

def run():
    StartTime = time()
    combined = process_map(osm_file, fields)
    pprint(combined)
    print "Processing took %f minutes for %i distinct address fields." % ((time()-StartTime)/float(60), len(combined))


if __name__ == '__main__':
    run()



