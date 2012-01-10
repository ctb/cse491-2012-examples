#! /usr/bin/env python

def divisible(i, primes):
    for p in primes:
        if i % p == 0:
            return True

    return False

def primes():
    primes = []
    i = 1
    while 1:
        i += 1
        while divisible(i, primes):
            i += 1
            
        yield i
        primes.append(i)
            
if __name__ == '__main__':
    for n, p in enumerate(primes()):
        print p
        if n >= 20: break
