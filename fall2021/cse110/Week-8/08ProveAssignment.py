from PIL import Image

image_original = Image.open("cse110/week-7/cse110_images/beach.jpg")
# image_original.show()

# Displays rgb values for different pixels.
width, height = image_original.size
pixels_original = image_original.load()
r, g, b = pixels_original[100, 200]
print(r, g, b)
r, g, b = pixels_original[300, 200]
print(r, g, b)
r, g, b = pixels_original[100, 0]
print(r, g, b)
r, g, b = pixels_original[150, 150]
print(r, g, b)
r, g, b = pixels_original[200, 100]
print(r, g, b)

# Changes rgb values for different pixels.
pixels_original[100, 200] = (255, 0, 255)
pixels_original[300, 200] = (0, 0, 0)
pixels_original[100, 0] = (2, 2, 2)
pixels_original[150, 150] = (200, 3, 85)
pixels_original[200, 100] = (255, 255, 255)

# image_original.show()
# image_original.save("cse110/week-7/cse110_images/image_original_copy.jpg")
# End of milestone.

# Beginning of assignment.
# Loads beach image and penguin image.
image_beach = Image.open("cse110/week-7/cse110_images/beach.jpg")
image_penguin = Image.open("cse110/week-7/cse110_images/penguin.jpg")
width_new, height_new = image_beach.size
pixels_new = image_beach.load()
pixels_alt = image_penguin.load()

# For loop that iterates through each pixel and determines whether to replace it or not.
for row in range(height):
    for column in range(width):
        (r, g, b) = pixels_alt[column, row]
        if g > 150 and r < 150 and b < 150:
            pixels_alt[column, row] = pixels_new[column, row]
image_penguin.save("cse110/week-7/cse110_images/image_penguin_on_beach.jpg")
image_penguin.show()

# Loads desert image and hiker image.
image_desert = Image.open("cse110/week-7/cse110_images/desert.jpg")
image_hiker = Image.open("cse110/week-7/cse110_images/hiker.jpg")
width_new, height_new = image_desert.size
pixels_new = image_desert.load()
pixels_alt = image_hiker.load()

# For loop that iterates through each pixel and determines whether to replace it or not.
for row in range(height):
    for column in range(width):
        (r, g, b) = pixels_alt[column, row]
        if g > 150 and r < 150 and b < 150:
            pixels_alt[column, row] = pixels_new[column, row]
image_hiker.save("cse110/week-7/cse110_images/image_hiker_in_desert.jpg")
image_hiker.show()

# Loads forest image and spaceshuttle image.
image_forest = Image.open("cse110/week-7/cse110_images/forest.jpg")
image_spaceshuttle = Image.open("cse110/week-7/cse110_images/spaceshuttle.jpg")
width_new, height_new = image_forest.size
pixels_new = image_forest.load()
pixels_alt = image_spaceshuttle.load()

# For loop that iterates through each pixel and determines whether to replace it or not.
for row in range(height):
    for column in range(width):
        (r, g, b) = pixels_alt[column, row]
        if g > 150 and r < 150 and b < 150:
            pixels_alt[column, row] = pixels_new[column, row]
image_spaceshuttle.save("cse110/week-7/cse110_images/image_spaceshuttle_in_forest.jpg")
image_spaceshuttle.show()