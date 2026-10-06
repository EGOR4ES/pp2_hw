"""
Task 6: Replace all occurrences of space, comma, or dot with a colon.
Pattern explanation: '[ ,.]' is a character class that matches
a space, a comma, or a dot (any one of these three characters).
"""
import re

pattern = r"[ ,.]"

text = "Python, Regex. Is fun and useful."

result_text = re.sub(pattern, ":", text)
print("Before:", text)
print("After: ", result_text)
