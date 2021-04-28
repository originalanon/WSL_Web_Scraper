import sys as sys
import requests
import pandas as pd
import string as str
from bs4 import BeautifulSoup
from tableauscraper import TableauScraper as TS
import csvFunctions as cf


url = "https://cruisemarketwatch.com/market-share/"

ts = TS()
ts.loads(url)
spreadSheet = ts.getWorksheet("Details")

spreadSheet.data[['Brand-value', 'Parent-value','Measure Names-alias', 'Measure Values-alias']].to_csv("./SpreadsheetInfoFirst.csv", header=False, index=False)


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

cf.organizeSpreadsheetInfo("./SpreadsheetInfoFirst.csv", "./CruiseData.csv")

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
