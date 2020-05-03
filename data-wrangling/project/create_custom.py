#!/usr/bin/env python
# -*- coding: utf-8 -*-

def create_addr(key, value, cities, address_dict):
    import re
    from scrub_fields import scrub_street, scrub_city, scrub_zip
    addr_pre = key[:5]
    lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
    if lower_colon.match(key):
        # create new addr field without the addr: text
        new_addr = key.replace(addr_pre,"")
        if new_addr == "street":
            # scrub street
            value = scrub_street(value)
        elif new_addr == "city":
            # scrub city name
            value = scrub_city(cities, value, .75)
        elif new_addr == "state":
            # all state values should be AZ for Phoenix OSM
            if value != "AZ":
                value = "AZ"
        elif new_addr == "postcode":
            # scrub zip
            value = scrub_zip(value)
        elif new_addr == "country":
            # all country values should be US for Phoenix OSM
            if value != "US":
                value = "US"
        # add to address dict
        address_dict[new_addr] = value   
    else:
        # ignore all else including address fields with double colons
        pass # do nothing
    return address_dict

def create_fuel(key, value, fuel_dict):
    import re
    fuel_pre = key[:5]
    value = value.lower()
    lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
    if lower_colon.match(key):
        fuel_type = key.replace(fuel_pre,"")
        fuel_dict[fuel_type] = value
    else:
        pass # do nothing
    return fuel_dict


