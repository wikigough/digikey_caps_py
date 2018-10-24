#------------------------------------------------------------------------------
# INFO:
# This file contains a function to initialise the files containing the tables with 
# Manufacturing part number, vendor etc. 
# If any new products are found, this file can also update the large file to 
# contain the new part numbers.
# 
#------------------------------------------------------------------------------#
import requests
from bs4 import BeautifulSoup
import time
import schedule
import numpy as numpy


class RequestClass:
	main_url = 'https://www.digikey.co.uk/products/en/capacitors/ceramic-capacitors/60'
	
	def __init__(self, pagenumber):
		self.payload = {'ColumnSort' : '0', 'page' : str(pagenumber), 'rohs' : '1', 'pageSize' : '500', 'pv1989' : '0', 'pv69' : '453', 'pv16':'4'}
		self.req = requests.get(main_url, params = self.payload)
		self.bsoup = BeautifulSoup(self.req.content, 'html.parser')
	

class PagePullArrays:
	def __init__(self):
		self.page_temp_vendor = []
		self.page_temp_mpn = []
		self.page_temp_value = []
		self.page_temp_tolerance = []
		self.page_temp_voltage = []
		self.page_temp_quantity = []
		self.page_temp_price = []

#-------------------------------------------------------------------------------
# INITIALISE THE LARGE TABLE - large data pull, new file
#------------------------------------------------------------------------------#

def init_pull(_RequestClass, _PagePullArrays):
	all_data = []
	get_item_stuff(_RequestClass, _PagePullArrays)
	
#-------------------------------------------------------------------------------
# Loop function to iterate through the data on digikey
#------------------------------------------------------------------------------#

def get_item_stuff(_RequestClass, _PagePullArrays):
    all_items_on_page = _RequestClass.bsoup.find_all("tr", {"itemtype" : "http://schema.org/Product"})
    for item in all_items_on_page:
        _PagePullArray.page_temp_vendor.append(soup.find("td", {"class" : "tr-vendor"}).text)
        _PagePullArray.page_temp_mpn.append(soup.find("td", {"class" : "tr-mfgPartNumber"}).text)
        _PagePullArray.page_temp_value.append(soup.find("td", {"class" : "CLS 2049 ptable-param"}).text)
        _PagePullArray.page_temp_tolerance.append(soup.find("td", {"class" : "CLS 3 ptable-param"}).text)
        _PagePullArray.page_temp_voltage.append(soup.find("td", {"class" : "CLS 14 ptable-param"}).text)
        _PagePullArray.page_temp_quantity.append(soup.find("td", {"class" : "tr-qtyAvailable"}).text)
        _PagePullArraypage_temp_price.append(soup.find("td", {"class" : "tr-unitPrice ptable-param"}).text)
    print("One page done.")
	
#-------------------------------------------------------------------------------
# Add new rows to the large table
#------------------------------------------------------------------------------#
def add_new_part():
	return 0
