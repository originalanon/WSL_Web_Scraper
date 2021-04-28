import sys as sys
import re

def csvHeadersInsert(file):
    sys.stdout = open(file, "w")
    print("Parent Company, Brand, Total Passengers, % of Passengers, Revenue, % of Revenue, Average Stock Value")
    sys.stdout.close()

def organizeSpreadsheetInfo(importfile, exportfile):
    readFile = open(importfile, "r")
    writeFile = open(exportfile, "w")

    while True:
        line = readFile.readline()
        if not line:
            break


        writeFile.write(line)

        

    readFile.close()
    writeFile.close()