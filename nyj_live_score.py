#!/usr/bin/env python

""" Simple script that gets the New York Jets schedule and scores of a season from NFL.com """

import sys
import urllib2
from xml.etree import ElementTree

#Season Scores
url_2 = 'http://www.nfl.com/ajax/scorestrip?season=%d&seasonType=REG&week=%d'

def main(year):
    for y in [year,]:
        for i in range(1,18):
            f 			= urllib2.urlopen(url_2 % (y,i))
            tree 		= ElementTree.parse(f)
            f.close()
            for node in tree.iter('g'):
                date 	=  node.attrib.get('eid')
                weekday =  node.attrib.get('d')
                time	=  node.attrib.get('t')
                h 		=  node.attrib.get('h')
                v 		=  node.attrib.get('v')
                hs 		=  node.attrib.get('hs')
                vs 		=  node.attrib.get('vs')
                if (v) == 'NYJ'or (h) == 'NYJ':
                    print v,vs,h,hs,weekday,"%s/%s/%s" % (date[4:6],date[6:8],date[:4]),time

if __name__ == "__main__":
    main(int(sys.argv[1]))