import random
play = 'yes'

while (play == 'yes'):
    number = random.randint(1, 100)
    user_guess = int(input("What is your guess? "))
    num_guesses = 1
    while (user_guess != number):
        if user_guess < number:
            print("Higher")
        if user_guess > number:
            print("Lower")
        user_guess = int(input("What is your guess? "))
        num_guesses += 1
    print(f"You guessed it! It took you {num_guesses} guesses.")
    play = input("Would you like to play again? ").lower()
print("Thank you for playing!")