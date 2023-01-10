def findMinArrowShots(points: list[list[int]]) -> int:
    ''' It sorts list by end point in child lists and iterates by both points to find
        intersections '''
    points = sorted(points, key = lambda x: x[1])
    result = 0
    last_max = -float('inf')
    
    for start, end in points:
        if start > last_max:
            result += 1
            last_max = end
    
    return result

print(findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])) # 2
print(findMinArrowShots([[1,2],[3,4],[5,6],[7,8]])) # 4
print(findMinArrowShots([[1,2],[2,3],[3,4],[4,5]])) # 2
print(findMinArrowShots([[1,2]])) # 1
print(findMinArrowShots([[-1,1],[0,1],[2,3],[1,2]])) # 2
print(findMinArrowShots([[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]])) # 2