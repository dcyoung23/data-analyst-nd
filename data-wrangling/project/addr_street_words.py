#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
from time import time
from pprint import pprint

letters = ["a", "b", "c", "d", "e", "h", "j", "l", "n", "o", "p", "r", "s", "t", "v", "w"]
osm_file = "phx.osm"

def get_words(item, dict_in):
    if item not in dict_in:
        dict_in[item] = 1
    else:
        dict_in[item] += 1
    return dict_in

def process_map(filename):
    words = {}
    for event, element in ET.iterparse(filename, events=("start",)):
        if element.tag == "node" or element.tag == "way":
            for tag in element.iter("tag"):
                key = tag.attrib['k']
                if key == "addr:street":
                    street_name = tag.attrib['v']
                    street_words = street_name.split()
                    for item in street_words:
                        if item[:1].lower() in letters:
                            # use raw item in dict for review for mapping
                            words = get_words(item, words)
    return words

def run():
    StartTime = time()
    words = process_map(osm_file)
    pprint(words)
    print "Processing took %f minutes for %i distinct words." % ((time()-StartTime)/float(60), len(words))

if __name__ == '__main__':
    run()
