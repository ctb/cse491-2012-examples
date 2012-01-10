#! /usr/bin/env python

class PrimeIterator(object):
    def __init__(self):
        self.primes = [2]

    def __iter__(self):
        return self

    def next(self):
        last_prime = self.primes[-1]

        i = last_prime
        while 1:
            i += 1

            divisible = False
            for p in self.primes:
                if i % p == 0:
                    divisible = True
                    break

            if not divisible:
                self.primes.append(i)
                break

        return last_prime
            
if __name__ == '__main__':
    primes = PrimeIterator()
    for n, p in enumerate(primes):
        print p
        if n >= 20: break
