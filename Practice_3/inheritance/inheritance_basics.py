# Here is the first example: a child class gets everything from the parent class
class Animal:
    #class for all animals.
    def __init__(self, name):
        self.name = name

    def eat(self):
        #method that all animals have.
        print(self.name, "is eating")

class Dog(Animal):
    #child class it has everything that Animal has.
    pass

rex = Dog("Rex")
rex.eat()  # Here is a method that Dog got from Animal


# Here is the second example: a child class with its own new method
class Cat(Animal):
    #child class with a new method.
    def purr(self):
        #method that only cats have.
        print(self.name, "says purr")

tom = Cat("Tom")
tom.eat()
tom.purr()


# Here is the third example: two children of one parent
class Person:
    #parent class for people.
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        # method that prints hello.
        print("Hello, my name is", self.name)

class Student(Person):
    # child class for students.
    def study(self):
        print(self.name, "is studying Python")

class Teacher(Person):
    #child class for teachers.
    def teach(self):
        print(self.name, "is teaching a lesson")

Student("Ali").say_hello()
Student("Ali").study()
Teacher("Aigul").say_hello()
Teacher("Aigul").teach()


# Here is the fourth example: checking the relationships between classes
print("Is rex a Dog?", isinstance(rex, Dog))
print("Is rex an Animal?", isinstance(rex, Animal))
print("Is Dog a subclass of Animal?", issubclass(Dog, Animal))
print("Is Cat a subclass of Dog?", issubclass(Cat, Dog))
