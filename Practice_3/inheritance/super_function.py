# Here is the first example: using super() to call the parent __init__
class Person:
    #parent class with a name and an age
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    #child class that adds a university
    def __init__(self, name, age, university):
        super().__init__(name, age)  # Here is the call of the parent constructor
        self.university = university

student = Student("Aigerim", 19, "KBTU")
print(student.name, student.age, student.university)


# Here is the second example: super() with a shape
class Shape:
    #parent class for shapes
    def __init__(self, color):
        self.color = color

class Rectangle(Shape):
    #child class that adds width and height
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

box = Rectangle("blue", 3, 4)
print("The", box.color, "rectangle has area", box.get_area())


# Here is the third example: super() to call a parent method inside a child method
class Employee:
    #parent class for employees
    def __init__(self, name):
        self.name = name

    def describe(self):
        #method that returns a text about the employee
        return "Employee " + self.name

class Manager(Employee):
    #child class that extends the describe method
    def describe(self):
        parent_text = super().describe()  # Here is the parent method call
        return parent_text + " (manager)"

print(Manager("Dana").describe())


# Here is the fourth example: super() in a chain of three classes
class Vehicle:
    def __init__(self, speed):
        self.speed = speed

class Car(Vehicle):
    def __init__(self, speed, doors):
        super().__init__(speed)
        self.doors = doors

class SportsCar(Car):
    def __init__(self, speed, doors, turbo):
        super().__init__(speed, doors)  # Here is the call of the Car constructor
        self.turbo = turbo

ferrari = SportsCar(300, 2, True)
print("Speed:", ferrari.speed, "| Doors:", ferrari.doors, "| Turbo:", ferrari.turbo)
