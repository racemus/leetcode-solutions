def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    ''' It iterates through range of length of list and checks the start point
        of iteration '''
    if sum(gas) - sum(cost) < 0:
        return -1
    start_point = 0
    tank = 0

    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start_point = i + 1
            tank = 0
      
    return start_point

print(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])) # 3
print(canCompleteCircuit([1,7,3,4,5,1,7], [7,4,7,2,3,1,4])) # 3
print(canCompleteCircuit([2,3,4], [3,4,3])) # -1