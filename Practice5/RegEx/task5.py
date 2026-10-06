"""
Task 5: Match a string that has an 'a' followed by anything, ending in 'b'.
Pattern explanation: '.*' means any characters (zero or more),
so this matches everything between the first 'a' and the last 'b'.
"""
import re

pattern = r"a.*b"

test_words = ["ab", "a123b", "axxxxb", "ba", "a_middle_text_b"]

for word in test_words:
    match_result = re.search(pattern, word)
    if match_result:
        print(f"'{word}' -> matched part: '{match_result.group()}'")
    else:
        print(f"'{word}' -> no match")
