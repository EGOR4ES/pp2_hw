"""
Task 9: Insert spaces between words starting with capital letters.
Pattern explanation: '(?<!^)(?=[A-Z])' finds every position before
a capital letter, except the very first position of the string
(that is what '(?<!^)' means), and we insert a space there.
"""
import re

pattern = r"(?<!^)(?=[A-Z])"

test_words = ["StudentNameAge", "HelloWorldPython", "RegexIsFun"]

for word in test_words:
    result_text = re.sub(pattern, " ", word)
    print(f"'{word}' -> '{result_text}'")
