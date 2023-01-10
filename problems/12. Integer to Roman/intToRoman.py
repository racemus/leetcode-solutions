def intToRoman(num: int) -> str:
    ''' It creates a string at first with no rules like roman 4, 9 etc. On the next step
        it correct this string to fit those rules '''
    roman_dict = {1: 'I',
                  5: 'V',
                  10: 'X',
                  50: 'L',
                  100: 'C',
                  500: 'D',
                  1000: 'M'}
    result = ''
    working_num = num
    
    for i in [1000, 100, 10, 1]:
        j = working_num // i
        if j > 0:            
            result += roman_dict[i]*j
            working_num -= i*j

    result = result.replace('CCCCCCCCC','CM').replace('CCCCC','D').replace('CCCC',
        'CD').replace('XXXXXXXXX','XC').replace('XXXXX','L').replace('XXXX',
        'XL').replace('IIIIIIIII','IX').replace('IIIII','V').replace('IIII','IV')

    return result

print(intToRoman(3)) # III
print(intToRoman(58)) # LVIII
print(intToRoman(1994)) # MCMXCIV