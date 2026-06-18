class Student:
    def __init__(self, first_name, last_name, age,):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def print_properties(self):
        print(f"fullname: {self.first_name} {self.last_name}") 
        


student1 = Student(first_name="John", last_name="Doe", age=20)
student2 = Student(first_name="Jane", last_name="Smith", age=22)

print(student1.first_name)
print(student1.last_name)
print(student1.age)

print("----------------")

print(student2.first_name)
print(student2.last_name)
print(student2.age)

print("----------------")

student1.print_properties()
print("----------------")
student2.print_properties()