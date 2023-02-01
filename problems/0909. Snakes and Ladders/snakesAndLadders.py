class Solution:
	'''
	My first try. Doesn't work yet!
	'''
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        plain_way = []
        graph = defaultdict(set)
        board_temp = board.copy()
        board_temp.reverse()
        
        for i in range(len(board_temp)):
            if i%2 == 0:
                plain_way += board_temp[i]
            else:
                board_temp[i].reverse()
                plain_way += board_temp[i]

        for a in range(1, len(plain_way)):
            for b in range(a + 1, min(a + 7, len(plain_way) + 1)):
                if plain_way[b-1] == -1:
                    graph[a].add(b)
                else:
                    graph[a].add(plain_way[b-1])
        print(graph)

        def bfs(graph, start, end):
            queue = []
            visited = set()
            queue.append([start])
            visited.add(start)

            while queue:
                path = queue.pop(0)
                node = path[-1]
                if node == end:
                    return path

                for adjacent in graph.get(node, []):
                    if adjacent not in visited:
                        visited.add(adjacent)
                        new_path = list(path)
                        new_path.append(adjacent)
                        queue.append(new_path)

        result = bfs(graph, 1, len(plain_way))
        print(result)
        if not result:
            return -1
        else:
            return len(result) - 1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self): 
        self.assertEqual(self.solution.snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]), 4)

    def test_2(self):
        self.assertEqual(self.solution.snakesAndLadders([[-1,-1],[-1,3]]), 1)
    
    def test_3(self):
        self.assertEqual(self.solution.snakesAndLadders([[1,1,-1],[1,1,1],[-1,1,1]]), -1)

if __name__ == '__main__':
    unittest.main()