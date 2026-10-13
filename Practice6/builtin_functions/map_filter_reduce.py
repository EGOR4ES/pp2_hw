"""
Using map(), filter(), and reduce() on lists
"""

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Here is map() - it applies a function to EVERY item in the list
squared_numbers = list(map(lambda number: number ** 2, numbers))
print("Squared numbers:", squared_numbers)


# Here is filter() - it keeps only the items where the function returns True
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
print("Even numbers:", even_numbers)


# Here is combining map() and filter() together
# First I keep only even numbers, then I square them
even_squares = list(map(lambda number: number ** 2, filter(lambda number: number % 2 == 0, numbers)))
print("Squares of even numbers:", even_squares)


# Here is reduce() - it combines all items into ONE single value
# It needs a function with two arguments: the "running total" and the "next item"
total_sum = reduce(lambda total, number: total + number, numbers)
print("Sum of all numbers using reduce:", total_sum)

# Here is using reduce() to find the biggest number in the list
biggest_number = reduce(lambda a, b: a if a > b else b, numbers)
print("Biggest number using reduce:", biggest_number)


# Here is a more practical example: prices with a discount
prices = [1000, 2500, 300, 7600]
discounted_prices = list(map(lambda price: price * 0.9, prices))  # Here is 10% off
print("Prices after 10% discount:", discounted_prices)

total_spent = reduce(lambda total, price: total + price, discounted_prices)
print("Total amount to pay:", total_spent)
