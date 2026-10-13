"""
Task 7: Copy the contents of a file to another file.
(I do this manually with read/write, without using shutil, to practice file handling)
"""

# Here is the original file with some content
with open("source_text.txt", "w") as file:
    file.write("This text will be copied.\n")
    file.write("Line two of the original file.\n")


def copy_file_contents(source_path, destination_path):
    """Here is a function that reads one file and writes its content into another."""
    with open(source_path, "r") as source_file:
        content = source_file.read()

    with open(destination_path, "w") as destination_file:
        destination_file.write(content)


copy_file_contents("source_text.txt", "copied_text.txt")
print("Copied source_text.txt -> copied_text.txt")

with open("copied_text.txt", "r") as file:
    print("--- Contents of copied_text.txt ---")
    print(file.read())
