import sys as sys
import requests
import pandas as pd
import string as str
from bs4 import BeautifulSoup
from tableauscraper import TableauScraper as TS
import numpy as np

#Some pandas display options
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

#Export CSV Files -- This is the file the Cleaned Data is exported to
EXPORT_CSV_FILE = "Cruisedata.csv"

#Setting up the TableauScraper
url = "https://cruisemarketwatch.com/market-share/"

ts = TS()
ts.loads(url)
#Getting the worksheet labelled "Details"
spreadSheet = ts.getWorksheet("Details")

#Listing the individual columns to a CSV -- this'll make sense in a minute
spreadSheet.data[['Brand-value', 'Measure Names-alias', 'Measure Values-alias']].to_csv("./SpreadsheetInfoFirst.csv", header=False, index=False)

#Split the three columns each into seperate lists -- this only works if they're in a CSV already, so it should make sense now
brandValueColumn = spreadSheet.data.loc[:, 'Brand-value']
measureNameAliasColumn = spreadSheet.data.loc[:, 'Measure Names-alias']
measureValueAliasColumn = spreadSheet.data.loc[:, 'Measure Values-alias']

#Arrays to use as columns from the data pulled from the Measure Values-alias list
revenueValueColumn = []
revenuePercentValueColumn = []
totalPassengersValueColumn = []
passengersPercentValueColumn = []



#Check what's being measured, then assign the value following it to that measure's array/list/whatever Python calls them
for x in range(len(measureNameAliasColumn)):
    if(measureNameAliasColumn[x] == "Total Passengers"):
        totalPassengersValueColumn.append(measureValueAliasColumn[x])
        measureValueAliasColumn[x].replace(",", "")
    elif(measureNameAliasColumn[x] == "Revenue"):
        measureValueAliasColumn[x].replace(",", "")
        revenueValueColumn.append(measureValueAliasColumn[x])
    elif(measureNameAliasColumn[x] == "% of Revenue"):
        revenuePercentValueColumn.append(measureValueAliasColumn[x])
    elif(measureNameAliasColumn[x] == "% of Passengers"):
        passengersPercentValueColumn.append(measureValueAliasColumn[x])

#Writing to export file
writeFile = open(EXPORT_CSV_FILE, "w")
writeFile.write("Brand, Total Passengers, % of Passengers, Revenue, % of Revenue\n") #Headers

for x in range(len(totalPassengersValueColumn)):
    writeFile.write(totalPassengersValueColumn[x].replace(",", "") + ", "
                    + passengersPercentValueColumn[x].replace("%", "") + ", "
                    + revenueValueColumn[x].replace(",", "").replace("$","")+ ", "
                    + revenuePercentValueColumn[x].replace("%", "") + "\n")

#BeautifulSoup stuff
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
