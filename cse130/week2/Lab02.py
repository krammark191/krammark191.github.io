# 1. Name:
#      Mark Van Horn
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      This program is meant to read a JSON file and create two Python
#      lists out of it, then ask the user for a username and password
#      and check if they match against the lists.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was figuring out how to parse the JSON data into
#      Python lists. I've never worked with JSON files before so I had
#      to figure that out on my own. The syntax was a little tricky when
#      it came to the for loops, I'm used to every other language that
#      does for loops intuitively, so trying to get it right in Python
#      is always a bit tricky for me. I feel like I skipped one of the
#      steps that the instructions told me to do, but the program works
#      as intended so I'm going to assume that I didn't skip the step.
# 5. How long did it take for you to complete the assignment?
#      About 3 hours.

import json

# Read JSON file into Python string.
with open("C://git//krammark191.github.io//cse130//week2//Lab02.json") as file:
    json_data = json.load(file)

# Assign each JSON list into a python list.
usernames = []
for username in json_data['username']:
    usernames.append(username)

passwords = []
for password in json_data['password']:
    passwords.append(password)

# Ask user for username and password and store in corresponding variables.
print()
user_username = input("Username: ")
user_password = input("Password: ")

# Check to see if the user provided username and password match.
is_authenticated = False
for i in range(0, 13):
    if user_username == usernames[i]:
        if user_password == passwords[i]:
            print("You are authenticated!\n")
            is_authenticated = True

# Print error message if username and/or password are incorrect.
if is_authenticated == False:
    print("You are not authorized to use the system.\n")