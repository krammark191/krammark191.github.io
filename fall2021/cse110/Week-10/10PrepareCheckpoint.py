print("\nPlease enter the items of the shopping list (type: quit to finish):")
item_list = []
item = str
while item != 'quit':
    item = input("Item: ")
    if item != 'quit':
        item_list.append(item)

def index_print():
    print("\nThe shopping list is:")
    for thing in item_list:
        print(thing)
index_print()

print("\nThe shopping list with indexes is:")
for item in range(len(item_list)):
    print(f"{item}. {item_list[item]}")

index_change = int(input("\nWhich item would you like to change? "))
item_change = input("What is the new item? ")
item_list[index_change] = item_change
index_print()