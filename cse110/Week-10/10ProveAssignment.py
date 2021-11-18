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

    # This if statement is the code for adding an item to the list.
    if answer == 1:
        item_name.append(input("What item would you like to add? ").capitalize())
        item_price.append(float(input(f"What is the price of '{item_name[-1]}'? ")))
        print(f"'{item_name[-1]}' has been added to the cart.")

    # This displays the contents of the shopping cart.
    elif answer == 2:
        print("The contents of the shopping cart are:")
        length = len(item_name)
        for i in range(length):
            print(f"{i + 1}. {item_name[i]} - ${item_price[i]:.2f}")
    
    # This removes an item from the shopping cart.
    elif answer == 3:
        index_remove = int(input("Which item would you like to remove? ")) - 1
        if 0 > index_remove > len(item_name):
            print("Sorry, that is not a valid item number.")
        else:
            del item_name[index_remove]
            del item_price[index_remove]
            print("Item removed.")
    
    # This displays the total of all the items in the shopping cart.
    elif answer == 4:
        sum = 0
        for i in range(len(item_price)):
            sum += item_price[i]
        print(f"The total price of the items in the shopping cart is ${sum:.2f}")

    # This quits the program.
    elif answer == 5:
        print("Thank you. Goodbye.")
     # This is in case the user inputs something other than an int between 1 and 5.
    else:
        print("Invalid entry.")
    time.sleep(1)