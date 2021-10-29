print("\n\n\n")

from PIL import Image
image = Image.open("cse110/week-7/cse110_images/beach.jpg")
# image.show()
pixels = image.load()
pixels[400, 300] = (0, 0, 0)
# image.show()
(width, height) = image.size
for column in range(width):
    pixels[column, 300] = (0, 0, 0)
# image.show()
for row in range(height):
    pixels[400, row] = (255, 0, 0)

# image.show()

image = Image.open("cse110/week-7/cse110_images/beach.jpg")
pixels = image.load()
for row in range(height):
    for column in range(width):
        (r, g, b) = pixels[column, row]
        pixels[column, row] = (r // 2, g // 2, b // 2)
# image.show()

image = Image.open("cse110/week-7/cse110_images/beach.jpg")
pixels = image.load()
for row in range(height):
    for column in range(width):
        (r, g, b) = pixels[column, row]
        average = (r + g + b) // 3
        pixels[column, row] = (average, average, average)
# image.show()

image = Image.open("cse110/week-7/cse110_images/beach.jpg")
pixels = image.load()
for row in range(height):
    for column in range(width):
        (r, g, b) = pixels[column, row]
        if (r + g + b) > 350:
            pixels[column, row] = (0, 0, 0)
image.show()