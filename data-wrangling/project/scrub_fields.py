#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from city_data import process_html, get_items
from pprint import pprint

cities = get_items('Common Cities', process_html())

def scrub_bicycle(bicycle):
    bicycle = bicycle.lower()
    bicycle = bicycle.split(";")
    bicycle = bicycle[0]
    return bicycle
    

def scrub_street(street):
    import re
    # dict for street type scrubbing
    street_mapping = { "Ave": "Avenue",
                    "Blvd": "Boulevard",
                    "Bldg": "Building",
                    "Ctr": "Center",
                    "circle": "Circle",
                    "Dr": "Drive",
                    "Pkwy": "Parkway",
                    "Parkwway": "Parkway",
                    "RD": "Road",
                    "Rd": "Road",
                    "St": "Street",
                    "street": "Street",
                    "Ste": "Suite",
                    "E": "East",
                    "N": "North",
                    "S": "South",
                    "W": "West"
                   }

    # remove periods from street
    street = street.replace(".","")
    # remove commas from street
    street = street.replace(",","")
    rx = re.compile(r'\b%s\b' % r'\b|\b'.join(map(re.escape, street_mapping)))
    def map_match(match):
        return street_mapping[match.group(0)]
    return rx.sub(map_match, street)

def scrub_city(cities, city_in, match_target):

    from difflib import SequenceMatcher as SM
    from string import capwords

    # Manual handling of street address in city field
    if city_in == "2036 N. Gilbert Rd.":
        city_in = "Mesa"
        
    city_out = city_in.lower()
    city_out = capwords(city_out)
    city_out = city_out.split(",")
    city_out = city_out[0]

    if city_out not in cities:
        for city in cities:
            match = SM(None, city_out, city).ratio()
            if match > match_target:
                # Reset match target based on current match
                match_target = match
                city_out = city
    return city_out

def scrub_zip(zip_in):
    # remove AZ from zip
    zip_out = zip_in.replace("AZ","")
    # strip white spaces
    zip_out = zip_out.strip()
    # encode to remove printable characters
    zip_out = zip_out.encode("utf-8")
    return zip_out


if __name__ == "__main__":
    bicycle_test = "designated;yes"
    street_test = "123 S Avery street,"
    city_test = "Luke AFB, Waddell"
    zip_test = "AZ 85007"

    pprint(scrub_bicycle(bicycle_test))
    pprint(scrub_street(street_test))
    pprint(scrub_city(cities, city_test, .75))
    pprint(scrub_zip(zip_test))

