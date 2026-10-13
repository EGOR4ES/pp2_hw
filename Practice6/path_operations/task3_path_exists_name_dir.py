"""
Task 3: Test whether a given path exists or not.
If it exists, find the filename and the directory portion of the path.
"""

import os


def inspect_path(path):
    """Here is a function that reports if a path exists, and splits it."""
    if os.path.exists(path):
        print(path, "-> exists")
        print("  File name:     ", os.path.basename(path))
        print("  Directory part:", os.path.dirname(path))
    else:
        print(path, "-> does NOT exist")


# Here is a sample file inside a sample folder, to have a real path to test
os.makedirs("sample_dir", exist_ok=True)
sample_path = os.path.join("sample_dir", "example.txt")
with open(sample_path, "w") as file:
    file.write("hello")

inspect_path(sample_path)
print()
inspect_path("missing_folder/missing_file.txt")
