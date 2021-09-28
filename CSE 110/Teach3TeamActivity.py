import math
import time

# This is for the square area function.
square_length = input("What is the length of a side of the square? ")
print("The area of the square is: " + str(float(square_length) ** 2))
time.sleep(1)

# This is for the rectangle area function.
rectangle_length = input("\nWhat is the length of the rectangle? ")
rectangle_width = input("What is the width of the rectangle? ")
print("The area of the reactangle is: " + str(float(rectangle_length) * float(rectangle_width)))
time.sleep(1)

# This is for the circle area function.
circle_radius = float(input("\nWhat is the radius of the circle? "))
circle_area = (circle_radius ** 2) * math.pi
print(f"The radius of the circle is: {str(circle_area)}\n")
time.sleep(1)

# This will prompt the user for a single value and output the area and volume of a square and circle.
single_value = float(input("Please enter a value to be used for a side and a radius: "))
time.sleep(1)
print(f"The area of a square is: {str(single_value ** 2)}")
print(f"The volume of a cube is: {str(single_value ** 3)}")
print(f"The area of a circle is: {str((single_value ** 2) * math.pi)}")
print(f"The volume of a sphere is: {str((4 / 3) * math.pi * (single_value ** 3))}\n")