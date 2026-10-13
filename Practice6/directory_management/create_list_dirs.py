"""
Creating and listing directories - os.mkdir, os.makedirs, os.listdir,
os.chdir, os.getcwd, os.rmdir
"""

import os

# Here is checking where I am right now with os.getcwd()
starting_folder = os.getcwd()
print("I am currently in:", starting_folder)


# Here is creating one simple folder with os.mkdir()
if not os.path.exists("my_folder"):
    os.mkdir("my_folder")
    print("Created my_folder")
else:
    print("my_folder already exists")


# Here is creating nested folders at once with os.makedirs()
# os.mkdir() can only make ONE folder, but makedirs() can make a whole path
nested_path = "projects/python/practice6"
if not os.path.exists(nested_path):
    os.makedirs(nested_path)
    print("Created nested folders:", nested_path)
else:
    print(nested_path, "already exists")


# Here is listing everything inside the current folder with os.listdir()
print("--- Contents of the current folder ---")
for item in os.listdir("."):
    print(item)


# Here is moving into a folder with os.chdir(), and then going back
os.chdir("my_folder")
print("Now I am inside:", os.getcwd())

os.chdir(starting_folder)  # Here is going back to where I started
print("I went back to:", os.getcwd())


# Here is removing an empty folder with os.rmdir()
# rmdir() only works if the folder is EMPTY
os.rmdir("my_folder")
print("Removed my_folder")

# Here is checking it is really gone
print("Does my_folder still exist?", os.path.exists("my_folder"))
