#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Let's assume that you combined the code from the previous 2 exercises
# with code from the lesson on how to build requests, and downloaded all the data locally.
# The files are in a directory "data", named after the carrier and airport:
# "{}-{}.html".format(carrier, airport), for example "FL-ATL.html".
# The table with flight info has a table class="dataTDRight".
# There are couple of helper functions to deal with the data files.
# Please do not change them for grading purposes.
# All your changes should be in the 'process_file' function
from bs4 import BeautifulSoup
from zipfile import ZipFile
import os

datadir = "data"


def open_zip(datadir):
    with ZipFile('{0}.zip'.format(datadir), 'r') as myzip:
        myzip.extractall()


def process_all(datadir):
    files = os.listdir(datadir)
    return files


def process_file(f):
    # This is example of the datastructure you should return
    # Each item in the list should be a dictionary containing all the relevant data
    # Note - year, month, and the flight data should be integers
    # You should skip the rows that contain the TOTAL data for a year
    # data = [{"courier": "FL",
    #         "airport": "ATL",
    #         "year": 2012,
    #         "month": 12,
    #         "flights": {"domestic": 100,
    #                     "international": 100}
    #         },
    #         {"courier": "..."}
    # ]
    data = []
    info = {}
    info["courier"], info["airport"] = f[:6].split("-")
    #print info
    
    with open("{}/{}".format(datadir, f), "r") as html:

        soup = BeautifulSoup(html)
        table = soup.find("table", { "id" : "DataGrid1" })

        header = table.find_all('tr')[:1]
        keys = []

        for row in header:
            values = row.find_all(text=True)

            items = values[1:6]
            for i, value in enumerate(items):
                value = value.encode("utf-8")
                keys.append(value.lower())
            #print keys

        rows = table.find_all('tr')[1:]
        for row in rows:
            values = row.find_all(text=True)
            
            items = values[1:6]
            #print items
            flights = {}
            for i, value in enumerate(items):
                value = value.encode("utf-8")
                value = value.replace(",","")
                if value.isdigit() == True:
                    value = int(value)
                #print keys[i]
                #print value
                if keys[i] == "domestic" or keys[i] == "international":
                    #print "Found flights!"
                    flights[keys[i]] = value
                    #print flights
                    if len(flights) == 2:
                        info["flights"] = flights
                else:
                    info[keys[i]] = value

            #print info
            if info["month"] != "TOTAL":
                data.append(dict(info))

            #data.pop(len(data)-1)

    return data


def test():
    print "Running a simple test..."
    #open_zip(datadir)
    files = process_all(datadir)
    data = []
    for f in files:
        data += process_file(f)

    
    print data
    assert len(data) == 3
    for entry in data[:3]:
        #print entry["flights"]["domestic"]
        assert type(entry["year"]) == int
        assert type(entry["flights"]["domestic"]) == int
        assert len(entry["airport"]) == 3
        assert len(entry["courier"]) == 2
    print "... success!"

if __name__ == "__main__":
    test()
