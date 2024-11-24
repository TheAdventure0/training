numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for x in numbers:
    is_prime = True
    if x == 1:
        continue
    for i in range(2, x):
        if x % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(x)
    else:
        not_primes.append(x)

print("primes:", primes)
print("not_primes:", not_primes)
