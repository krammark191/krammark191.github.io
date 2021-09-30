import math

# This function asks the user for fahrenheit temperature input and outputs the celsius temperature.
fahrenheit_temperature = float(input("\nWhat is the temperature in fahrenheit? "))
celsius_temperature = (fahrenheit_temperature - 32) * (5 / 9)
if celsius_temperature <= 0:
    print(f"The temperature in celsius is {celsius_temperature:.1f} degrees. That's really cold!\n")
else:
    print(f"The temperature in celsius is {celsius_temperature:.1f} degrees.\n")