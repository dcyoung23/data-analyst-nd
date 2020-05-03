#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
from time import time
from pprint import pprint
import re

osm_file = "phx.osm"
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

def update_items(item, items):
    if item not in items:
        items[item] = 1
    else:
        items[item] += 1
    return items

def process_map(filename):
    tags = {}
    keys = {}
    tagk = {}
    for event, element in ET.iterparse(filename, events=("start",)):
        tag = element.tag
        tags = update_items(tag, tags)
        attribs = element.attrib
        for i, key in enumerate(attribs):
            key = "{}-{}".format(tag, key)
            keys = update_items(key, keys)
        if tag == "node" or tag == "way":
            for tag in element.iter("tag"):
                tag2 = element.tag
                key2 = tag.attrib['k']
                if problemchars.search(key2):
                    print key2
                else:
                    key = "{}-{}".format(tag2, key2)
                    keys = update_items(key, keys)
    return tags, keys

def run():
    StartTime = time()
    tags, keys = process_map(osm_file)
    pprint(tags)
    pprint(keys)
    print "Processing took %f minutes for %i top level tags." % ((time()-StartTime)/float(60), len(tags))

if __name__ == "__main__":
    run()
