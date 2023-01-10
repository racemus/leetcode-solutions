from collections import Counter

def minimumRounds(tasks: list[int]) -> int:
    result = 0
    # tasks_set = set(tasks)
    # tasks_dict = {j:tasks.count(j) for j in tasks_set}
    tasks_dict = Counter(tasks)
    
    for k,v in tasks_dict.items():
        if v <= 1:
            return -1
        else:
            # result += v // 3 + (v % 3 > 0)
            result += (v + 2) // 3
    
    return result

print(minimumRounds([2,2,3,3,2,4,4,4,4,4])) # 4
print(minimumRounds([2,3,3])) # -1