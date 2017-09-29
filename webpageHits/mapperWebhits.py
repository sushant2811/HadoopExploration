#!/usr/bin/python

# Format of each line is:
# IP_address client_identity client_username time request_line status_code size_of_the_object 
#
# For the first part where we want the number of hits for each different page, we wanna 
# work with the request_line entry

import sys

IP = '10.99.99.186'

for line in sys.stdin:
    data = line.strip().split()
    
    if len(data) == 10:
	if data[0] == IP:
           print "{0}\t{1}".format(IP, 1)
	else:
	   print "{0}\t{1}".format(IP, 0)	
