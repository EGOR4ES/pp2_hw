"""
Type checking and type conversion functions
"""

# Here is checking the type of different values with type()
print(type(10))
print(type(3.14))
print(type("hello"))
print(type([1, 2, 3]))
print(type(True))


# Here is checking a type with isinstance() - this is usually better than type()
number = 42
print("Is number an int?", isinstance(number, int))
print("Is number a string?", isinstance(number, str))


# Here is converting between types
text_number = "25"
real_number = int(text_number)  # Here is converting text to a whole number
print(real_number + 5)  # Here is proof it is really a number now, not text

price_text = "19.99"
price_number = float(price_text)  # Here is converting text to a decimal number
print(price_number * 2)

number_as_text = str(100)  # Here is converting a number into text
print("The number as text is: '" + number_as_text + "'")


# Here is converting between lists, tuples, and sets
my_list = [1, 2, 2, 3, 3, 3]
my_tuple = tuple(my_list)   # Here is a list turned into a tuple
my_set = set(my_list)        # Here is a list turned into a set, duplicates disappear

print("As a tuple:", my_tuple)
print("As a set (no duplicates):", my_set)
print("Back to a list:", list(my_set))


# Here is a safe way to convert text to a number, using try/except
def safe_convert_to_int(text_value):
    """Here is a function that tries to convert text to a number safely."""
    try:
        return int(text_value)
    except ValueError:
        return None

print(safe_convert_to_int("42"))
print(safe_convert_to_int("not a number"))
