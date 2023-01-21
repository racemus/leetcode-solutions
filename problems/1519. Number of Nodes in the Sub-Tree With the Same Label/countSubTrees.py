from typing import Optional, List, Dict, Set
from collections import defaultdict
import unittest

def graphFromEdges(edges: List[List[int]]) -> Dict[str, Set[str]]:
    '''
    It creates an two-ways undirected graph in dict with nodes as keys and sets of
    connected nodes as values
    '''
    nodes = defaultdict(set)

    for edge in edges:
        ### ordinary dict
        # nodes.setdefault(str(edge[0]), {str(edge[1])}).add(str(edge[1]))
        # nodes.setdefault(str(edge[1]), {str(edge[0])}).add(str(edge[0]))
        
        nodes[str(edge[0])].add(str(edge[1]))
        nodes[str(edge[1])].add(str(edge[0]))

    return nodes

def treeFromEdges(edges: List[List[int]]) -> Dict[str, Set[str]]:
    '''
    It creates tree in dict with parent nodes as keys and sets of children nodes as
    values
    '''
    nodes = defaultdict(set)

    for edge in edges:
        ### ordinary dict
        # nodes.setdefault(str(edge[0]), {str(edge[1])}).add(str(edge[1]))

        nodes[str(edge[0])].add(str(edge[1]))

    return nodes

def countLabeledNodes(graph: Dict[str, Set[str]], node: str, labels: str,
    results: List[bool]=None, seen: List[bool]=None) -> int:
    '''

    '''
    if results == None:
        results = []
    if seen == None:
        seen = set()
    results.append(labels[int(node)])
    if node in graph:
        seen.add(node)

        for con_node in graph[node] - seen:
            countLabeledNodes(graph, con_node, labels, results, seen)

    return results.count(labels[int(node)])

class Solution:
    '''
    
    '''
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = graphFromEdges(edges)
        print(graph)
        results = []
        seen = set()

        for node in graph:
            if node not in seen:
                seen.add(node)
            print('node:', node, 'labels:', labels, 'countLabeledNodes:', countLabeledNodes(graph, node, labels))
            results.append(countLabeledNodes(graph, node, labels))

        return results

### DFS solution example
# class Solution:
#     '''
#     - It builds the graph from edges.
#     - It traverses a tree by recursion, keeping track of each node's parent so it doesn't
#       revisit already visited node.
#     - During the traversal, it keeps track of the label counts in result.
#     - Once the travesal is completed, it returns result.
#     '''
#     def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
#         self.labels = labels
#         self.graph = defaultdict(list)
#         self.labelCount = defaultdict(int)
#         self.result = [0] * n
        
#         for a, b in edges:
#             self.graph[a].append(b)
#             self.graph[b].append(a)

#         self.dfs()
#         return self.result
        
#     def dfs(self, node=0, parent=None):
#         previous = self.labelCount[self.labels[node]]
#         self.labelCount[self.labels[node]] += 1
        
#         for child in self.graph[node]:
#             if child != parent: self.dfs(child, node)

#         self.result[node] = self.labelCount[self.labels[node]] - previous


# class Solution:
#     def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
#         self.seen = set()
#         self.graph = defaultdict(list)
#         self.result = []

#         for a, b in edges: 
#             self.graph[a].append(b)
#             self.graph[b].append(a)

#         return self.dfs(0)
           
#     def dfs(self, node: int)->int:
#         self.seen.add(node)    
#         result.append(self.dfs(n) for n in self.graph[node] if n not in self.seen) 
#         if not self.result and not hasApple[node]:
#             return 0

#         return result.count(labels[node])

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(graphFromEdges([[0,2],[0,3],[1,2]]),
            {'0': {'2', '3'}, '2': {'0', '1'}, '3': {'0'}, '1': {'2'}})

    def test_2(self):
        self.assertEqual(graphFromEdges([[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]),
            {'0': {'2', '1'}, '1': {'0', '5', '4'}, '2': {'0', '6', '3'}, '4': {'1'},
            '5': {'1'}, '3': {'2'}, '6': {'2'}})

    def test_3(self):
        self.assertEqual(graphFromEdges([[0,1],[0,2],[1,4],[1,5],[2,3],[2,6],[4,7],[4,8],[5,9],[5,10],[7,11],[7,12]]),
            {'0': {'2', '1'}, '1': {'0', '5', '4'}, '2': {'0', '6', '3'}, '4': {'7', '1', '8'}, '5': {'9', '1', '10'},
            '3': {'2'}, '6': {'2'}, '7': {'12', '11', '4'}, '8': {'4'}, '9': {'5'}, '10': {'5'}, '11': {'7'}, '12': {'7'}})

    def test_4(self):
        self.assertEqual(treeFromEdges([[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]),
            {'0': {'1', '2'}, '1': {'5', '4'}, '2': {'3', '6'}})

    def test_5(self):
        graph = treeFromEdges([[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]])
        self.assertEqual(countLabeledNodes(graph, '2', 'abaedcd'), 1)

    def test_6(self):
        self.assertEqual(self.solution.countSubTrees(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],
            'abaedcd'), [2,1,1,1,1,1,1])

    def test_7(self):
        self.assertEqual(self.solution.countSubTrees(4, [[0,1],[1,2],[0,3]], 'bbbb'),
            [4,2,1,1])
    
    def test_8(self):
        self.assertEqual(self.solution.countSubTrees(5, [[0,1],[0,2],[1,3],[0,4]],
            'aabab'), [3,2,1,1,1])
    
    def test_9(self):
        self.assertEqual(self.solution.countSubTrees(4, [[0,2],[0,3],[1,2]], 'aeed'),
            [1,1,2,1])

if __name__ == '__main__':
    unittest.main()