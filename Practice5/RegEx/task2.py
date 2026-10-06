"""
Task 2: Match a string that has an 'a' followed by two to three 'b'.
Pattern explanation: 'b{2,3}' means between 2 and 3 letters b.
"""
import re

pattern = r"ab{2,3}"

test_words = ["ab", "abb", "abbb", "abbbb", "a"]

for word in test_words:
    match_result = re.search(pattern, word)
    if match_result:
        print(f"'{word}' -> matched part: '{match_result.group()}'")
    else:
        print(f"'{word}' -> no match")
