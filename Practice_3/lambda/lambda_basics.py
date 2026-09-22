# Here is the first example: the simplest lambda with one argument
add_ten = lambda number: number + 10
print(add_ten(5))    # Here is the result: 15
print(add_ten(100))  # Here is the result: 110


# Here is the second example: a lambda with two arguments
multiply = lambda first_number, second_number: first_number * second_number
print(multiply(4, 5))


# Here is the third example: a lambda with a condition inside
bigger_of_two = lambda a, b: a if a > b else b
print(bigger_of_two(3, 9))
print(bigger_of_two(50, 20))


# Here is the fourth example: a regular function and a lambda that do the same
def square_regular(number):
    #regular function that returns the square of a number
    return number * number

square_lambda = lambda number: number * number  # Here is the same thing as a lambda

print(square_regular(6))
print(square_lambda(6))


# Here is the fifth example: a function that creates lambdas (practical use)
def make_multiplier(factor):
    #function that returns a lambda which multiplies by factor
    return lambda number: number * factor

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(8))
print(triple(8))

# Here is a lambda that is used right away without a name (anonymous function)
print((lambda name: "Hello, " + name)("Aruzhan"))
