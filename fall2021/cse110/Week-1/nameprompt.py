try:
    birth_year = int(input("\n\n\nPlease enter your birth year: "))
    print(f"Your age is {2021 - birth_year}\n\n\n")
except ValueError:
    print(">:(\n\n\n")