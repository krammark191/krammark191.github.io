# 1. Name:
#      Mark Van Horn
# 2. Assignment Name:
#      Lab 13: Prime Numbers
# 3. Assignment Description:
#      This program is meant to display all prime numbers at or below
#      a given number.
# 4. What was the hardest part? Be as specific as possible.
#      This assignment was not too difficult, the hardest part was
#      ironing out small bugs.
# 5. How long did it take for you to complete the assignment?
#      It took me an hour to complete this assignment.

# Used for the square root function.
import math

# Determines if the given number is less than two and displays a message
# accordingly, also returns a boolean value that Main uses to determine
# whether to run find_the_primes().
def is_less_than_two(n):
    if n < 2:
        print(f"There are no prime numbers at or below {n}.")
        assert n < 2
        return True

# Accepts the user input and finds any and all prime numbers at or less
# than the given value.
def find_the_primes(n):

    # Initiates a boolean array the size of the given number plus one and
    # assigns all values to True.
    numbers =  [True] * (n + 1)

    # Sets the first and second index of the array as they correspond to
    # 0 and 1 respectively. They will always be false as they are not
    # prime numbers and they will never be out of the array's range as
    # if they were this function would not be called.
    assert len(numbers) > 2
    numbers[0] = numbers[1] = False

    # Iterates through every factor of every number at or less than the
    # square root of the given number.
    for factor in range(2, int(math.sqrt(n)) + 1):
        assert len(numbers) >= factor
        if numbers[factor]:
            for multiple in range(factor * 2, n + 1, factor):
                assert len(numbers) >= multiple
                numbers[multiple] = False
    # Initiates primes array for assigning remaining values still true
    # from the numbers array to the primes array.
    primes = []
    for index in range(2, n + 1):

        # If the value at the index of the numbers array is still true,
        # the index, which corresponds to the number, is added to the
        # primes array.
        assert len(numbers) >= index
        if numbers[index]:
            primes.append(index)
    
    return primes

# Main function: Asks the user for a number, then displays all prime numbers
# at or less than the given number.
print()
n = int(input("This program will find all the prime numbers at or below N. Select that N: "))
while is_less_than_two(n):
    n = int(input("Please enter a new value for N: "))
if not is_less_than_two(n):
    print(f"The prime numbers at or below {n} are {find_the_primes(n)}")
print()