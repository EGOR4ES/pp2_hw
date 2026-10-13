"""
Reading files - r mode, read(), readline(), readlines(), with statement
"""

# Here is a small sample file I create first, so I have something to read
with open("sample.txt", "w") as sample_file:
    sample_file.write("Line one\n")
    sample_file.write("Line two\n")
    sample_file.write("Line three\n")


# Here is reading the whole file at once with read()
# The "with" statement is called a context manager, it closes the file automatically
with open("sample.txt", "r") as file:
    whole_text = file.read()
    print("--- read() ---")
    print(whole_text)


# Here is reading just one line with readline()
with open("sample.txt", "r") as file:
    first_line = file.readline()
    second_line = file.readline()
    print("--- readline() called twice ---")
    print("First line:", first_line.strip())
    print("Second line:", second_line.strip())


# Here is reading all lines into a list with readlines()
with open("sample.txt", "r") as file:
    all_lines = file.readlines()
    print("--- readlines() ---")
    print(all_lines)


# Here is the most common way: loop over the file directly, line by line
with open("sample.txt", "r") as file:
    print("--- looping over the file ---")
    for line in file:
        print("Got line:", line.strip())
