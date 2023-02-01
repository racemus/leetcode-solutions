from typing import List

def minDeletionSize(strs: List[str]) -> int:
    counter = 0
    columns_list = zip(*strs)
    
    for column in columns_list:
        column_sort = sorted(column)
        if column != tuple(column_sort):
            counter += 1
    
    return counter

print(minDeletionSize(["cba","daf","ghi"])) # 1
print(minDeletionSize(["a","b"])) # 0
print(minDeletionSize(["zyx","wvu","tsr"])) # 3