from tableauscraper import TableauScraper as TS

url = "https://cruisemarketwatch.com/market-share/"
ts = TS()
ts.loads(url)
spreadSheet = ts.getWorkbook()
print(spreadSheet.data)
