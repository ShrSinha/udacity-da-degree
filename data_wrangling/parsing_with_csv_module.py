"""Parse the csv file.

Args:
    datafile: csv file.

Returns:
    Dictionary where the key is the header title of the field, and the value is the value of that field in the row.

"""
import os
import pprint
import csv

DATADIR = ""
DATAFILE = "beatles-diskography.csv"

def parse_csv(datafile):
    data = []
    with open(datafile, 'rb') as f:
        r = csv.DictReader(f)
        data = [line for line in r]
    return data        

datafile = os.path.join(DATADIR,DATAFILE)
d = parse_csv(datafile)
pprint.pprint(d)