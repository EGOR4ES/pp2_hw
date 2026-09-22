# Here is the first example: positional arguments (the order matters!)
def describe_pet(animal_type, pet_name):
    #function that shows information about a pet.
    print("I have a", animal_type, "and its name is", pet_name)

describe_pet("dog", "Rex")   # Here is the correct order
describe_pet("Rex", "dog")   # Here is the wrong order, the result is funny


# Here is the second example: default argument values
def power(number, exponent=2):
    #function that raises a number to a power (default is 2).
    return number ** exponent

print(power(5))      # Here is the call that uses the default exponent 2
print(power(2, 10))  # Here is the call where I give my own exponent


# Here is the third example: keyword arguments (order does not matter)
def create_profile(name, age, city):
    #function that prints a small user profile.
    print("Name:", name, "| Age:", age, "| City:", city)

create_profile(name="Aigerim", age=19, city="Almaty")
create_profile(city="Astana", name="Dana", age=20)  # Here is a different order


# Here is the fourth example: passing a list and other data types as arguments
def calculate_average(grades_list):
    #function that gets a list of grades and returns the average.
    return sum(grades_list) / len(grades_list)

student_grades = [80, 90, 70, 100]
print("Average grade:", calculate_average(student_grades))

# Here is a function that gets a dictionary as an argument
def show_student(student_info):
    #function that prints the data from a dictionary.
    print(student_info["name"], "studies", student_info["subject"])

show_student({"name": "Ali", "subject": "Python"})

# Here is a function that changes a list, the original list also changes
def add_fruit(fruits_list):
    #function that adds a fruit to the list it received.
    fruits_list.append("banana")

my_fruits = ["apple", "orange"]
add_fruit(my_fruits)
print("My fruits after the function:", my_fruits)
