#!/usr/bin/python

# Format of each line is:
# date \t time \t store_name \t item_description \t cost \t method_of_payment
#


import sys
from datetime import datetime

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
	
	weekday = datetime.strptime(date, "%Y-%m-%d").weekday()	

        print "{0}\t{1}".format(weekday, cost)
