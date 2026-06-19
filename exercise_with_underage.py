class Person:
    

    def __init__(self, full_name, age):
        self.full_name = full_name
        self.age = age
        
        if self.age >= 18:
            self.category = "Adult"
        else:
            self.category = "Underage"

    def get_details(self):
        print(f"Fullname: {self.full_name}")
        print(f"Age: {self.age}")
        print(f"Category: {self.category}")

    def get_age(self):
        print(f"Age: {self.age}")

number_of_people = 2

persons = []
for i in range(number_of_people):
     full_name = input("Enter your full name: ")
     age = int(input("Enter your age: "))

     person = Person(full_name, age)

     #add person to the list
     persons.append(person)


for person in persons:
    print("----------------")
    person.get_details()
   