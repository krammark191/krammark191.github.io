print("Enter a list of numbers, type 0 when finished.")

numbers = []
number = -1

while number != 0:
    number = int(input("Enter number: "))

    if number != 0:
        numbers.append(number)

sum = 0

for number in numbers:
    sum += number

print(f"The sum is: {sum}")

count = len(numbers)
average = sum / count

print(f"The average is: {average}")

max_number = 0
for number in numbers:
    if number > max_number:
        max_number = number

print(f"The largest number is: {max_number}")

small_pos_number = 9999999999999999
for number in numbers:
    if 0 < number < small_pos_number:
        small_pos_number = number

print(f"The smallest positive number is: {small_pos_number}")


sorted_list = sorted(numbers)
print("The sorted list is:")
for number in sorted_list:
    print(number)