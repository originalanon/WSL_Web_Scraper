import sys as sys
from tableauscraper import TableauScraper as TS

url = "https://cruisemarketwatch.com/market-share/"

ts = TS()
ts.loads(url)

spreadSheet = ts.getWorkbook() #the tableau test-id of the second worksheet

sys.stdout = open("SpreadsheetInfoFirst.txt", "w")
for t in spreadSheet.worksheets:
    print(t.data)
sys.stdout.close()