# 1. Name: 
#    Mark Van Horn
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#    This program asks the user for an integer which it then creates a random number
#    from 1 to the supplied number and asks the user to guess the number until they
#    get it right, which it then displays how many guess and what the guess were.
# 4. What was the hardest part? Be as specific as possible.
#    The hardest part was honestly figuring out where in the template to put each line
#    of code, I'm still not sure I got it all correct. The last class I took in python
#    (CSE 110) had us just write the code and annotate it ourselves, and the CS124 class
#    I took had basic function heading requirements and this heading but that was it.
#    The hardest part will be adhering to the exact requirements of the template.
#    The lab itself was not difficult to create, I've created simple binary guessing games
#    in Java, C#, and C++ before.
#    The only difficulty (if you could call it that) was I forgot exactly how to set up an
#    array, but I looked at a past assignment from one of my previous classes for a quick
#    refresher.
# 5. How long did it take for you to complete the assignment?
#    30 minutes.  

import random

# Game introduction
print("This is the \"guess a number\" game.")
print("You try to guess a random number in the smallest number of attempts.")

# Prompt the user for how difficult the game will be. Ask for an integer
value_max = int(input("\nPick a positive integer: "))

# Generate a random number between 1 and the chosen value
value_random = random.randint(1, value_max)

# Give the user instructions as to what he or she will be doing
print(f"Guess a number between 1 and {value_max}.")

# Initialize the sentinal and the array of guesses
numbers_guessed = []
num_guesses = 0
player_guess = 0

# Play the guessing game
while player_guess != value_random:

    # Prompt the user for a number
    player_guess = int(input("> "))

    # Store the number in an array so it can be displayed later
    numbers_guessed.append(player_guess)
    num_guesses += 1

    # Make a decision: was the guess too high, too low, or just right
    if player_guess < value_random:
        print("\tToo low!")
    elif player_guess > value_random:
        print("\tToo high!")

# Give the user a report: How many guesses and what the guesses were
print(f"You were able to find the number in {num_guesses} guesses.")
print(f"The numbers you guessed were: {numbers_guessed}")