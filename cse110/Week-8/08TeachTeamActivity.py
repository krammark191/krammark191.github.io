import math

# This line prompts the user for the size of the muliplication table.
user_choice = int(input("How many columns and rows do you want in your multiplication table? "))

# This section determines the maximum number that will be multiplied in the table and calculates
# the necessary spacing needed.
max_number = user_choice ** 2
digits = int(math.log10(max_number)) + 1

# This nested for loop creates and prints the muliplication table based on the user input.
range_size = user_choice + 1
for row_number in range(1, range_size):
    for column_number in range(1, range_size):
        number = row_number * column_number
        print(f"{number:{digits}}", end=" ")
    print()