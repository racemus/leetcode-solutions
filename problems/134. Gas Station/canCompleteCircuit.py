def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    ''' It iterates through range of doubled length of list to cycle over again
        and checks the start point of iterate that lasts by length of list cycles '''
    if sum(gas) < sum(cost):
        return - 1
    start_point = 0
    tank = 0
    
    for i in range(len(gas) * 2):
        tank += gas[i%len(gas)] - cost[i%len(gas)]
        if tank < 0:
            start_point = (i + 1) % len(gas)
            tank = 0
        if i >= start_point + len(gas):
            return start_point
    
    return -1

print(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])) # 3
print(canCompleteCircuit([1,7,3,4,5,1,7], [7,4,7,2,3,1,4])) # 3
print(canCompleteCircuit([2,3,4], [3,4,3])) # -1