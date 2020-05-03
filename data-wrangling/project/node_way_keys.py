#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
from time import time
from pprint import pprint
import re

osm_file = "phx.osm"

def get_keys(tag, keys):
    if tag.attrib["k"]:
        key = tag.attrib['k']
        if key not in keys:
            keys[key] = 1
        else:
            keys[key] += 1
    return keys

def process_map(filename):
    keys = {}
    for event, element in ET.iterparse(filename, events=("start",)):
        if element.tag == "node" or element.tag == "way":
            for tag in element.iter("tag"):
                keys = get_keys(tag, keys)
    return keys
                
def run():
    StartTime = time()
    keys = process_map(osm_file)
    pprint(keys)
    print "Processing took %f minutes for %i records" % ((time()-StartTime)/float(60), len(keys))


if __name__ == "__main__":
    run()
                
            
    
