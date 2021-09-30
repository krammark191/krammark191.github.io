import math
import time

# User input and variable allocation.
price_for_child_meal = float(input("What is the price of a child's meal? "))
price_for_adult_meal = float(input("What is the price of an adult's meal? "))
number_of_children = int(input("How many children are there? "))
number_of_adults = int(input("How many adults are there? "))
sales_tax_rate = float(input("What is the sales tax rate? "))

# Calculations for subtotal, tax, and total with .2f precision.
subtotal = (float(number_of_children) * price_for_child_meal) + (float(number_of_adults) * price_for_adult_meal)
print(f"\nSubtotal: ${subtotal:.2f}")
sales_tax = (sales_tax_rate * subtotal) / 100
print(f"Sales Tax: ${sales_tax:.2f}")
total = subtotal + sales_tax
print(f"Total: ${total:.2f}\n")

# User input for payment. If user input is insufficient, program prompts for additional funds.
payment_amount = float(input("What is the payment amount? "))
while payment_amount < total:
    additional_funds = float(input(f"Your current balance of ${payment_amount:.2f} is not enough, please enter additional funds: "))
    payment_amount += additional_funds
    if payment_amount >= total:
        print(f"Your balance of ${payment_amount:.2f} is sufficient, enjoy your meal!\n")

# Calculation and print statement for change.
change_amount = payment_amount - total
print(f"Change: ${change_amount:.2f}")