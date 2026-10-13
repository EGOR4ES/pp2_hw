"""
Task 2: Check access to a specified path.
Test existence, readability, writability, and executability.
"""

import os


def check_path_access(path):
    """Here is a function that checks several things about one path."""
    print("Checking path:", path)
    print("  Exists:    ", os.path.exists(path))
    print("  Readable:  ", os.access(path, os.R_OK))
    print("  Writable:  ", os.access(path, os.W_OK))
    print("  Executable:", os.access(path, os.X_OK))


# Here is testing an existing file
with open("sample_for_access.txt", "w") as file:
    file.write("just a test file")

check_path_access("sample_for_access.txt")

print()

# Here is testing a path that does not exist at all
check_path_access("this_file_does_not_exist.txt")
