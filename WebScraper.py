from tableauscraper import TableauScraper as TS

url = "https://cruisemarketwatch.com/market-share/"

ts = TS()
ts.loads(url)

spreadSheet = ts.getWorksheet("Details") #the tableau test-id of the second worksheet
print(spreadSheet.data)