def maxIceCream(costs: list[int], coins: int) -> int:
    ''' It iterates through sorted costs, collect bought ice-cream prices and
        returns its lenght'''
    if min(costs) > coins:
        return 0
    if sum(costs) < coins:
        return len(costs)
    costs.sort()
    i = 0
    bought = []
    while i < len(costs) and sum(bought) <= coins:
        bought.append(costs[i])
        i += 1
    return len(bought[:-1])

print(maxIceCream([1,3,2,4,1], 7)) # 4 (1,3,2,1)
print(maxIceCream([10,6,8,7,7,8], 5)) # 0 (cannot afford)
print(maxIceCream([1,6,3,1,2,5], 20)) # 6 (all)