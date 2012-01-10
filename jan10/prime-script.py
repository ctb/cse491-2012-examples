#! /usr/bin/env python
primes = []

i = 2
while len(primes) < 20:
    divisible = False
    for p in primes:
        if i % p == 0:
            divisible = True
            break

    if not divisible:
        primes.append(i)
        print i

    i += 1
