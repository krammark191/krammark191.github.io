import math
import time

print ("\nWelcome to the velocity calculator. Please enter the following:\n")

# User input below, stored as floating point variables.
mass = float(input("Mass (in kg): "))
gravity = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
time_variable = float(input("Time (in seconds): "))
fluid_density = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
cross_sectional_area = float(input("Cross sectional area (in m^2): "))
drag_constant = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))
time.sleep(1)

# Calculates c (the force of drag against the object) and prints to console. c = 1/2*p*A*C
c = (1 / 2) * fluid_density * cross_sectional_area * drag_constant
print(f"\nThe inner value of c is: {c:.3f}")

# Calculates velocity and prints to console. velocity v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)*t))
velocity = math.sqrt(mass * gravity / c) * (1 - math.exp((-math.sqrt(mass * gravity * c) / mass) * time_variable))
print(f"The velocity after {time_variable:.1f} seconds is: {velocity:.3f} m/s\n")