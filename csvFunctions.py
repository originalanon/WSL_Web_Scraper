import sys as sys

def csvHeadersInsert(file):
    sys.stdout = open(file, "w")
    print("Parent Company, Brand, Total Passengers, % of Passengers, Revenue, % of Revenue, Average Stock Value")
    sys.stdout.close()

