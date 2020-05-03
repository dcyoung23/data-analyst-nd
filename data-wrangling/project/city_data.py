#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import time
from pprint import pprint

def process_html():
    from bs4 import BeautifulSoup
    # http://www.unitedstateszipcodes.org/az/#zips
    html_page = "az_zip_codes.html"
    keys = ['Zip Code', 'Type', 'Common Cities', 'County']
    counter = 0
    info = {}
    data = []

    with open(html_page, "r") as html:
        soup = BeautifulSoup(html)
        table = soup.find("table", { "class" : "table table-hover table-striped"})

        rows = table.find_all('tr')
        rows = rows[1:]

        for row in rows:
            # test
            if counter < 0:
                break
            else:
                values = row.find_all(text=True)
                values = values[:4]
              
                for i, value in enumerate(values):
                    value = value.strip()
                    value = value.encode("utf-8")
                    info[keys[i]] = value

                data.append(dict(info))
                counter += 1
    return data
                            
def get_items(field, data):
    items = set()
    for item in data:
        a = item[field]
        split_item = a.split(',')
        for item in split_item:
            item = item.replace('...','')
            item = item.strip()
            if len(item) > 0:
                items.add(item)
    s = sorted(items)
    return s

if __name__ == "__main__":
    StartTime = time()
    data = process_html()
    
    print "Processing took %f minutes for %i records" % ((time()-StartTime)/float(60), len(data))
    
    zips = get_items('Zip Code', data)
    cities = get_items('Common Cities', data)

    pprint(data[0])
    pprint(zips[0])
    pprint(cities[0])

