#first example: a class variable is shared by all objects
class Cat:
    #class with one class variable and one instance variable.
    species = "Felis catus"  # Here the class variable

    def __init__(self, name):
        self.name = name  # Here is the instance variable

tom = Cat("Tom")
kitty = Cat("Kitty")
print(tom.name, "and", kitty.name, "are both", tom.species)


#second example: instance variables are different for each object
print("Names are different:", tom.name, "!=", kitty.name)


#third example: changing the class variable changes it for all objects
Cat.species = "Domestic cat"
print(tom.species)
print(kitty.species)


#fourth example: changing an instance variable changes only one object
tom.name = "Big Tom"
print(tom.name)    # Here changed name
print(kitty.name)  # Here is the name that did not change


#fifth example: using a class variable as a counter
class Student:
    #class that counts how many students were created.
    total_students = 0

    def __init__(self, name):
        self.name = name
        Student.total_students += 1  # Here is where the counter goes up

Student("Ali")
Student("Sara")
Student("Dana")
print("Total students created:", Student.total_students)
