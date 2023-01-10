import itertools

def maxPoints(points: list[list[int]]) -> int:
    ''' It's creates a list of combinations of 2 points (minimum for a line) and then
        iterates over them and points to find triangles with zero area i.e. line with
        3 points '''
    count = 0
    max_count = 0
    if len(points) <= 2:
        return len(points)
    two_point_lines = itertools.combinations(points, 2)
    
    for line in two_point_lines:

        for point in points:
            if ((line[0][0] - point[0]) * (line[1][1] - point[1]) ==
                (line[1][0] - point[0]) * (line[0][1] - point[1])):
                count += 1
        
        # if max_count < count:
        #     max_count = count
        max_count = max(max_count, count)
        count = 0
    
    return max_count

print(maxPoints([[1,1],[2,2],[3,3]])) # 3
print(maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]])) # 4
print(maxPoints([[0,0]])) # 1
print(maxPoints([[1,0],[0,0]])) # 2
print(maxPoints([[2,3],[3,3],[-5,3]])) # 3