# 1. Name:
#      Mark Van Horn
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      This program is meant to accept a user-inputed file name and search that
#      file for matching words.
# 4. Algorithmic Efficiency
#      Best case scenario is O(1), but that is only in the case of either an
#      empty list or a single-item list. Average efficiency is O(log n) as
#      with a binary search the efficiency increases with the size of the array.
#      This means that this program is more efficient at searching through
#      Lab06.countries.json than any of the other .json files provided for this
#      search program.
# 5. What was the hardest part? Be as specific as possible.
#      The hardest part was getting the actual search function to work, I
#      ended up going with a recursive solution because it was a little easier,
#      more efficient (I think), and definitely cooler than a standard while loop.
# 6. How long did it take for you to complete the assignment?
#      This assignment took me roughly an hour and a half (1.5 hrs).

import json

# Get file name from user.
file_name = input("\nWhat is the name of the file? ")

# Read JSON file into Python string.
try:
    with open(f"C://git//krammark191.github.io//cse130//week6//{file_name}") as file:
        json_data = json.load(file)
except:
    print("File not found.\n")
    exit()

# Transcribe the JSON object into a python list.
python_list = []
for item in json_data['array']:
    python_list.append(item)

# Check if the list is empty and respond accordingly.
if python_list:
    item_to_find = input("What name are we looking for? ")
else:
    print("This list is empty.\n")
    exit()

# Recursive function used for binary search.
def advanced_search(python_list, low, high, item_to_find):
    if high >= low:
        midpoint = (high + low) // 2
        if python_list[midpoint] == item_to_find:
            return midpoint
        elif python_list[midpoint] > item_to_find:
            return advanced_search(python_list, low, midpoint - 1, item_to_find)
        else:
            return advanced_search(python_list, midpoint + 1, high, item_to_find)
    else:
        return -1
result = advanced_search(python_list, 0, len(python_list)-1, item_to_find)

# Take result of the advanced search function and print statement depending on result.
if result != -1:
    print(f"We found {item_to_find} in {file_name}.\n")
else:
    print(f"We did not find {item_to_find} in {file_name}.\n")