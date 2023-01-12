import math
from typing import List

# def isPrime(n): # Strange prime chaking function; need to investigate
#     if (n <= 1):
#         return False
#     if (n <= 3):
#         return True
#     if (n % 2 == 0 or n % 3 == 0):
#         return False
#     i = 5
#
#     while(i * i <= n):
#         if (n % i == 0 or n % (i + 2) == 0):
#             return False
#         i = i + 6
#
#     return True

def isPrime(n): # interesting to check its perfomance when math.sqrt in the iteration range
    if n <= 1:
        return False
    sq_n = int(math.sqrt(n))

    for i in range(2, sq_n + 1):
        if n % i == 0:
            return False

    return True

def closestPrimes(left: int, right: int) -> List[int]:
    '''
    It iterates through all integers between left and right included and collect all
    primes to list, and when it becomem bigger than 2 primes, it also begins to check
    minimum delta betwen them to save time. If there is no quick win, it iteretes through
    primes list to find the closest couple.
    '''
    primes = []
    delta = float('inf')
    
    for num in range(left, right+1):
        if isPrime(num):
            primes.append(num)
            if len(primes) >= 2 and primes[-1] - primes[-2] <= 2:
                return [primes[-2], primes[-1]]
    
    if len(primes) < 2:
        return [-1, -1]

    for i in range(len(primes)-1):
        if delta > primes[i+1] - primes[i]:
            delta = primes[i+1] - primes[i]
            result = [primes[i], primes[i+1]]
    
    return result

print(closestPrimes(10, 19)) # [11, 13]
print(closestPrimes(4, 6)) # [-1, -1] (no two primes between)
print(closestPrimes(344755, 763442)) # [344819, 344821]
print(closestPrimes(1, 1000000)) # [2, 3]
print(closestPrimes(69346, 69379)) # [69371, 69379]