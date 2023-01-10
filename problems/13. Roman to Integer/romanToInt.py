def romanToInt(s: str) -> int:
    roman_dict = {'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000}
    roman_comb_dict = {'IV': 4,
                       'IX': 9,
                       'XL': 40,
                       'XC': 90,
                       'CD': 400,
                       'CM': 900}
    result = 0
    i = 0

    while i < len(s):
        if s[i:i+2] in roman_comb_dict:
            result += roman_comb_dict[s[i:i+2]]
            i += 2
        else:
            result += roman_dict[s[i]]
            i += 1

    return result

print(romanToInt('III')) # 3
print(romanToInt('LVIII')) # 58
print(romanToInt('MCMXCIV')) # 1994