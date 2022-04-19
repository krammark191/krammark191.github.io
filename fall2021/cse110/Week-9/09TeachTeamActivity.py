print("Enter a list of numbers, type 0 when finished.")

# Initialize numbers list and number integer.
numbers = []
number = -1

# Loop for numbers to add to list, 0 for exit.
while number != 0:
    number = int(input("Enter number: "))

    if number != 0:
        numbers.append(number)

# Sum calculation.
sum = 0
for number in numbers:
    sum += number
print(f"The sum is: {sum}")

# Average calculation.
if sum != 0:
    average = sum / len(numbers)
else:
    average = 0
print(f"The average is: {average}")

# Largest number calculation.
max_number = -100000000000
for number in numbers:
    if number > max_number:
        max_number = number
print(f"The largest number is: {max_number}")

# Smallest positive number calculation.
small_pos_number = 9999999999999999
for number in numbers:
    if 0 < number < small_pos_number:
        small_pos_number = number
print(f"The smallest positive number is: {small_pos_number}")

# Print list from smallest to greatest.
sorted_list = sorted(numbers)
print("The sorted list is:")
for number in sorted_list:
    print(number)