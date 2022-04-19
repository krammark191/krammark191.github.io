letters = []
for letter in range(ord('a'), ord('z') + 1):
    letters.append(chr(letter))
# print(letters)

for row in range(8, 0, -1):
    print("   +--+--+--+--+--+--+--+--+")
    print(row, "  |", sep='', end='')
    for column in range(ord('a'), ord('i')):
        print(chr(column), row, "|", end='', sep='')
    print()
print("   +--+--+--+--+--+--+--+--+")
print("    a  b  c  d  e  f  g  h")