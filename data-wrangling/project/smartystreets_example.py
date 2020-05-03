#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib
from pprint import pprint

'''
{u'_id': ObjectId('55879136168d5daceafa52f0'),
 u'address': {u'city': u'Chandler',
              u'housenumber': u'290',
              u'postcode': u'85225',
              u'state': u'AZ',
              u'street': u'South Cooper Road'},
 u'amenity': u'school',
 u'created': {u'changeset': u'30879069',
              u'timestamp': u'2015-05-07T17:03:39Z',
              u'uid': u'2896459',
              u'user': u'anunlikelycloud',
              u'version': u'1'},
 u'id': u'343496958',
 u'name': u'Chief Hill Learning Academy',
 u'node_refs': [u'3503303392',
                u'3503305093',
                u'3503305094',
                u'3503305095',
                u'3503305096',
                u'3503305097',
                u'3503305098',
                u'3503305099',
                u'3503305100',
                u'3503305101',
                u'3503305102',
                u'3503305103',
                u'3503305104',
                u'3503303392'],
 u'operator': u'Chandler Unified School District',
 u'type': u'way'}
'''

# Replace with valid AUTH_ID and AUTH-TOKEN
LOCATION = "https://api.smartystreets.com/street-address"
QUERY_STRING = urllib.urlencode({
  "auth-id": r"AUTH-ID", # UPDATE HERE
  "auth-token": r"AUTH-TOKEN", # UPDATE HERE
    "street": "290 south cooper road",
    "city": "chandler",
    "state": "az",
    "zipcode": "85225",
    "candidates": "1",
})

URL = LOCATION + "?" + QUERY_STRING

# Perform request, read result, and load from string into Python object
response = urllib.urlopen(URL).read()
results = json.loads(response)
pprint(results)

'''
[{u'analysis': {u'active': u'Y',
                u'dpv_cmra': u'N',
                u'dpv_footnotes': u'AABB',
                u'dpv_match_code': u'Y',
                u'dpv_vacant': u'N',
                u'footnotes': u'N#'},
  u'candidate_index': 0,
  u'components': {u'city_name': u'Chandler',
                  u'delivery_point': u'90',
                  u'delivery_point_check_digit': u'0',
                  u'plus4_code': u'5897',
                  u'primary_number': u'290',
                  u'state_abbreviation': u'AZ',
                  u'street_name': u'Cooper',
                  u'street_predirection': u'S',
                  u'street_suffix': u'Rd',
                  u'zipcode': u'85225'},
  u'delivery_line_1': u'290 S Cooper Rd',
  u'delivery_point_barcode': u'852255897900',
  u'input_index': 0,
  u'last_line': u'Chandler AZ 85225-5897',
  u'metadata': {u'carrier_route': u'C011',
                u'congressional_district': u'05',
                u'county_fips': u'04013',
                u'county_name': u'Maricopa',
                u'elot_sequence': u'0009',
                u'elot_sort': u'A',
                u'latitude': 33.3007,
                u'longitude': -111.8076,
                u'precision': u'Zip9',
                u'rdi': u'Commercial',
                u'record_type': u'S',
                u'time_zone': u'Mountain',
                u'utc_offset': -7,
                u'zip_type': u'Standard'}}]
'''
