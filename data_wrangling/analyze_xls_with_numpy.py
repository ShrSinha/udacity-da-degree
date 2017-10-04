"""Parse the Excel file.

Args:
    datafile: Excel file.

Returns:
    - min, max and average values for the COAST region
    - time value for the min and max entries. They should be returned as Python tuples.

"""
import pprint
import xlrd
import numpy as np
from zipfile import ZipFile

datafile = "2013_ERCOT_Hourly_Load_Data.xls"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    #read the provided Excel file
    sheet_data = [ [sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
    #sheet.nrows includes header record in row count.

    #find and return the min, max and average values for the COAST region
    for c in range(len(sheet_data[0])):
        if sheet_data[0][c] == 'COAST':
            coast_data = np.array( sheet.col_values(c, start_rowx=1, end_rowx=None) )
            maxvalue = np.max(coast_data)
            minvalue = np.min(coast_data)
            avgcoast = np.mean(coast_data) 

    row_maxvalue = int(np.where(coast_data == maxvalue)[0]) + 1
    row_minvalue = int(np.where(coast_data == minvalue)[0]) + 1            
            
    #find and return the time value for the min and max entries   
    for c in range(len(sheet_data[0])):
        if sheet_data[0][c] == 'Hour_End':
            mintime = xlrd.xldate_as_tuple(sheet_data[row_minvalue][c], 0)
            maxtime = xlrd.xldate_as_tuple(sheet_data[row_maxvalue][c], 0)

    ### other useful methods:
    # print "\nROWS, COLUMNS, and CELLS:"
    # print "Number of rows in the sheet:", 
    # print sheet.nrows
    # print "Type of data in cell (row 3, col 2):", 
    # print sheet.cell_type(3, 2)
    # print "Value in cell (row 3, col 2):", 
    # print sheet.cell_value(3, 2)
    # print "Get a slice of values in column 3, from rows 1-3:"
    # print sheet.col_values(3, start_rowx=1, end_rowx=4)

    # print "\nDATES:"
    # print "Type of data in cell (row 1, col 0):", 
    # print sheet.cell_type(1, 0)
    # exceltime = sheet.cell_value(1, 0)
    # print "Time in Excel format:",
    # print exceltime
    # print "Convert time to a Python datetime tuple, from the Excel float:",
    # print xlrd.xldate_as_tuple(exceltime, 0)

    data = {
            'maxtime': maxtime,
            'maxvalue': maxvalue,
            'mintime': mintime,
            'minvalue': minvalue,
            'avgcoast': avgcoast
    }
    return data


def test():
    open_zip(datafile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()