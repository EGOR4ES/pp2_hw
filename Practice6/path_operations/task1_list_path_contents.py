"""
Task 1: List only directories, only files, and both files and directories
in a specified path.
"""

import os

target_path = "."  # Here I use the current folder as the path to check

all_items = os.listdir(target_path)

only_files = []
only_directories = []

for item in all_items:
    full_path = os.path.join(target_path, item)
    if os.path.isfile(full_path):
        only_files.append(item)
    elif os.path.isdir(full_path):
        only_directories.append(item)

print("All files and directories:", all_items)
print("Only files:", only_files)
print("Only directories:", only_directories)
