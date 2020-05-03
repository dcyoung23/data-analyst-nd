#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
from pprint import pprint

def count_tags(filename):
        tags = {}
        for event, elem in ET.iterparse(filename):
            # if key does not exist add
            if elem.tag not in tags:
                tags[elem.tag] = 1
            # else +1
            else:
                tags[elem.tag] += 1
        return tags
                
def test():

    tags = count_tags('mapparser.xml')
    pprint(tags)

if __name__ == "__main__":
    test()
