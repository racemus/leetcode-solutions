def wordPattern(pattern: str, s: str) -> bool:
    '''
    It puts every pair of letter from pattern and word from s to dictionary in iteration
    like creating paring rules and compares every new pair with this rules on next
    iterations
    '''
    pattern_dict = {}
    pattern_list = [*pattern]
    s_list = s.split()
    if (len(pattern_list) != len(s_list)) or (len(set(pattern_list)) != len(set(s_list))):
        return False
    
    for i in range(len(pattern_list)):
        if (pattern_list[i] in pattern_dict) and (pattern_dict[pattern_list[i]] != s_list[i]):
            return False
        else:
            pattern_dict[pattern_list[i]] = s_list[i]
    
    return True

print(wordPattern('abba', 'dog cat cat dog')) # True
print(wordPattern('abba', 'dog cat cat fish')) # False
print(wordPattern('aaaa', 'dog cat cat dog')) # False
print(wordPattern('aba', 'cat cat cat dog')) # False