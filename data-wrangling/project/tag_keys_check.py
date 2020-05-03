#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
from pprint import pprint
import re

osm_file = "phx.osm"

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

def key_check(element, check):
    if element.tag == "tag":
        key = element.attrib['k']
        if problemchars.search(key):
            check["problemchars"] += 1
        elif lower.match(key):
            check["lower"] += 1
        elif lower_colon.match(key):
            check["lower_colon"] += 1
        else:
            check["other"] += 1
    return check

def process_map(filename):
    check = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for event, element in ET.iterparse(filename, events=("start",)):
        check = key_check(element, check)
    return check

def run():
    keys = process_map(osm_file)
    pprint(keys)

if __name__ == "__main__":
    run()
