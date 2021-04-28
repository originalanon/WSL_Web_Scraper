import sys as sys
import requests
import pandas as pd
import string as str
from bs4 import BeautifulSoup
from tableauscraper import TableauScraper as TS
import csvFunctions as cf
import numpy as np
from CruiseStats import CruiseStats

statsList = []

url = "https://cruisemarketwatch.com/market-share/"

ts = TS()
ts.loads(url)
spreadSheet = ts.getWorksheet("Details")

spreadSheet.data[['Brand-value', 'Parent-value','Measure Names-alias', 'Measure Values-alias']].to_csv("./SpreadsheetInfoFirst.csv", header=False, index=False)


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

brandValueColumn = spreadSheet.data.loc[:, 'Brand-value']
print(brandValueColumn)


parentValueColumn = spreadSheet.data.loc[:, 'Parent-value']
print(parentValueColumn)

measureNameAliasColumn = spreadSheet.data.loc[:, 'Measure Names-alias']
print(measureNameAliasColumn)

measureValueAliasColumn = spreadSheet.data.loc[:, 'Measure Values-alias']
print(measureValueAliasColumn)

cf.organizeSpreadsheetInfo("./SpreadsheetInfoFirst.csv", "./CruiseData.csv")

for x in range(len(measureNameAliasColumn)):
    statsList.append(CruiseStats())

    statsList[x].setName(brandValueColumn[x])
    statsList[x].setParentCompany(parentValueColumn[x])

    if(measureNameAliasColumn[x] == "Total Passengers"):
        statsList[x].setTotalPassengers(measureValueAliasColumn[x])
    elif(measureNameAliasColumn[x] == "Revenue"):
        statsList[x].setRevenue(measureValueAliasColumn[x])
    elif(measureNameAliasColumn[x] == "% of Revenue"):
        statsList[x].setPercentOfRevenue(measureValueAliasColumn[x])
    elif(measureNameAliasColumn[x] == "% of Passengers"):
        statsList[x].setPercentOfPassengers(measureValueAliasColumn[x])

    statsList[x].printStatistic()


page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
