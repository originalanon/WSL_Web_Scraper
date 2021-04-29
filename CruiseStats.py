class CruiseStats():

    def __init_(self, name = "", parentCompany = "" ,totalPassengers = "", percentOfPassengers = "", revenue = "", percentOfRevenue = "" ):
        self.name=name
        self.parentCompany=parentCompany
        self.totalPassengers=totalPassengers
        self.percentOfPassengers=percentOfPassengers
        self.revenue=revenue
        self.percentOfRevenue=percentOfRevenue

    def setName(self,x):
        self.name=x
    def setParentCompany(self,x):
        self.parentCompany=x
    def setTotalPassengers(self,x):
        self.totalPassengers=x
    def setPercentOfPassengers(self,x):
        percent = x.split("%", 1)
        self.percentOfPassengers = percent[0]
    def setRevenue(self,x):
        revenue = x.split("$", 1)
        self.revenue = revenue[1]
    def setPercentOfRevenue(self,x):
        percent = x.split("%", 1)
        self.percentOfRevenue = percent[0]

    def getPassengers(self):
        return self.totalPassengers

    def printStatistic(self):
        print(str(self.name + ', ' + self.parentCompany +', '
        +self.setPercentOfPassengers +', '+self.revenue+ ', ' +self.percentOfRevenue))
                
