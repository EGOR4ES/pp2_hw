#first example: a class with an __init__ constructor
class Student:
    #class that stores a student name and age.
    def __init__(self, name, age):
        self.name = name
        self.age = age

first_student = Student("Aigerim", 19)
print(first_student.name, first_student.age)


#second example: __init__ with a default value
class Book:
    #class for a book, the pages have a default value.
    def __init__(self, title, author, pages=100):
        self.title = title
        self.author = author
        self.pages = pages

short_book = Book("Small Story", "Some Author")
long_book = Book("Big Story", "Other Author", 500)
print(short_book.title, "has", short_book.pages, "pages")
print(long_book.title, "has", long_book.pages, "pages")


#third example: calculating a new property inside __init__
class Rectangle:
    #class for a rectangle that calculates its own area.
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height  #value that calculated in the constructor

room = Rectangle(4, 5)
print("Room area:", room.area)


#fourth example: creating many objects with a loop
class Pet:
    #class for a pet with a name.
    def __init__(self, name):
        self.name = name

pet_names = ["Rex", "Luna", "Max"]
pets = []
for pet_name in pet_names:
    pets.append(Pet(pet_name))  # Here is where each object is created

for pet in pets:
    print("Pet:", pet.name)
