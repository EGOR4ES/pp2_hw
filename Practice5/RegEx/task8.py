"""
Task 8: Split a string at uppercase letters.
Pattern explanation: '(?=[A-Z])' is a lookahead, it finds the position
right before a capital letter, without consuming the letter itself.
That is where re.split cuts the string.
"""
import re

pattern = r"(?=[A-Z])"

test_words = ["StudentNameAge", "HelloWorldPython", "RegexIsFun"]

for word in test_words:
    parts = re.split(pattern, word)
    # Here I remove the empty string that appears at the very start
    parts = [part for part in parts if part != ""]
    print(f"'{word}' -> {parts}")
