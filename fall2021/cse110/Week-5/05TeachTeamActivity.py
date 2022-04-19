# User input.
number_grade = int(input("\nWhat is your grade percentage? "))

#               0%   10%  20%  30%  40%  50%  60%  70%  80%  90%  100%
letter_grades = ['F', 'F', 'F', 'F', 'F', 'F', 'D', 'C', 'B', 'A', 'A']
letter_grade = letter_grades[number_grade // 10]

# Check for minus grade or plus grade.
sign = ""
if int(number_grade) % 10 < 3 and letter_grade != 'F':
    sign = "-"
elif int(number_grade) % 10 > 7 and letter_grade != 'A':
    sign = "+"

# Print statement based on grade.
print(f"Your grade is {letter_grade}{sign}.\n")