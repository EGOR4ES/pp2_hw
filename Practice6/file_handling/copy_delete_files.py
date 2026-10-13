"""
Copying, backing up, and deleting files - using the shutil module
"""

import os
import shutil

# Here is a sample file I create so I have something to copy and delete
with open("original.txt", "w") as file:
    file.write("This is the original file.\n")
    file.write("It has some important data.\n")


# Here is copying a file to a new name with shutil.copy()
shutil.copy("original.txt", "copy_of_original.txt")
print("Copied original.txt -> copy_of_original.txt")

with open("copy_of_original.txt", "r") as file:
    print("Content of the copy:")
    print(file.read())


# Here is making a backup with a different name, using shutil.copy2()
# copy2 is like copy, but it also keeps the original file's metadata (like date)
shutil.copy2("original.txt", "original_backup.txt")
print("Backup created: original_backup.txt")


# Here is deleting a file safely - I check that it exists BEFORE deleting it
file_to_delete = "copy_of_original.txt"

if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print(file_to_delete, "was deleted")
else:
    print(file_to_delete, "does not exist, nothing to delete")

# Here is trying to delete the same file again - it should not exist anymore
if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
else:
    print(file_to_delete, "is already gone, I did not try to delete it again")
