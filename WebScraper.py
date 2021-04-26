import sys as sys
import requests
import pandas as pd
from bs4 import BeautifulSoup
from tableauscraper import TableauScraper as TS


url = "https://cruisemarketwatch.com/market-share/"

ts = TS()
ts.loads(url)
spreadSheet = ts.getWorksheet("Details")

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

sys.stdout = open("SpreadsheetInfoFirst.txt", "w")
print(spreadSheet.data)
sys.stdout.close()



#soup = BeautifulSoup(page.content, 'html.parser')
