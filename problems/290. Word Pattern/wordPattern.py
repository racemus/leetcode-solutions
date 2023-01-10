def createPattern(input):
    pattern_list = []
    pattern_code = []

    for element in input:
        if element not in pattern_list:
            pattern_list.append(element)
        pattern_code.append(pattern_list.index(element))    

    return pattern_code

def wordPattern(pattern: str, s: str) -> bool:
    return createPattern(pattern) == createPattern(s.split())

print(wordPattern('abba', 'dog cat cat dog')) # True
print(wordPattern('abba', 'dog cat cat fish')) # False
print(wordPattern('aaaa', 'dog cat cat dog')) # False
print(wordPattern('aba', 'cat cat cat dog')) # False