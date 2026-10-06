"""
Task 3: Find sequences of lowercase letters joined with an underscore.
Pattern explanation: '[a-z]+' is one or more lowercase letters,
then '_', then '[a-z]+' again.
"""
import re

pattern = r"[a-z]+_[a-z]+"

text = "function_name and another_example plus simpleword and third_one"

found_items = re.findall(pattern, text)
print("Found:", found_items)
