N = int(input())

primes = [i for i in range(30 * N + 1)]
primes[1] = 0

i = 2
while i <= 30 * N:
    if primes[i] != 0:
        j = i + i
        while j <= 30 * N:
            primes[j] = 0
            j = j + i
    i += 1

primes = [i for i in primes if i != 0]
print(primes[N - 1])


