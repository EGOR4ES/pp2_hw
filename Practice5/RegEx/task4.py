"""
Task 4: Find sequences of one upper case letter followed by lower case letters.
Pattern explanation: '[A-Z]' is exactly one capital letter,
then '[a-z]*' is zero or more small letters after it.
"""
import re

pattern = r"[A-Z][a-z]*"

text = "Hello World, this is Python and RegEx practice with Almaty city"

found_items = re.findall(pattern, text)
print("Found:", found_items)
