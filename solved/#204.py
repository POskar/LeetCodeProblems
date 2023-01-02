#204. Count Primes

import math


def countPrimes(self, n: int) -> int:
    primes = [0,0] + [1 for x in range(0,n-2)]
    for i in range(2, math.isqrt(n) + 1):
        if primes[i]:
            w = i*i
            while w < n:
                primes[w] = 0
                w += i

    return sum(primes)

n = 1000
print(countPrimes(0, n))