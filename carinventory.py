from Cars import Cars
from Cars import Car_Inventory



car1 = Cars("BMW", "7 Series", "Grey", "Deluxe", 180)
car2 = Cars("Mercedes", "G Wagon", "Black", "Premium", 150)
car6 = Cars ("Porsche", "911", "Red", "Premium", 200)

'''
car3 = Car_Inventory("Suburu", 3)
car3.add_car(car3)
print(car3.inventory[0].make)

car4 = Car_Inventory("Honda", 3)
car4.add_car(car4)
print(car4.inventory[0].make)

car5 = Car_Inventory("Camry", 3)
car5.add_car(car5)
print(car5.inventory[0].make)
'''

cars = Car_Inventory("New Inventory", 3)
cars.add_car(car1)
cars.add_car(car2)
cars.add_car(car6)


print(cars.inventory[2].make)
