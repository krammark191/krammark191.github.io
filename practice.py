year = int(input("Enter year: "))
isLeapYear = True if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)) else False
print(f"{year} is a leap year.") if isLeapYear else print(f"{year} is not a leap year.")