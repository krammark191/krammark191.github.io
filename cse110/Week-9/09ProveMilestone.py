import time

item_name = []
item_price = []

answer = 0

while answer != 5:
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    answer = int(input("Please enter an action: "))
    if answer == 1:
        item_name.append(input("What item would you like to add? "))
    elif answer == 2:
        print("The contents of the shopping cart are:")
        length = len(item_name)
        for index in range(length):
            print(item_name[index])
    elif answer == 3:
        print("[WORK IN PROGRESS]")
    elif answer == 4:
        print("[WORK IN PROGRESS]")
    elif answer == 5:
        print("Thank you. Goodbye.")
    else:
        print("Invalid entry.")
    time.sleep(1)