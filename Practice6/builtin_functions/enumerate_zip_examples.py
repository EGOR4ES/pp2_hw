"""
Using enumerate() and zip() for paired iteration
"""

fruits = ["apple", "banana", "cherry"]

# Here is enumerate() - it gives me both the index AND the value in a loop
print("--- enumerate() ---")
for index, fruit in enumerate(fruits):
    print(index, "->", fruit)

# Here is enumerate() starting the counting from 1 instead of 0
print("--- enumerate() starting at 1 ---")
for position, fruit in enumerate(fruits, start=1):
    print("Fruit number", position, "is", fruit)


# Here is zip() - it combines two (or more) lists together, pair by pair
names = ["Ali", "Sara", "Dana"]
ages = [19, 20, 21]

print("--- zip() with two lists ---")
for name, age in zip(names, ages):
    print(name, "is", age, "years old")


# Here is zip() with THREE lists at once
cities = ["Almaty", "Astana", "Shymkent"]
print("--- zip() with three lists ---")
for name, age, city in zip(names, ages, cities):
    print(name, "-", age, "-", city)


# Here is turning a zip into a dictionary (a very common trick)
name_to_age = dict(zip(names, ages))
print("Dictionary made from zip:", name_to_age)


# Here is combining enumerate() and zip() together
print("--- enumerate() + zip() together ---")
for index, (name, age) in enumerate(zip(names, ages)):
    print("Record", index, ":", name, "-", age)
