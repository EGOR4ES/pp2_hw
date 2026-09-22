# Here is the first example: a class with two parents
class Flyer:
    #first parent it can fly.
    def fly(self):
        print("I can fly!")

class Swimmer:
    #second parent it can swim
    def swim(self):
        print("I can swim!")

class Duck(Flyer, Swimmer):
    #child class that gets methods from both parents.
    pass

donald = Duck()
donald.fly()
donald.swim()


# Here is the second example: a child of a father and a mother
class Father:
    def __init__(self):
        self.eye_color = "brown"

    def play_football(self):
        print("Playing football")

class Mother:
    def cook(self):
        print("Cooking dinner")

class Child(Father, Mother):
    #child class that has skills of both parents
    def __init__(self):
        super().__init__()  # Here is the call of the Father constructor

kid = Child()
print("Eye color:", kid.eye_color)
kid.play_football()
kid.cook()


# Here is the third example: the same method name in both parents
class A:
    def say(self):
        print("Hello from A")

class B:
    def say(self):
        print("Hello from B")

class C(A, B):
    #class where A is first, so A wins
    pass

C().say()
print("Method Resolution Order:", [cls.__name__ for cls in C.__mro__])


# Here is the fourth example: a smartphone that is a phone and a camera
class Phone:
    def call(self, number):
        print("Calling", number)

class Camera:
    def take_photo(self):
        print("Click! Photo taken")

class Smartphone(Phone, Camera):
    #child class that combines two devices
    def open_browser(self):
        print("Opening the browser")

my_phone = Smartphone()
my_phone.call("+7 777 123 4567")
my_phone.take_photo()
my_phone.open_browser()
