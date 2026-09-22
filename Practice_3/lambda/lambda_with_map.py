# Here is the first example: squares of all numbers in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda number: number ** 2, numbers))
print("Squares:", squared_numbers)


# Here is the second example: converting Celsius to Fahrenheit
celsius_temperatures = [0, 20, 30, 100]
fahrenheit_temperatures = list(map(lambda celsius: celsius * 9 / 5 + 32, celsius_temperatures))
print("Fahrenheit:", fahrenheit_temperatures)


# Here is the third example: making every name uppercase
student_names = ["anna", "timur", "dana"]
uppercase_names = list(map(lambda name: name.upper(), student_names))
print("Uppercase names:", uppercase_names)


# Here is the fourth example: adding 12 percent tax to prices
prices = [100, 250, 400]
prices_with_tax = list(map(lambda price: price * 1.12, prices))
print("Prices with tax:", prices_with_tax)


# Here is the fifth example: map with two lists at the same time
first_list = [1, 2, 3]
second_list = [10, 20, 30]
sums_of_pairs = list(map(lambda x, y: x + y, first_list, second_list))
print("Sums of pairs:", sums_of_pairs)
