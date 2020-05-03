#!/usr/bin/env python
# -*- coding: utf-8 -*-
# So, the problem is that the gigantic file is actually not a valid XML, because
# it has several root elements, and XML declarations.
# It is, a matter of fact, a collection of a lot of concatenated XML documents.
# So, one solution would be to split the file into separate documents,
# so that you can process the resulting files as valid XML documents.

import xml.etree.ElementTree as ET
PATENTS = 'patent.data'



##a = f.readline()
##
##file_name = "{}-{}".format(PATENTS, counter)
##
###with open(file_name, 'w') as w:
##    #w.write(a)
##
##test = 'patent.data-0'
##
##t = open(test, 'r')
##b = t.readline()
##print b



#print linenum
#print counter

#for n in range(4):
#    print n


def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()




def split_file(filename):
    # we want you to split the input file into separate files
    # each containing a single patent.
    # As a hint - each patent declaration starts with the same line that was causing the error
    # The new files should be saved with filename in the following format:
    # "{}-{}".format(filename, n) where n is a counter, starting from 0.

    counter = 0
    linenum = 0
    xmlfile = ""
    f = open(filename, 'r')

    for line in f:
        linenum += 1
        if line[:5] == "<?xml":
            #print line
            # create file name + counter
            file_name = "{}-{}".format(PATENTS, counter)
            print file_name
            counter += 1

            if linenum == 1:
                xmlfile += line

            else:
                with open(file_name, 'w') as w:
                    w.write(xmlfile)

        else:
            xmlfile += line

    with open(file_name, 'w') as w:
            w.write(xmlfile)


def test():
    split_file(PATENTS)
    for n in range(4):
        try:
            fname = "{}-{}".format(PATENTS, n)
            f = open(fname, "r")
            if not f.readline().startswith("<?xml"):
                print "You have not split the file {} in the correct boundary!".format(fname)
            f.close()
        except:
            print "Could not find file {}. Check if the filename is correct!".format(fname)


test()
