# Here is the first example: children change the method of the parent
class Animal:
    #parent class with a general sound.
    def make_sound(self):
        print("Some animal sound")

class Dog(Animal):
   #child class that overrides make_sound.
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    #child class that overrides make_sound.
    def make_sound(self):
        print("Meow!")

Animal().make_sound()
Dog().make_sound()
Cat().make_sound()


# Here is the second example: overriding a method that returns a value
class Shape:
    #parent class for shapes.
    def get_area(self):
        return 0

class Square(Shape):
    #child class that calculates its own area.
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side * self.side

class Circle(Shape):
    #child class with a different formula.
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2

shapes = [Shape(), Square(4), Circle(3)]
for shape in shapes:
    print(type(shape).__name__, "area:", shape.get_area())


# Here is the third example: overriding and using super() together
class Employee:
    #parent class with a salary calculation.
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def get_salary(self):
        return self.base_salary

class Manager(Employee):
    #child class that adds a bonus to the parent salary.
    def get_salary(self):
        return super().get_salary() + 50000  # Here is the parent value plus bonus

worker = Employee("Ali", 200000)
boss = Manager("Dana", 300000)
print(worker.name, "gets", worker.get_salary())
print(boss.name, "gets", boss.get_salary())


# Here is the fourth example: overriding the __str__ method
class Person:
    #class where I override the built-in __str__ method.
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Person: " + self.name

class Student(Person):
    #child class with its own __str__.
    def __str__(self):
        return "Student: " + self.name

print(Person("Timur"))
print(Student("Aruzhan"))
