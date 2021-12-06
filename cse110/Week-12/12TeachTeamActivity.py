import time

chosen_volume = input("Which volume of scripture would you like to learn about? ")
print()
time.sleep(0.5)
max_chapters = -1
book_with_max = ""
with open("cse110/Week-12/books_and_chapters.txt") as file:
    for line in file:
        parts = line.split(":")
        book = parts[0].strip()
        chapters = int(parts[1])
        scripture = parts[2].strip()
        if scripture.lower() == chosen_volume.lower():
            print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapters}")
            if chapters > max_chapters:
                max_chapters = chapters
                book_with_max = book
        time.sleep(0.01)
print(f"\nThe book with the most chapters in the {chosen_volume} is: {book_with_max}")
print(f"It has {max_chapters} chapters.")