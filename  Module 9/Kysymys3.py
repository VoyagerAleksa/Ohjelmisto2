class Car:
    def __init__(self , license_plate , maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self, acceleration):
        self.current_speed += acceleration
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0
    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

car = Car("ABC-123", 142)
#print(f"Initial distance: {car.travelled_distance} km")
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
car.current_speed = 60
car.drive(1.5)
#print(f"Current speed: {car.current_speed} km/h")
car.accelerate(-200)
#print(f"Current speed: {car.current_speed} km/h")
#print(f"Distance after driving 1.5 hours at 60 km/h: {car.travelled_distance} km")