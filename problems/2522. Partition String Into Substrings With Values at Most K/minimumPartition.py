def minimumPartition(s: str, k: int) -> int:
    '''
    It iteratess through the s string with included iteration that checks digits until
    their combinations become higher than k or all digits checked.
    '''
    result = 0
    left = 0
    right = 0

    while right < len(s):

        while right < len(s) and int(s[left:right + 1]) <= k:
            right += 1
        result += 1
        if left == right:
            return -1
        left = right

    return result

print(minimumPartition('165462', 60)) # 4 (16, 54, 6, 2)
print(minimumPartition('238182', 5)) # -1 (there are digits higher than 5)
print(minimumPartition('23456784325675432145', 15)) # 19 (2,3,4,5,6,7,8,4,3,2,5,6,7,5,4,3,2,14,5)
print(minimumPartition('1', 1)) # 1 (1)
print(minimumPartition('75734379996162298577', 7)) # -1 (there are digits higher than 7)