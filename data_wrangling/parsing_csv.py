"""Parse the first 10 data lines.

Args:
    datafile: csv file.

Returns:
    Dictionary where the key is the header title of the field, and the value is the value of that field in the row.

"""

import os

DATADIR = ""
DATAFILE = "beatles-diskography.csv"

def parse_file(datafile):
    
    data = []
    counter = 0 
    
    with open(datafile,"r") as f:
        header = f.readline().split(",")

        for line in f:
            if counter == 10:
                break
            data.append( { header[i].strip() : v.strip() for i,v in list(enumerate(line.split(","))) } )
            counter += 1    

        return(data)


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline


test()

    