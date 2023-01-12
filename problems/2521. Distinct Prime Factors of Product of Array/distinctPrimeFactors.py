import math
from typing import List

def distinctPrimeFactors(nums: List[int]) -> int:
    '''
    It iterates over list of numbers and finds all prime factors for all numbers in list
    '''
    result = set()
    
    for num in nums:
        sq_num = int(math.sqrt(num))
        
        for i in range(2, sq_num +1):
            if num % i == 0:
                result.add(i)
                while num % i == 0:
                    num //= i
        
        if num >= 2:
            result.add(num)
    
    return len(result)
                        
print(distinctPrimeFactors([2,4,3,7,10,6])) # 4 (2, 3, 5, 7)
print(distinctPrimeFactors([2,4,8,16])) # 1 (2)