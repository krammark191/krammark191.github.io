from PIL import Image

image_original = Image.open("cse110/week-7/cse110_images/beach.jpg")
image_original.show()

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

pixels_original[100, 200] = (255, 0, 255)
pixels_original[300, 200] = (0, 0, 0)
pixels_original[100, 0] = (2, 2, 2)
pixels_original[150, 150] = (200, 3, 85)
pixels_original[200, 100] = (255, 255, 255)
image_original.show()

image_original.save("image_original_copy.jpg")

# End of milestone.
# image_new = Image.new("RGB", image_original.size)
# pixels_new = image_new.load()
# pixels_new[width, height] = (r, g, b)
