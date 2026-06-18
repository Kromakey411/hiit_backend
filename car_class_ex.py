class Car:
    color = "Red"
    brand = "Lexus"
    max_speed = "200 km/hr"

    def __init__(self, color, brand, max_speed, year):
        self.color = color
        self.brand = brand
        self.max_speed = max_speed
        self.year = year
 

my_car1 = Car("Red", "Lexus", "200 km/hr", 2020)
my_car2 = Car("Blue", "Toyota", "180 km/hr", 2019)
print(my_car1.color)
print(my_car1.brand)
print(my_car1.max_speed)
print(my_car1.year)

print("----------------")
print(my_car2.color)
print(my_car2.brand)
print(my_car2.max_speed)
print(my_car2.year)