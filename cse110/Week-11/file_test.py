with open("cse110/Week-11/data.txt") as file:
    for line in file:
        words = line.split(":")
        name = words[0]
        favorite_number = 0.0
        try:
            favorite_number = float(words[1])
        except:
            pass

        tithing = 0.0
        try:
            tithing = float(words[2]) / 10
        except:
            pass

        print(f"{name}, your tithing is ${tithing:.2f} and your favorite number is {favorite_number}")