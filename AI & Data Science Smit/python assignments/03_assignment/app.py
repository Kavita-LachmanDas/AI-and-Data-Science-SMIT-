class Vehicle:
    def __init__(self,brand,year,mileage):
        self.brand = brand
        self.year = year
        self.mileage = mileage


    def drive(self,mileage):
        self.mileage += mileage
        

    def describe(self):
            print(f"Vehicle Details:")
            print(f"- Brand: {self.brand}")
            print(f"- Manufacturing Year: {self.year}")
            print(f"- Current Mileage: {self.mileage} km")   


car = Vehicle("Toyota", 2020, 10000)
car.drive(500)  # Adds 500 miles
car.describe()
