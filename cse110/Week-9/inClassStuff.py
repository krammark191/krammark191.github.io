last_name = "Van Horn"

print("\nI am Brother", last_name)
print("\nHello Mark", last_name[0])
print()

length = len(last_name)
for index in range(length):
    print(last_name[index])
print("\n-----------------------------\n")
for letter in last_name:
    print(letter)
print()

numbers = [3, 7, 8, 2, 6, 9]
print(len(numbers))