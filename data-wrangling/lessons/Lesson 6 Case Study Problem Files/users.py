#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
from pprint import pprint
import re

"""
Your task is to explore the data a bit more.
The first task is a fun one - find out how many unique users
have contributed to the map in this particular area!

The function process_map should return a set of unique user IDs ("uid")
"""

# define user identifier field
uid = "uid"

def get_user(element):
    return element[uid]

def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        attrib = element.attrib
        if uid in attrib:
            user = get_user(attrib)
            users.add(user)
    return users

def test():

    users = process_map('users.xml')
    pprint(users)
    assert len(users) == 6

if __name__ == "__main__":
    test()
