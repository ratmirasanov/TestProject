"""Some test project for working with CSV-files."""

import csv
import sys


# Reading CSV-file to list of lists.
EXAMPLE_FILE = open("Badprice.csv", "rU")
EXAMPLE_READER = csv.reader(EXAMPLE_FILE)
EXAMPLE_DATA = list(EXAMPLE_READER)

# Declaration of variables.
MAX_VALUE = 0
MIN_VALUE = sys.float_info.max
MAX_INDEX = ""
MIN_INDEX = ""
AVG_PRICE = 0
AVG_SQUARE_FOOTAGE = 0
COUNT_PRICE = 0
COUNT_SQUARE_FOOTAGE = 0

# Creation of two lists.
for row in EXAMPLE_DATA:

    if row[9].isalpha():

        continue

    else:

        if float(row[9]) > 0 and float(row[6]) > 0:

            AVG_PRICE += float(row[9])
            AVG_SQUARE_FOOTAGE += float(row[6])
            COUNT_PRICE += 1
            COUNT_SQUARE_FOOTAGE += 1

            if MAX_VALUE < float(row[9]):

                MAX_VALUE = float(row[9])
                MAX_INDEX = row

            if MIN_VALUE > float(row[9]):

                MIN_VALUE = float(row[9])
                MIN_INDEX = row

# Printing results.
print("Max price of real estate -- " + str(MAX_INDEX) + " is: " + str(MAX_VALUE) + "$.")
print("Min price of real estate -- " + str(MIN_INDEX) + " is: " + str(MIN_VALUE) + "$.")
print("Average square footage is -- " + str(AVG_SQUARE_FOOTAGE / COUNT_SQUARE_FOOTAGE))
print("Average price is -- $" + str(AVG_PRICE / COUNT_PRICE))
