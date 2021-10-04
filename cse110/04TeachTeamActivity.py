import math
import time

print ("\nWelcome to the velocity calculator. Please enter the following:\n")

# User input below.
mass = float(input("Mass (in kg): "))
gravity = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
time_variable = float(input("Time (in seconds): "))
fluid_density = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
cross_sectional_area = float(input("Cross sectional area (in m^2): "))
drag_constant = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

# Calculates c and prints to console.
c = (1 / 2) * fluid_density * cross_sectional_area * drag_constant
print(f"The inner value of c is: {c:.3f}")

# Calculates velocity and prints to console.