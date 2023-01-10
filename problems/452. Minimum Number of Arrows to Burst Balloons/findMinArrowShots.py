def findMinArrowShots(points: list[list[int]]) -> int:
    ''' It sorts list by start point in child lists and iterates from the second one
        to find intersecting baloons, but it has a flaw: it shoud start with
        result = 1 to cover the last uncounted ballon '''
    if len(points) <= 1:
        return len(points)
    sorted_points = sorted(points)
    result = 1
    max_points = [sorted_points[0][1]]

    for i in range(len(sorted_points) - 1):
        min_point = sorted_points[i+1][0]
        if min_point > min(max_points):
            result += 1
            max_points = [sorted_points[i+1][1]]
        max_points.append(sorted_points[i+1][1])

    return result

print(findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])) # 2
print(findMinArrowShots([[1,2],[3,4],[5,6],[7,8]])) # 4
print(findMinArrowShots([[1,2],[2,3],[3,4],[4,5]])) # 2
print(findMinArrowShots([[1,2]])) # 1
print(findMinArrowShots([[-1,1],[0,1],[2,3],[1,2]])) # 2
print(findMinArrowShots([[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]])) # 2