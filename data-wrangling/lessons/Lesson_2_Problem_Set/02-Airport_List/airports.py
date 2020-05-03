#!/usr/bin/env python
# -*- coding: utf-8 -*-
# All your changes should be in the 'extract_airports' function
# It should return a list of airport codes, excluding any combinations like "All"

from bs4 import BeautifulSoup
html_page = "options.html"


def extract_airports(page):
    data = []
    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html)
        carrier_list = soup.find(id="AirportList")
        for option in carrier_list.find_all('option'):
            if "All" not in option['value']:
                data.append(option['value'])
        return data

def print_list(label, codes):
    print "\n%s:" % label
    for c in codes:
        print c


def test():
    data = extract_airports(html_page)
    print_list("Airports", data)
    assert len(data) == 15
    assert "ATL" in data
    assert "ABR" in data

test()
