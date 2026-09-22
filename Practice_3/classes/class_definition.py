# Here is the first example: defining a simple class with properties
class Car:
    """Here is a simple class that describes a car."""
    brand = "Toyota"
    color = "white"

# Here is how I create an object (an instance) of the class
my_car = Car()
print("My car is", my_car.color, my_car.brand)


# Here is the second example: making several objects from one class
friend_car = Car()
friend_car.color = "black"  # Here is a change only for the friend's car
print("Friend's car color:", friend_car.color)
print("My car color is still:", my_car.color)


# Here is the third example: modifying an object property
my_car.color = "red"
print("I repainted my car, now it is", my_car.color)


# Here is the fourth example: deleting a property of an object
del my_car.color  # Here is where I delete the property from the object
print("Does my_car have its own color now?", "color" in my_car.__dict__)
print("But the class color is still there:", my_car.color)


# Here is the fifth example: deleting the whole object
del friend_car
try:
    print(friend_car)
except NameError:
    print("The object friend_car does not exist anymore")
