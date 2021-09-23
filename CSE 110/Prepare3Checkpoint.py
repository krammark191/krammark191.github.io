age = int(input('How old are you? ')) + 1
print(f"On your next birthday you will be {age}.\n")
eggCount = int(input("How many egg cartons do you have? ")) * 12
print(f"You have {eggCount} eggs.\n")
cookieCount = int(input("How many cookies do you have? "))
if cookieCount == 0:
    print("HA! Sucks to be you loser.\n")
else:
    peopleCount = int(input("How many people are there? "))
    cookieEach = cookieCount / peopleCount
    if cookieEach == 1:
        print(f"Each person may have 1 cookie.\n")
    else:
        print(f"Each person may have {cookieEach} cookies.\n")