import requests
from bs4 import BeautifulSoup
import time
import schedule
import numpy as numpy

#-------------------------
#   FUNCTION DEFINITIONS
#------------------------#

# prints all the ahref links on the page in a column in console
def print_all_links_in_page():
    for link in soup.find_all("a"):
        print(link.get("href"))

def print_all_link_text_in_page():
    for link in soup.find_all("a"):
        print(link.text)

def print_links():
    for link in soup.find_all("a"):
        print(link.text, link.get("href"))

def html_format_links():
    for link in soup.find_all("a"):
        print("<a href='%s'>%s</a>" %(link.get("href"), link.text))

def get_div_stuff():
    g_data = soup.find_all("div", {"class" : "mid-wrapper"}) #a list
    for item in g_data:
        print(item.text, item.get("class")) #gets the text written in that class
        print(item.contents)

def get_item_stuff():
    all_items_on_page = soup.find_all("tr", {"itemtype" : "http://schema.org/Product"})
    for item in all_items_on_page:
        page_temp_vendor.append(soup.find("td", {"class" : "tr-vendor"}).text)
        page_temp_mpn.append(soup.find("td", {"class" : "tr-mfgPartNumber"}).text)
        page_temp_value.append(soup.find("td", {"class" : "CLS 2049 ptable-param"}).text)
        page_temp_tolerance.append(soup.find("td", {"class" : "CLS 3 ptable-param"}).text)
        page_temp_voltage.append(soup.find("td", {"class" : "CLS 14 ptable-param"}).text)
        page_temp_quantity.append(soup.find("td", {"class" : "tr-qtyAvailable"}).text)
        page_temp_price.append(soup.find("td", {"class" : "tr-unitPrice ptable-param"}).text)
    print("One page done.")



#-------------------------
#   MAIN CODE
#------------------------#

page_temp_vendor = []
page_temp_mpn = []
page_temp_value = []
page_temp_tolerance = []
page_temp_voltage = []
page_temp_quantity = []
page_temp_price = []
all_data = []
main_url = 'https://www.digikey.co.uk/products/en/capacitors/ceramic-capacitors/60'
payload = {'ColumnSort' : '0', 'page' : '1', 'rohs' : '1', 'pageSize' : '500', 'pv1989' : '0', 'pv69' : '453', 'pv16':'4'}
r = requests.get(main_url, params = payload)
print("Got request. ")
print(r.status_code)
print(r.url)
print(r.encoding)

# requests.content can display all the HTML text from the webpage. However, dont use this directly
# because this will crash this program.... too many lines
# beatifulsoup4 helps us to make the HTML into a more readable format.

soup = BeautifulSoup(r.content, 'html.parser') #conversion into something useable
print("Content taken from digikey")
# print(soup.prettify)

get_item_stuff()



