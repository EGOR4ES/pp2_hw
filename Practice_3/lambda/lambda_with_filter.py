# Here is the first example: keeping only even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
print("Even numbers:", even_numbers)


# Here is the second example: keeping only long words
words = ["cat", "elephant", "dog", "giraffe", "ant"]
long_words = list(filter(lambda word: len(word) > 3, words))
print("Long words:", long_words)


# Here is the third example: finding adults by their ages
ages = [12, 18, 25, 16, 40, 9]
adult_ages = list(filter(lambda age: age >= 18, ages))
print("Adult ages:", adult_ages)


# Here is the fourth example: students who passed the exam (list of dictionaries)
students = [
    {"name": "Ali", "grade": 85},
    {"name": "Sara", "grade": 45},
    {"name": "Dana", "grade": 70},
    {"name": "Bek", "grade": 55},
]
passed_students = list(filter(lambda student: student["grade"] >= 60, students))
for student in passed_students:
    print(student["name"], "passed with", student["grade"])


# Here is the fifth example: removing empty strings from a list
messy_list = ["hello", "", "world", "", "python"]
clean_list = list(filter(lambda text: text != "", messy_list))
print("Clean list:", clean_list)
