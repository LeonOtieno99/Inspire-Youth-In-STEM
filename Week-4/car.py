class car:
    def __init__(self,model,make,year,engineCapacity):
        self.model = model
        self.make = make
        self.year = year
        self.engineCapacity = engineCapacity
#getters
    def get_model(self):
        return self.model

    def get_make(self):
        return self.make
            
    def get_year(self):
        return self.year

    def get_engineCapacity(self):
        return self.engineCapacity

#settters
    def set_model(self,model):
        self.model = model

    def set_make(self,make):
        self.make = make

    def set_year(self,year):
        self.year = year

car1 = car("demio","nissan",2018,1300)
car2 = car("hilux","toyota",2020,3501)
car3 = car("passat","vw",2019,1100)

car3.set_year(2023)
car1.set_year(2026)

print(car1.get_model())
print(car1.get_year())

print(car2.get_model())
print(car3.get_year())

print(car1.get_year())
print(car3.get_year())

        
