#first example: a class with a method that uses self
class Dog:
    #class for a dog with a bark method.
    def __init__(self, name):
        self.name = name

    def bark(self):
        #method that prints the barking of this dog.
        print(self.name, "says Woof!")

rex = Dog("Rex")
rex.bark()


#second example: methods that change the object data
class BankAccount:
    #class for a simple bank account.
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        #method that adds money to the balance.
        self.balance = self.balance + amount

    def withdraw(self, amount):
        #method that takes money if there is enough.
        if amount > self.balance:
            print("Not enough money!")
        else:
            self.balance = self.balance - amount

    def show_balance(self):
        #method that prints the current balance.
        print(self.owner, "has", self.balance, "tenge")

account = BankAccount("Dana", 1000)
account.deposit(500)
account.withdraw(200)
account.show_balance()
account.withdraw(5000)


#third example: a method that returns a value
class Circle:
    #class for a circle.
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        #method that returns the area of the circle.
        return 3.14 * self.radius ** 2

small_circle = Circle(2)
print("Circle area:", small_circle.get_area())


#fourth example: one method calls another method with self
class Person:
    #class for a person who can have birthdays.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def have_birthday(self):
        #method that makes the person one year older.
        self.age = self.age + 1
        self.introduce()  # Here is the call of another method of the same object

    def introduce(self):
        #method that prints the name and age.
        print("Hi, I am", self.name, "and I am", self.age)

student = Person("Ali", 19)
student.introduce()
student.have_birthday()
