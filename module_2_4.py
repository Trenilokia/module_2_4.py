numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in range(2, len(numbers) + 1):
    for k in range(2, len(numbers)):
        if i % k == 0 and i != k:
            is_prime = False
            break
        else:
            is_prime = True
    if is_prime == True:
        primes.append(i)
    else:
        not_primes.append(i)

print('Primes: ', primes)
print('Not Primes: ', not_primes)
