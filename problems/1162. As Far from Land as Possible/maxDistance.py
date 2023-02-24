class Solution:
    '''
    It creates the distance matrix with size of the original one and fill it with maximum
    distance possible. Then it uses BFS for each land cell and change the amount for each
    cell in distance matrix with maximum distance from the nearest land cell. In the end,
    it returns maximum distance from the distance matrix.
    '''
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        max_distance = 2 * n - 1
        matrix = [x[:] for x in [[max_distance] * n] * n]
        print(matrix)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = min(matrix[i][j], min(matrix[i-1][j] + 1 if i > 0
                        else max_distance, matrix[i][j-1] + 1 if j > 0 else max_distance))

        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[i]) - 1, -1, -1):
                matrix[i][j] = min(matrix[i][j], min(matrix[i+1][j] + 1 if i < n - 1
                    else max_distance, matrix[i][j+1] + 1 if j < n - 1 else max_distance))

        print(matrix)
        result = max([item for row in matrix for item in row])
        if result == 0 or result == max_distance:
            return -1
        else:
            return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.maxDistance([[1,0,1],[0,0,0],[1,0,1]]), 2)

    def test_2(self):
        self.assertEqual(self.solution.maxDistance([[1,0,0],[0,0,0],[0,0,0]]), 4)

if __name__ == '__main__':
    unittest.main()