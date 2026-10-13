"""
Task 5: Write a list to a file.
"""

shopping_list = ["Milk", "Eggs", "Bread", "Apples", "Rice"]

# Here is writing each item of the list on its own line
with open("shopping_list.txt", "w") as file:
    for item in shopping_list:
        file.write(item + "\n")

print("Saved the shopping list to shopping_list.txt")

# Here is reading it back to prove it worked
with open("shopping_list.txt", "r") as file:
    print("--- Contents of shopping_list.txt ---")
    print(file.read())
