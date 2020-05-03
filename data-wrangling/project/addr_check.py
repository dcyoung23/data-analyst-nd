#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
from time import time
from pprint import pprint
import re

osm_file = "phx.osm"
addr_pre = "addr:"
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')

def get_keys(tag, keys):
    if tag.attrib["k"]:
        key = tag.attrib['k']
        if key not in keys:
            keys[key] = 1
        else:
            keys[key] += 1
    return keys

def process_map(filename):
    addr_main = {}
    addr_sub = {}
    for event, element in ET.iterparse(osm_file, events=("start",)):
        if element.tag == "node" or element.tag == "way":
            for tag in element.iter("tag"):
                key = tag.attrib['k']
                if key[:5] == addr_pre and lower_colon.match(key):
                    addr_main = get_keys(tag, addr_main)
                elif key[:5] == addr_pre and not lower_colon.match(key):
                    addr_sub = get_keys(tag, addr_sub)
                else:
                    pass # do nothing
    return addr_main, addr_sub
    
def run():
    StartTime = time()
    addr_main, addr_sub = process_map(osm_file)
    addr = {}
    addr["addr_main"] = addr_main
    addr["addr_sub"] = addr_sub
    pprint(addr)
    print "Processing took %f minutes for %i distinct address keys." % ((time()-StartTime)/float(60), len(addr_main) + len(addr_sub))

if __name__ == "__main__":
    run()

