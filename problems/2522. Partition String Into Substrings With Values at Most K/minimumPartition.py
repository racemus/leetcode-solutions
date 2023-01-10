def minimumPartition(s: str, k: int) -> int:
    ''' It iterates through string and compare accumulating helper string with k.
        It has same flaw as my findMinArrowShots version that needs result = 1 at
        at start to cover last element of iteration. '''
    if int(s) == k:
            return 1
    result = 1
    compare = ''

    for l in s:
        if int(l) > k:
            return -1
        compare = compare + l
        if int(compare) >= k:
            result += 1
            compare = l

    return result

print(minimumPartition('165462', 60)) # 4 (16, 54, 6, 2)
print(minimumPartition('238182', 5)) # -1 (there are digits higher than 5)
print(minimumPartition('23456784325675432145', 15)) # 19 (2,3,4,5,6,7,8,4,3,2,5,6,7,5,4,3,2,14,5)
print(minimumPartition('1', 1)) # 1 (1)
print(minimumPartition('75734379996162298577', 7)) # -1 (there are digits higher than 7)