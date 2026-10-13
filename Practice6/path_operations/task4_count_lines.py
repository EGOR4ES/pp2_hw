"""
Task 4: Count the number of lines in a text file.
"""

# Here is a sample file with a known number of lines, so I can check my answer
with open("lines_sample.txt", "w") as file:
    file.write("First line\n")
    file.write("Second line\n")
    file.write("Third line\n")
    file.write("Fourth line\n")


def count_lines(file_path):
    """Here is a function that counts how many lines are in a file."""
    with open(file_path, "r") as file:
        lines = file.readlines()
        return len(lines)


total_lines = count_lines("lines_sample.txt")
print("lines_sample.txt has", total_lines, "lines")
