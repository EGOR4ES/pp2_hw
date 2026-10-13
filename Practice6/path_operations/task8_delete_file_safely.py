"""
Task 8: Delete a file by its specified path.
Before deleting, check for access and whether the path exists.
"""

import os


def delete_file_safely(file_path):
    """Here is a function that deletes a file only after checking it is safe to do so."""
    if not os.path.exists(file_path):
        print(file_path, "does not exist, nothing to delete")
        return

    if not os.access(file_path, os.W_OK):
        print("I do not have permission to delete", file_path)
        return

    os.remove(file_path)
    print(file_path, "was deleted successfully")


# Here is a sample file created just so I have something to delete
with open("temp_file.txt", "w") as file:
    file.write("temporary data")

delete_file_safely("temp_file.txt")

# Here is trying to delete it again - it should already be gone
delete_file_safely("temp_file.txt")

# Here is trying to delete a file that never existed
delete_file_safely("never_existed.txt")
