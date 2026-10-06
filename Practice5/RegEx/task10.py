"""
Task 10: Convert a given camel case string to a snake case string.
Pattern explanation: same lookahead trick as task 9, but instead of a space
we insert an underscore, and then make everything lowercase.
"""
import re


def camel_to_snake(camel_case_text):
    pattern = r"(?<!^)(?=[A-Z])"
    with_underscores = re.sub(pattern, "_", camel_case_text)
    return with_underscores.lower()


test_words = ["studentName", "totalPriceValue", "helloWorld", "alreadyWorkingCode"]

for word in test_words:
    print(f"'{word}' -> '{camel_to_snake(word)}'")
