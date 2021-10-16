import math

# Pythagorean theorem
a = -9.09 # length 1
b = -0.3 # length 2
c = math.sqrt(a ** 2 + b ** 2) # hypotenuse
print(c)

# distance equation
d = 30.0
t = 3.0
s = d + a * t
print(s)

# distance with acceleration
g = -1.625
s = d + a * t + 0.5 * g * t ** 2
print(s)

# Lander force or acceleration
tr = 45000
w = 15.103
la = 45000 / 15103
print(la)

# Total acceleration
ta = la + g
print(f"Total acceleration = {ta}")

# Distance with total acceleration
s = d + a * t + 0.5 * ta * t ** 2
print(f"Total distance = {s}")

# kinematic equation
under_sqrt = (a ** 2) - (4 * (0.5 * ta) * 30)
yp = (-a + math.sqrt(under_sqrt)) / (2 * 0.5 * ta)
yn = (-a - math.sqrt(under_sqrt)) / (2 * 0.5 * ta)
print(f"Value under the square root: {under_sqrt}")
print(f"Time one: {yp}")
print(f"Time two: {yn}")