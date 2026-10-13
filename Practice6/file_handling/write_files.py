"""
Writing and appending files - w mode, a mode, x mode, writelines()
"""

# Here is "w" mode: it creates a new file, or empties it if it already exists
with open("notes.txt", "w") as file:
    file.write("First note\n")
    file.write("Second note\n")

print("Created notes.txt with 2 lines")


# Here is "a" mode: it adds new lines to the end, without deleting old ones
with open("notes.txt", "a") as file:
    file.write("Third note (appended)\n")

with open("notes.txt", "r") as file:
    print("--- notes.txt after appending ---")
    print(file.read())


# Here is writing many lines at once with writelines()
lines_to_write = ["Apple\n", "Banana\n", "Cherry\n"]
with open("fruits.txt", "w") as file:
    file.writelines(lines_to_write)

with open("fruits.txt", "r") as file:
    print("--- fruits.txt ---")
    print(file.read())


# Here is "x" mode: it only creates a NEW file, and gives an error if it exists already
try:
    with open("notes.txt", "x") as file:
        file.write("This will not work, notes.txt already exists")
except FileExistsError:
    print("'x' mode blocked me because notes.txt already exists - that is its job")

# Here is "x" mode working correctly on a file that does not exist yet
with open("brand_new_file.txt", "x") as file:
    file.write("This file was just created with x mode")
print("brand_new_file.txt was created successfully")
