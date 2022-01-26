

class Cars:

    def __init__(self, make, model, color, package, top_speed):
        self.make = make
        self.model = model
        self.color = color
        self.package = package
        self.top_speed = top_speed

    def speed(self):
        if self.top_speed < 160:
            print("This car is fast")

class Car_Inventory:
    def __init__(self, make, max_cars):
        self.make = make 
        self.max_cars = max_cars
        self.inventory = []

    def add_car(self, make):
        if len(self.inventory) < self.max_cars:
            self.inventory.append(make)
            return make
