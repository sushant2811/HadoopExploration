#!/usr/bin/python

# Format of each line is:
# IP_address client_identity client_username time request_line status_code size_of_the_object 
#
# For the first part where we want the number of hits for each different page, we wanna 
# work with the request_line entry

import sys

for line in sys.stdin:
    data = line.strip().split()
    
    if len(data) == 10:
        print "{0}\t{1}".format(data[6], 1)
