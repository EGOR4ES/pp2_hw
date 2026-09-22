# Here is the first example: sorting words by their length
words = ["banana", "kiwi", "apple", "fig"]
sorted_by_length = sorted(words, key=lambda word: len(word))
print("By length:", sorted_by_length)


# Here is the second example: sorting tuples by the second value
pairs = [("a", 3), ("b", 1), ("c", 2)]
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
print("By second value:", sorted_pairs)


# Here is the third example: sorting students by grade from high to low
students = [
    {"name": "Ali", "grade": 85},
    {"name": "Sara", "grade": 95},
    {"name": "Dana", "grade": 70},
]
best_students_first = sorted(students, key=lambda student: student["grade"], reverse=True)
for student in best_students_first:
    print(student["name"], student["grade"])


# Here is the fourth example: sorting words by their last letter
names = ["Anna", "Timur", "Dana", "Bek"]
sorted_by_last_letter = sorted(names, key=lambda name: name[-1])
print("By last letter:", sorted_by_last_letter)


# Here is the fifth example: sorting products by price (cheap first)
products = [("laptop", 500000), ("mouse", 5000), ("keyboard", 15000)]
cheapest_first = sorted(products, key=lambda product: product[1])
print("Cheapest first:", cheapest_first)
