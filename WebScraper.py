import sys as sys
import requests
import pandas as pd
import pandas_profiling
import string as str
from bs4 import BeautifulSoup
from tableauscraper import TableauScraper as TS
import csvFunctions as cf


url = "https://cruisemarketwatch.com/market-share/"

ts = TS()
ts.loads(url)
spreadSheet = ts.getWorksheet("Details")

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

cf.organizeSpreadsheetInfo("./SpreadsheetInfoFirst.csv")

#adding cleaning
cruise_info=pd.read_csv("./SpreadsheetInfoFirst.csv", encoding= 'latin1')
cruise_info=cruise_info.drop(["Brand-alias", "Parent-alias","Measure Names-value"],axis=1)
cruise_info=cruise_info.drop_duplicates(inplace=True,subset="title")
cruise_info.columns=["Parent Company", "Brand", "Total Passengers", "% of Passengers", "Revenue", "% of Revenue", "Average Stock Value"]

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
