import random


class Car:
    def __init__(self , license_plate , maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
        self.traveled_distance = 0
    def accelerate(self, acceleration):
        self.current_speed += acceleration
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0
    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours
def race(cars):
    while True:
        is_finished = False
        for car in cars:
            car.accelerate (random.randint (-10, 15))
            car.drive(1)
            if car.travelled_distance >= 10000:
                is_finished = True
        if is_finished == True:
            break
    return cars

car1 = Car("ABC-123", 142)
car2 = Car("AKC-193", 160)
cars_global = [car1 , car2]
race(cars_global)