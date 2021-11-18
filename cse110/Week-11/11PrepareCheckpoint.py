with open("cse110/Week-11/books.txt") as book_file:
    for line in book_file:
        book = line.strip()
        print(book)