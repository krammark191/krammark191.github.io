primes = []
for number in range(1, 24):
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        primes.append(number)

print(f"\nFirst ten prime numbers: {primes}")
print(f"First three prime numbers: {primes[0:3]}")
print(f"Last three prime numbers: {primes[-3:]}")
print(f"Middle three prime numbers: {primes[4:7]}")