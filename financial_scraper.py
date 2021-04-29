# Michael J. Franco, Jr.
# Dell 2021 High C's
# April 28, 2021
#
# Scraper tool for retrieving data from the 2020 Annual
# Report 10-K for Royal Caribbean Cruises as shown on
# the website https://sec.report/ by scraping the data
# from the HTML code.

import requests
import urllib.request
import time
import pandas as pd
from bs4 import BeautifulSoup
import pickle
import re

# Set the URL for collecting the data.
url = 'https://sec.report/Document/0000884887-21-000006/'

page_response = requests.get(url)

# The BeautifulSoup code for the page response
page_soup = BeautifulSoup(page_response.text, 'html.parser')
