class Vehicle:
    def __init__(self, max_speed, mileage):
     self.max_speed=max_speed
     self.mileage=mileage
car=Vehicle(200,40)
truck=Vehicle(240,60)
print(car.max_speed, car.mileage)
print(truck.max_speed, truck.mileage)
