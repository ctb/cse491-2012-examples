#! /usr/bin/env python

primes = []
def next_prime():
    if not primes:
        i = 2
    else:
        i = primes[-1]

    while 1:
        divisible = False
        for p in primes:
            if i % p == 0:
                divisible = True
                break

        if not divisible:
            primes.append(i)
            return i

        i += 1

if __name__ == '__main__':
    for i in range(20):
        print next_prime()
