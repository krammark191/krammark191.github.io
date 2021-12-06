people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
youngest_person = ""
youngest_age = 100
for line in people:
    print(line)
    info = line.split(" ")
    print(f"Name: {info[0]}, Age: {info[1]}")
    if int(info[1]) < youngest_age:
        youngest_age = int(info[1])
        youngest_person = info[0]

print(f"The youngest person is {youngest_person} at age {youngest_age}.")