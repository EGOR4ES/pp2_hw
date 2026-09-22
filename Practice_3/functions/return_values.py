# Here is the first example: a function that returns one value
def multiply(first_number, second_number):
    #function that returns the product of two numbers.
    return first_number * second_number

result = multiply(6, 7)  # Here is where I save the returned value
print("6 * 7 =", result)


# Here is the second example: a function that returns several values
def find_min_and_max(numbers_list):
    #function that returns the smallest and the biggest number.
    return min(numbers_list), max(numbers_list)

smallest, biggest = find_min_and_max([4, 9, 1, 15, 7])
print("Smallest:", smallest, "| Biggest:", biggest)


# Here is the third example: a function without return gives None
def print_message(message):
    #function that only prints and does not return anything.
    print(message)

value_from_function = print_message("Just printing")
print("The function returned:", value_from_function)


# Here is the fourth example: return stops the function immediately
def check_age(age):
    #function that returns a text about the age.
    if age < 0:
        return "Age cannot be negative"  # Here is an early return
    if age >= 18:
        return "Adult"
    return "Child"

print(check_age(-5))
print(check_age(25))
print(check_age(10))


# Here is the fifth example: a function that returns a list
def get_even_numbers(limit):
    #function that returns all even numbers up to the limit.
    even_numbers = []
    for number in range(limit + 1):
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

print(get_even_numbers(10))
