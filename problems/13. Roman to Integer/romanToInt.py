def romanToInt(s: str) -> int:
    '''
    It iterates through roman string and adds values from dictionary to result checking
    4/9 rules
    '''
    roman_dict = {'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000}
    result = 0

    for i in range(len(s)):
        try:
            if roman_dict[s[i]] < roman_dict[s[i+1]]:
                result -= roman_dict[s[i]]
            else:
                result += roman_dict[s[i]]
        except:
            result += roman_dict[s[i]]

    return result

print(romanToInt('III')) # 3
print(romanToInt('LVIII')) # 58
print(romanToInt('MCMXCIV')) # 1994