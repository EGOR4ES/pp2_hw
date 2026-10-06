"""
Task 1: Match a string that has an 'a' followed by zero or more 'b's.
Pattern explanation: 'a' means the letter a, 'b*' means zero or more b's.
"""
import re

pattern = r"ab*"

test_words = ["a", "ab", "abbbb", "ac", "b"]

for word in test_words:
    match_result = re.search(pattern, word)
    if match_result:
        print(f"'{word}' -> matched part: '{match_result.group()}'")
    else:
        print(f"'{word}' -> no match")
