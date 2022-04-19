# 1. Name:
#      Mark Van Horn
# 2. Assignment Name:
#      Lab 10: Numeric Sequence
# 3. Assignment Description:
#      The program is meant to receive a number from the user and then calculate
#      the Francois number at that index and show it to the user.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was actually the design part, implementation was actually
#      very easy.
# 5. How long did it take for you to complete the assignment?
#      Total time was about 30 minutes.

# Create an option to loop through again.
play_again = True
while play_again:
    number = int(input("\nWhich Francois number would you like to see? "))

    # Take care of negative number cases.
    while number < 1:
        number = int(input("Please enter a positive integer greater than zero: "))
    
    # Establish preliminary values.
    number = number - 1
    a = 2
    b = 1

    # Print case if user selects the first number.
    if number == 0:
        print("Francois number 1 is 2.")

    # Begin calcuations for selected number.
    else:
        for i in range(2, number + 1):
            c = a + b
            a = b
            b = c
        print(f"Francois number {number + 1} is {b}.")
    
    # Ask the user if they want to do another number, if not change play_again to False,
    # else do nothing, as play_again is already True.
    play_again_prompt = input("\nWould you like to enter another Francois number? (y/n) ").lower()
    if play_again_prompt == 'n':
        play_again = False