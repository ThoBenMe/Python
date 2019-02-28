#!/usr/bin/env python
# This program will demonstrate the use of the global namespace

count = 0	# global variable

def show_count():
	print("count = ", count)
	
def set_count(c):
	global count	# calls the global variable count
	count = c		# and updates the value to c
	
""" 
def set_count(c):
	count = c      <-- this would be incorrect, because the local count will be set to the value of c while 
					   the global count remains the same. 
"""