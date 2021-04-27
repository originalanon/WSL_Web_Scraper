import sys as sys
import requests
import pandas as pd
from bs4 import BeautifulSoup
from tableauscraper import TableauScraper as TS
from csvFunctions import csvHeadersInsert as csvHeaders

CSV_EXPORT_FILE = "CruiseData.csv"
url = "https://cruisemarketwatch.com/market-share/"

csvHeaders(CSV_EXPORT_FILE)

ts = TS()
ts.loads(url)
spreadSheet = ts.getWorksheet("Details")

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

sys.stdout = open("SpreadsheetInfoFirst.csv", "w")
print(spreadSheet.data)
sys.stdout.close()

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
