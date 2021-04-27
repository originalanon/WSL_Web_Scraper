import Company

class CruiseStats(Company):
     def __init__(self, companyName, year,totalPassengers, percentOfPassengers, revenue, percentOfRevenue ):
         companyName=Company
         self.name=companyName
         self.year=year
         self.passenger=totalPassengers
         self.people_percent=percentOfPassengers
         self.revenue=revenue
         self.cash_percent=percentOfRevenue


m=Company("Spoon","dell")
stats=CruiseStats(n, 2021, 9, 100, -500, -100)
print(stats.name)