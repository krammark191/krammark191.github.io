# 1. Name:
#      Mark Van Horn
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      This program is designed to determine whether a hotel can be
#      built on Pennsylvania Avenue in Monopoly.
# 4. What was the hardest part? Be as specific as possible.
#      Was it the syntax of Python?
#          No, the syntax was easy.
#      Was it an aspect of the problem you are to solve?
#          Yes, making sure every condition is checked proved to be
#          a bit tough to keep track of.
#      Was it the instructions or any part of the problem definition?
#          No, the instructions were clear.
#      Was it the submission process?
#          No, submission was easy.
# 5. How long did it take for you to complete the assignment?
#      One hour and fifteen minutes.

def houses_needed(houses_on_PA, houses_on_PC, houses_on_NC) -> int:
    if houses_on_PA == 5:
        houses_on_PA = 4
    if houses_on_PC == 5:
        houses_on_PC = 4
    if houses_on_NC == 5:
        houses_on_NC = 4

    houses_needed = 12 - houses_on_PA - houses_on_PC - houses_on_NC
    return houses_needed

print()

if input("Do you own all the green properties? (y/n) ").lower() != 'y':
    print("You cannot purchase a hotel until you own "
          "all the properties of a given color group.")

else:
    houses_on_PA = int(input("What is on Pennsylvania Avenue? "
                             "(0:nothing, 1:one house, ... 5:a hotel) "))

    if houses_on_PA == 5:
        print("You cannot purchase a hotel if the property already has one.")

    else:
        houses_on_PC = int(input("What is on Pacific Avenue "
                                 "(0:nothing, 1:one house, ... 5:a hotel) "))
        houses_on_NC = int(input("What is on North Carolina Avenue "
                                 "(0:nothing, 1:one house, ... 5:a hotel) "))
        houses_available = int(
            input("How many houses are there to purchase? "))
        hotels_available = int(
            input("How many hotels are there to purchase? "))

        houses_to_buy = houses_needed(houses_on_PC, houses_on_PA, houses_on_NC)
        if houses_to_buy > houses_available:
            print("There are not enough houses available for purchase at this time.")
        elif hotels_available < 1 and houses_on_NC < 5 and houses_on_PC < 5:
            print("There are not enough hotels available for purchase at this time.")
        else:
            cash = int(input("How much cash do you have to spend? "))
            if cash > (houses_to_buy + 1) * 200 and hotels_available > 0:
                if houses_on_NC < 4:
                    if houses_on_PC < 4:
                        print(f"This will cost ${(houses_to_buy + 1) * 200}.\n"
                              f"\tPurchase 1 hotel and {houses_to_buy} house(s).\n"
                              f"\tPut 1 hotel on Pennsylvania and return any houses to the bank.\n"
                              f"\tPut {4 - houses_on_NC} house(s) on North Carolina.\n"
                              f"\tPut {4 - houses_on_PC} house(s) on Pacific.")
                    else:
                        print(f"This will cost ${(houses_to_buy + 1) * 200}.\n"
                              f"\tPurchase 1 hotel and {houses_to_buy} house(s).\n"
                              f"\tPut 1 hotel on Pennsylvania and return any houses to the bank.\n"
                              f"\tPut {4 - houses_on_NC} house(s) on North Carolina.")
                else:
                    if houses_on_PC < 4:
                        print(f"This will cost ${(houses_to_buy + 1) * 200}.\n"
                              f"\tPurchase 1 hotel and {houses_to_buy} house(s).\n"
                              f"\tPut 1 hotel on Pennsylvania and return any houses to the bank.\n"
                              f"\tPut {4 - houses_on_PC} house(s) on Pacific.")
                    else:
                        print(f"This will cost ${(houses_to_buy + 1) * 200}.\n"
                              f"\tPurchase 1 hotel and {houses_to_buy} house(s).\n"
                              f"\tPut 1 hotel on Pennsylvania and return any houses to the bank.")
            else:
                if houses_on_NC == 5:
                    print("Swap North Carolina's hotel with Pennsylvania's 4 houses.")
                elif houses_on_PC == 5:
                    print("Swap Pacific's hotel with Pennsylvania's 4 houses.")
                else:
                    print(
                        "You do not have sufficient funds to purchase a hotel at this time.")
print()