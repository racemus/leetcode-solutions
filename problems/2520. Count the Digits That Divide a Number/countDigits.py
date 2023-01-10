def countDigits(num: int) -> int:
    result = 0
    num_str = str(num)
    
    for i in num_str:
        if num % int(i) == 0:
            result += 1
    
    return result

print(countDigits(7)) # 1
print(countDigits(121)) # 2
print(countDigits(1248)) # 4