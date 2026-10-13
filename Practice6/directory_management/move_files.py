"""
Moving/copying files between directories, and finding files by extension
"""

import os
import shutil

# Here is preparing two folders and a few sample files to work with
os.makedirs("source_folder", exist_ok=True)
os.makedirs("destination_folder", exist_ok=True)

sample_files = ["report.txt", "photo.jpg", "data.csv", "notes.txt"]
for file_name in sample_files:
    with open(os.path.join("source_folder", file_name), "w") as file:
        file.write("Sample content for " + file_name)

print("Created sample files in source_folder")


# Here is listing files and folders separately
print("--- Everything inside source_folder ---")
for item in os.listdir("source_folder"):
    full_path = os.path.join("source_folder", item)
    if os.path.isfile(full_path):
        print(item, "-> this is a file")
    elif os.path.isdir(full_path):
        print(item, "-> this is a folder")


# Here is finding only the files that end with ".txt"
print("--- Only .txt files ---")
txt_files = [name for name in os.listdir("source_folder") if name.endswith(".txt")]
print(txt_files)


# Here is copying one file from source_folder to destination_folder
shutil.copy(os.path.join("source_folder", "report.txt"),
            os.path.join("destination_folder", "report.txt"))
print("Copied report.txt to destination_folder")


# Here is MOVING a file (it disappears from the old place)
shutil.move(os.path.join("source_folder", "data.csv"),
            os.path.join("destination_folder", "data.csv"))
print("Moved data.csv to destination_folder")

print("source_folder now has:", os.listdir("source_folder"))
print("destination_folder now has:", os.listdir("destination_folder"))
