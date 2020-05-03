#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
import re
import codecs
import json
from time import time
from pprint import pprint

from create_custom import create_addr, create_fuel
from scrub_fields import scrub_bicycle
from city_data import process_html, get_items

# process cities once
cities = get_items('Common Cities', process_html())

osm_file = "phx.osm"

problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')
    
# list to easily add new top level tags in output
TOP_TAG = [ "id" ]
# list for created dict
CREATED = [ "version", "changeset", "timestamp", "user", "uid" ]
# list for position list
POSITION = [ "lat", "lon" ]

# test if string is float
def is_float(s):
    try:
        s = s.replace(",","")
        float(s)
        return True
    except ValueError:
        return False

def shape_element(element):
    # create empty dict/list
    node = {}
    created_dict = {}
    pos = []
    address_dict = {}
    fuel_dict = {}
    nd_ref = []
    if element.tag == "node" or element.tag == "way" :
        # isolate node attributes dict
        attribs = element.attrib
        #pprint(attribs)

        # element tag for all types
        node["type"] = element.tag

        # top level tags
        for item in TOP_TAG:
            if item in attribs:
                node[item] = attribs[item]

        # created fields
        for item in CREATED:
            if item in attribs:
                created_dict[item] = attribs[item]
        if len(created_dict) > 0:
            node["created"] = created_dict

        # position
        for item in POSITION:
            if item in attribs:
                f = attribs[item]
                if is_float(f) == True:
                    pos.append(float(f))
        if len(pos) > 0:
            node["pos"] = pos

        # loop through k atrributes
        for tag in element.iter("tag"):
            check = tag.attrib['k']
            value = tag.attrib["v"]

            # ignore if key has problem chars
            if problemchars.search(check):
                pass # do nothing

            #ignore if key has been labeled "fixme"
            elif check[:5].lower() == "fixme":
                pass # do nothing

            # scrub bicycle value
            elif check == "bicycle":
                bicycle_value = scrub_bicycle(value)
                node[check] = bicycle_value
                        
            # create address dict
            elif check[:4] == "addr":
                address_dict = create_addr(check, value, cities, address_dict)

            # create fuel set
            elif check[:4] == "fuel":
                fuel_dict = create_fuel(check, value, fuel_dict)
           
            # all other include as is
            else:
                node[check] = tag.attrib["v"]

        # add address dict to node
        if len(address_dict) > 0:
            #pprint(address_dict)
            node["address"] = address_dict

        # convert fuel set to sorted list and add to node
        if len(fuel_dict) > 0:
            #pprint(fuel_dict)
            node["fuel_types"] = fuel_dict
            
        # create node list
        for nd in element.iter("nd"):
            nd_ref.append(nd.attrib["ref"])
        if len(nd_ref) > 0:
            node["node_refs"] = nd_ref
       
        return node
    else:
        return None

def process_map(file_in, pretty = False):
    # for json output replace .osm from the filename
    file_out = "{0}.json".format(file_in.replace(".osm",""))
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, element in ET.iterparse(file_in):
            el = shape_element(element)
            if el:
                #pprint(el)
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2)+"\n")
                else:
                    fo.write(json.dumps(el) + "\n")
    return data

def run():
    StartTime = time()
    data = process_map(osm_file, False)
    print "Processing took %f minutes for %i records" % ((time()-StartTime)/float(60), len(data))

if __name__ == "__main__":
    run()

