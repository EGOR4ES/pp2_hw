"""
Task 7: Convert a snake case string to a camel case string.
Pattern explanation: '_([a-z])' finds an underscore followed by a small letter,
and the lambda function turns that small letter into a capital letter,
while removing the underscore.
"""
import re


def snake_to_camel(snake_case_text):
    pattern = r"_([a-z])"
    return re.sub(pattern, lambda match: match.group(1).upper(), snake_case_text)


test_words = ["student_name", "total_price_value", "hello_world", "already_working_code"]

for word in test_words:
    print(f"'{word}' -> '{snake_to_camel(word)}'")
