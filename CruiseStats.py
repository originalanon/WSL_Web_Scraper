import Company

class CruiseStats(Company):
     def __init__(self, year,totalPassengers, percentOfPassengers, revenue, percentOfRevenue ):
        
        Company.__init__(self,name,parentCompany)
    
        self.year=year
        self.passenger=totalPassengers
        self.people_percent=percentOfPassengers
        self.revenue=revenue
        self.cash_percent=percentOfRevenue


m=Company("Spoon","dell")
stats=CruiseStats( 2021, 9, 100, -500, -100)
print(stats.name)