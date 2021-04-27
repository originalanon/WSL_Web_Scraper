import sys as sys
import re

def csvHeadersInsert(file):
    sys.stdout = open(file, "w")
    print("Parent Company, Brand, Total Passengers, % of Passengers, Revenue, % of Revenue, Average Stock Value")
    sys.stdout.close()

def organizeSpreadsheetInfo(file):
    csvFile = open(file, "r")
    while True:
        line = csvFile.readline()
        if not line:
            break

        line = line.replace(',', '\n', 7)

        print(line)
        

    csvFile.close()