#!/usr/bin/env python3

import numpy as np
import math

# adding a comment for testing on github
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

primes = []
middles = []
for x in np.arange(1,(10**3)):
    result = is_prime(x)
    print(f"{x}: {result}")
    if is_prime(x):
        primes.append(x)

for prime in primes:
    #print(f"{bcolors.ENDC}{prime}", end=' ')
    try:
        if (prime > 5) and (primes[primes.index(prime)+1] == prime+2):
            middle = int((primes[primes.index(prime)+1] + prime)/2)
            middles.append(middle)
            #print(f"{bcolors.OKCYAN}{middle}", end=' ')
    except:
        continue

for n in range(len(middles)):
    try:
        diff = middles[n+1] - middles[n]
        if diff % 6 != 0:
            print(f"{middles[n+1]}-{middles[n]} =\t{diff}")
    except:
        continue
print()