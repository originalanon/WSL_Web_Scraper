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
        self.percentOfPassengers=x
    def setRevenue(self,x):
        self.revenue=x    
    def setPercentOfRevenue(self,x):
        self.percentOfRevenue=x

    def getPassengers(self):
        return self.totalPassengers

    def printStatistic(self):
        print(str(self.name + ', ' + self.parentCompany +', '
        +self.setPercentOfPassengers +', '+self.revenue+ ', ' +self.percentOfRevenue))
                
