num = int(input(print("Please enter a positive number: ")))
while num < 0:
    num = int(input(print("Sorry, that is a negative number, please try again.\n"
    "Please enter a positive number: ")))
print(f"Your number is: {num}")

candy = "no"
while candy != "yes":
    candy = input(print("Can I have a piece of candy? ")).lower()
print("Thank you.")