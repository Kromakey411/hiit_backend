class Car:

    def __init__(self, color, brand, max_speed, year):
        self.color = color
        self.brand = brand
        self.max_speed = max_speed
        self.year = year

    def print_properties(self):
        print(f"Color: {self.color}")
        print(f"Brand: {self.brand}")
        print(f"Maximum Speed: {self.max_speed}")
        print(f"Year: {self.year}")

    def get_color(self):
        return self.color

my_car1 = Car(color="Red", brand="Lexus", max_speed="200 km/hr", year=2020)

my_car2 = Car(color="Blue", brand="Toyota", max_speed="180 km/hr", year=2019)

my_car1.print_properties()
print("----------------")
my_car2.print_properties()

print (my_car1.get_color())
print (my_car2.get_color())