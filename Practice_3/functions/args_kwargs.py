# Here is the first example: *args takes any number of positional arguments
def sum_all_numbers(*numbers):
    #function that sums as many numbers as I give it.
    total = 0
    for number in numbers:
        total = total + number
    return total

print(sum_all_numbers(1, 2, 3))
print(sum_all_numbers(10, 20, 30, 40, 50))


# Here is the second example: **kwargs takes any number of keyword arguments
def print_student_info(**info):
    #function that prints every key and value that I give it.
    for key, value in info.items():
        print(key, "->", value)

print_student_info(name="Madina", age=19, university="KBTU")


# Here is the third example: using both *args and **kwargs together
def show_order(customer_name, *items, **options):
    #function that prints an order with items and extra options.
    print("Customer:", customer_name)
    print("Items:", items)      # Here is a tuple with all extra items
    print("Options:", options)  # Here is a dictionary with all keyword options

show_order("Bek", "pizza", "cola", "salad", delivery=True, tip=500)


# Here is the fourth example: unpacking a list and a dictionary into a call
numbers_list = [5, 10, 15]
print(sum_all_numbers(*numbers_list))  # Here is the * that unpacks the list

person_data = {"name": "Aidos", "age": 21}
print_student_info(**person_data)      # Here is the ** that unpacks the dictionary
