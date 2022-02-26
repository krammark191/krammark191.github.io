# 1. Name:
#      Mark Van Horn
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      This program is meant to read a file containing a list,
#      sort the list, then print the list.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was getting the sorting algorithm to work.
#      There were several areas in which it worked partially, I
#      finally got it to work but I'm not sure if it meets the
#      requirements fully.
# 5. How long did it take for you to complete the assignment?
#      About an hour and a half.

import json

# Get file name from user.
file_name = input("\nWhat is the name of the file? ")

# Read JSON file into Python string.
try:
    with open(f"C://git//krammark191.github.io//cse130//week8//{file_name}") as file:
        json_data = json.load(file)
except:
    print("File not found.\n")
    exit()

# Transcribe the JSON object into a python list.
python_list = []
for item in json_data['array']:
    python_list.append(item)

# Sort the python list.
def reverse_linear_sort(array):
    assert len(array) > 0, "Array should not be empty."
    for index in range(1, len(array)):
        highest_number = array[index]
        temp = index - 1
        while temp >= 0 and highest_number < array[temp]:
            array[temp + 1] = array[temp]
            temp -= 1
        array[temp + 1] = highest_number

# Check if list is empty, else run the sorting algorithm.
if python_list:
    reverse_linear_sort(python_list)
    print(f"The values in {file_name} are:")
    for item in python_list:
        print(item)
    print()
else:
    assert len(python_list) == 0, "List should be empty."
    print("This list is empty.\n")