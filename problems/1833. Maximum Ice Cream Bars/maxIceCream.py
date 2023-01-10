def maxIceCream(costs: list[int], coins: int) -> int:
    ''' It iterates through sorted costs spending coins till it still avaliable '''
    costs.sort()
    for i in range(len(costs)):
        coins -= costs[i]
        if coins < 0:
            return i
    return i + 1

print(maxIceCream([1,3,2,4,1], 7)) # 4 (1,3,2,1)
print(maxIceCream([10,6,8,7,7,8], 5)) # 0 (cannot afford)
print(maxIceCream([1,6,3,1,2,5], 20)) # 6 (all)