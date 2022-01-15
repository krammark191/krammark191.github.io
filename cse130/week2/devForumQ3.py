with open("name.txt", "w") as name_file:
    name = input("\nPlease enter your name: ")
    name_file.write(name.title())

with open("name.txt", "r") as name_file:
    print(f"\nYour name is {name_file.read()}.\n")