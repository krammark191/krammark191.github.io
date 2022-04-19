num = int(input("Please enter a positive number: "))
while num < 0:
    num = int(input("Sorry, that is a negative number, please try again.\n"
    "Please enter a positive number: "))
print(f"Your number is: {num}")

candy = "no"
while candy != "yes":
    candy = input("Can I have a piece of candy? ").lower()
print("Thank you.")