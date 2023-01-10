import itertools

def maxPoints(points: list[list[int]]) -> int:
    ''' It's my first try (don't work) '''
    count = 0
    max_count = 0
    if len(points) <= 2:
        return len(points)
    two_point_lines = itertools.combinations(points, 2)
    # print('two_point_lines:', two_point_lines)
    
    for line in two_point_lines:
        # print('line:', line)
        vect = [line[1][0] - line[0][0], line[1][1] - line[0][1]]
        # print('vect:', vect, 'for line:', line)
        # points_left = [p for p in points if p not in line]
        
        for point in points:
            first_line_point_compare = [point[0] - line[0][0], point[1] - line[0][1]]
            second_line_point_compare = [point[0] - line[1][0], point[1] - line[1][1]]
            print('first_line_point_compare:', first_line_point_compare, 'second_line_point_compare:', second_line_point_compare, 'for line:', line, 'vect:', vect, 'and point:', point)
            x_x_coef = vect[0] / first_line_point_compare[0] if first_line_point_compare[0] else 0
            x_y_coef = vect[1] / first_line_point_compare[1] if first_line_point_compare[1] else 0
            y_x_coef = vect[0] / second_line_point_compare[0] if second_line_point_compare[0] else 0
            y_y_coef = vect[1] / second_line_point_compare[1] if second_line_point_compare[1] else 0
            print('x_x_coef:', x_x_coef, 'x_y_coef:', x_y_coef)
            print('y_x_coef:', y_x_coef, 'y_y_coef:', y_y_coef)
            # if (x_x_coef == 0 or x_y_coef == 0 or y_x_coef == 0 or y_y_coef == 0
            #     and (x_x_coef == x_y_coef and y_x_coef == y_y_coef)):
            if ((x_y_coef == 0 and y_y_coef == 0) or (x_x_coef == 0 and y_x_coef == 0)
                or (x_x_coef == x_y_coef and y_x_coef == y_y_coef)):
            # if x_x_coef == x_y_coef and y_x_coef == y_y_coef:
                count += 1
                print('count:', count)
                # if [sum(x) for x in zip(vect, )]
        
        if max_count < count:
            max_count = count
        count = 0
    
    return max_count

print(maxPoints([[1,1],[2,2],[3,3]])) # 3
print(maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]])) # 4
print(maxPoints([[0,0]])) # 1
print(maxPoints([[1,0],[0,0]])) # 2
print(maxPoints([[2,3],[3,3],[-5,3]])) # 3