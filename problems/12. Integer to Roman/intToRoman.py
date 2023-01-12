def intToRoman(num: int) -> str:
    '''
    It iterates through reversed dictionary of all variations for converting from roman
    string as keys to integer as values where it creates the result string
    '''
    result = ''
    # map = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50,
    #        'XC':90, 'C':100, 'CD':400, 'D':500, 'CM':900,'M':1000}
    # map = dict(sorted(map.items(), key=lambda x: x[1], reverse=True))
    map = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100,'XC':90,
           'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}
    
    for key,v in map.items():
        result += key * (num // v)
        num %= v 
    
    return result

print(intToRoman(3)) # III
print(intToRoman(58)) # LVIII
print(intToRoman(1994)) # MCMXCIV