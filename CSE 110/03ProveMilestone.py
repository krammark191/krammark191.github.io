import math
import time

# User input and variable allocation.
price_for_child_meal = float(input("What is the price of a child's meal? "))
price_for_adult_meal = float(input("What is the price of an adult's meal? "))
number_of_children = int(input("How many children are there? "))
number_of_adults = int(input("How many adults are there? "))
sales_tax_rate = float(input("What is the sales tax rate? "))

# Calculations for subtotal, tax, and total.
subtotal = (float(number_of_children) * price_for_child_meal) + (float(number_of_adults) * price_for_adult_meal)
print(f"\n{subtotal:.2f}")