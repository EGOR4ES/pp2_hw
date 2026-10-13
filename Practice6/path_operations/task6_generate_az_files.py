"""
Task 6: Generate 26 text files named A.txt, B.txt, and so on, up to Z.txt
"""

import os
import string

output_folder = "az_files"
os.makedirs(output_folder, exist_ok=True)

for letter in string.ascii_uppercase:  # Here is "ABCDEFGH...XYZ"
    file_name = letter + ".txt"
    file_path = os.path.join(output_folder, file_name)
    with open(file_path, "w") as file:
        file.write("This is the file for letter " + letter)

created_files = sorted(os.listdir(output_folder))
print("Created", len(created_files), "files:")
print(created_files)
