# Here is the first example: a function without any arguments
def say_hello():
    #Here is a simple function that prints a hello message.
    print("Hello, world!")

# Here is how I call the function from example 1
say_hello()
say_hello()  # Here is a second call, functions can be used many times


# Here is the second example: a function with one argument
def greet_person(name):
    #function that greets a person by name.
    print("Hello, " + name + "!")

# Here is how I call it with different names
greet_person("Anna")
greet_person("Timur")


# Here is the third example: a function that does a math operation
def add_two_numbers(first_number, second_number):
    #function that adds two numbers and prints the sum.
    total = first_number + second_number
    print("The sum of", first_number, "and", second_number, "is", total)

add_two_numbers(5, 7)
add_two_numbers(10, 25)


# Here is the fourth example: one function calls another function
def print_square(number):
    # prints the square of a number.
    print(number, "squared is", number * number)

def print_squares_up_to(limit):
    #function that prints squares from 1 to the limit.
    for number in range(1, limit + 1):
        print_square(number)  # Here is the call of the first function

print_squares_up_to(5)
