"""
class Rectangle:
    # l
    # b
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth


obj1 = Rectangle(length=30, breadth=60)

print(obj1.length) 
"""

class Vehicle:
    running = False

    def __init__(self, owner) -> None:
        self.owner = owner

    def is_running(self):
        if self.running:
            print(f"{self.owner}'s vehicle car is running")

        else:
            print(f"{self.owner}'s vehicle car is not running")