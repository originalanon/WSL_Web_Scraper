class CruiseStats():
        def __init__(self, name, parentCompany,totalPassengers, percentOfPassengers, revenue, percentOfRevenue ):
        
                self.name=name
                self.parentCompany=parentCompany
                self.totalPassenger=totalPassengers
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

        def printStatistic(self):
                print(self.name + ', ' + self.parentCompany + ', '+ self.year + ', ' + self.totalPassengers+', '
                +self.setPercentOfPassengers +', '+self.revenue+ ', ' +self.percentOfRevenue)
                