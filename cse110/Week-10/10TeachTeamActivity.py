# Initialize variables.
print("\nEnter the names and balances of bank accounts (type: quit when done)")
account_names = []
account_balances = []
account_name = None

# Collects user input for account names and their balances.
while account_name != 'quit':
    account_name = input("What is the name of this account? ")
    if account_name != "quit":
        account_balance = float(input("What is the balance? "))
        account_names.append(account_name)
        account_balances.append(account_balance)

# Prints the account information and total for the user.
total = 0
print("\nAccount Information:")
for i in range(len(account_names)):
    print(f"{i}. {account_names[i]} - ${account_balances[i]:.2f}")
    total += account_balances[i]
print(f"\nTotal: ${total:.2f}")

# Average calculation.
sum = 0
for j in range(len(account_names)):
    sum += account_balances[j]
average = sum / len(account_balances)
print(f"Average: ${average:.2f}")

# Highest balance calculation.
highest_balance = 0
for l in range(len(account_balances)):
    if account_balances[l] > account_balances[highest_balance]:
        highest_balance = l
print(f"Highest balance: {account_names[l]} - ${account_balances[l]:.2f}\n")

# Update account option.
update_account = 'yes'
while update_account != "no":
    update_account = input("\nDo you want to update an account? ").lower()
    if update_account != 'no':
        account_number = int(input("What account index do you want to update? "))
        new_amount = float(input("What is the new amount? "))
        account_balances[account_number] = new_amount
        print("\nAccount Information:")
        for k in range(len(account_names)):
            print(f"{k}. {account_names[k]} - ${account_balances[k]:.2f}")
