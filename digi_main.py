#------------------------------------------------------------------------------
# INFO:
# This is the main file that runs the entire script, using functions from other
# files. 
# 
#------------------------------------------------------------------------------#

# application specific functions
import large_table.py
import textfile_parser
import digi_plot
import digi_pullnsave

# other third party libraries
import requests
from bs4 import BeautifulSoup
import time
import schedule
import numpy as numpy

#-------------------------------------------------------------------------------
# construct_initial_table()
# if a text file doesnt exist with the name 'digi_tingz.txt' then run this function
#------------------------------------------------------------------------------#

if True:
	req = RequestClass(0)
	page_array = PagePullArrays()
	init_pull(req, page_array)

#-------------------------------------------------------------------------------
# 
#------------------------------------------------------------------------------#
