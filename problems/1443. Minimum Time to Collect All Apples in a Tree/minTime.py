from typing import Optional, List, Dict, Set
from collections import defaultdict
import unittest

def treeFromEdges(edges: List[List[int]]) -> Dict[str, Set[str]]:
    '''
    It creates tree in dict with parent nodes as keys and sets of children nodes as
    values
    N.B. I had to make not a tree, but two-ways undirected graph.
    '''
    nodes = defaultdict(set)
    for edge in edges:
        ### if ... else easy reading
        # if str(edge[0]) not in nodes:
        #     nodes[str(edge[0])] = {str(edge[1])}
        # else:
        #     nodes[str(edge[0])].add(str(edge[1]))
        
        ### ordinary dict
        # nodes.setdefault(str(edge[0]), {str(edge[1])}).add(str(edge[1]))

        nodes[str(edge[0])].add(str(edge[1]))
    return nodes

def nodeHasApples(tree: Dict[str, Set[str]], node: str, hasApple: List[bool],
    results: List[bool]=None) -> bool:
    '''
    It checks are there any apples in provided node and lower in tree.
    '''
    if results == None:
        results = []
    results.append(hasApple[int(node)])
    if node in tree:
        for next_node in tree[node]:
            nodeHasApples(tree, next_node, hasApple, results)
    return any(results)

### This one needs fix for test #11. Better check it with graph function instead of tree
# class Solution:
#     '''
#     It creates tree from edges with treeFromEdges() and checks its nodes using pre-order
#     traversal with nodeHasApples()
#     '''
#     def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
#         if sum(hasApple) == 0:
#             return 0
#         tree = treeFromEdges(edges)
#         print(tree)
#         stack = ['0']
#         result = -2
#         path = set()

#         while stack:
#             # print('stack:', stack)
#             node = stack.pop(0)

#             if nodeHasApples(tree, node, hasApple):
#                 print('node:', node, 'nodeHasApples:', nodeHasApples(tree, node, hasApple))
#                 result += 2
#                 # print(result)
#                 # path.append(node)
#                 if node in tree:
#                     stack.extend(sorted(tree[node]))
#                 # for subnode in tree[node]:
#                 #     if subnode
#                 # if node in 
#                 # print(stack)

#         return result

# class Solution:
#     '''
#     It backs to handle functions, but works with edges. It still have LTE on leetcode.com
#     on "very big" test case. It solved it in terminal, but I don't know the answers was
#     right or not. Anyway it needs to rework with graph fuction instead of tree and maybe
#     combine with previous one.
#     '''
#     def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
#         # if sum(hasApple) == 0:
#         #     return 0
#         counter = 0
#         # checked = [0]

#         ends = [edge[1] for edge in edges]
#         ends.append(0)
#         # print(ends)

#         for i in range(len(edges)):
#             if edges[i][0] not in ends:
#                 edges[i] = [edges[i][1],edges[i][0]]
#         # print(edges)
#         tree = treeFromEdges(edges)
#         # print(tree)
#         for edge in edges:
#             # print('edge #1:', edge, 'cheking node:', edge[1], 'counter', counter)
#             # print('nodeHasApples:', nodeHasApples(tree, str(edge[1]), hasApple))
#             # if edge[0] in checked:
#             if nodeHasApples(tree, str(edge[1]), hasApple):
#                 counter += 2
#                 # checked.append(edge[0]) if edge[0] not in checked else checked
#                 # checked.append(edge[1]) if edge[1] not in checked else checked
#             # print('edge #2:', edge, 'counter', counter)
#         return counter

### DFS solution example
# class Solution:
#     def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
#         # Construct the tree using the edges.
#         # Since the tree is undricted, we need to add both directions in the tree.
#         # tree = {} # without defaultdict
#         tree = defaultdict(list)
        
#         for start, end in edges:
#             # tree.setdefault(start, []).append(end) # without defaultdict
#             # tree.setdefault(end, []).append(start) # without defaultdict
#             tree[start].append(end)
#             tree[end].append(start)
#         # print(tree)
        
#         # node is the current node we are examing.
#         # par is the node's direct parent node.
#         def dfs(node, parent):
#             result = 0
            
#             # Since it is a tree, there will be no cycles.
#             # However, the tree is undirected, which means one of the neighbor node is its
#             # parent node.
#             for pair in tree[node]:
#                 # Make sure we are not going backward to its parent node.
#                 if pair != parent:
#                     result += dfs(pair, node)

#             # case1, result != 0, this means we have found some apples down the tree
#             # case2, hasApple[node]==True, this means the current node has a apple on it
#             # In both cases, we will have to increase the result by 2.
#             # Adding 2 because we need 1 to get to this node and 1 going back
#             if result or hasApple[node]:
#                 return result + 2

#             # There is no apple on this node or down the tree, res should 0.
#             # In this case we don't want to come to this node at all, so return 0.
#             return result

#         # Following the dfs, you can see that when we coming back to node 0, if there are
#         # some apples in the tree, we added an extra 2 to the result, so we need to -2 here.
#         # In case there is no apples in this tree, dfs will return 0, but we can't return -2,
#         # so just return 0
#         return max(dfs(0,-1) - 2, 0)

class Solution:
    '''
    It is the simpliest solution with DFS (Depth-First Search) recursion and saving
    the set of visited nodes.

    - It builds a graph and initializes the seen set to track which nodes have been
      visited.
    - It starts at node = 0, as directed, and traverse the graph recursively. It
      returns when it hits a dead-end node, that is a node n for which all nodes in
      graph[n] have already been visited.
    '''
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.hasApple = hasApple
        self.seen = set()
        self.graph = defaultdict(list)

        for a, b in edges: 
            self.graph[a].append(b)
            self.graph[b].append(a)

        return max(self.dfs(0) - 2, 0)

    def dfs(self, node: int)->int:
        self.seen.add(node)
        # print('node:', node, 'seen:', seen)
        result = sum(self.dfs(v) for v in self.graph[node] if v not in self.seen)
        # print('#1:', 'node:', node, 'seen:', seen, 'result:', result)
        if not result and not self.hasApple[node]:
            # print('return 0')
            return 0
        # print('node:', node, 'seen:', seen, 'result:', result+2)
        return result + 2  

        self.tree = defaultdict(list)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(treeFromEdges([[0,2],[0,3],[1,2]]),
            {'0': {'2', '3'}, '1': {'2'}})
    
    def test_2(self):
        self.assertEqual(treeFromEdges([[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]),
            {'0': {'1', '2'}, '1': {'4', '5'}, '2': {'3', '6'}})
    
    def test_3(self):
        self.assertEqual(treeFromEdges([[0,1],[0,2],[1,4],[1,5],[2,3],[2,6],[4,7],[4,8],[5,9],[5,10],[7,11],[7,12]]),
            {'0': {'1', '2'}, '1': {'4', '5'}, '2': {'3', '6'}, '4': {'8', '7'}, '5': {'10', '9'}, '7': {'12', '11'}})
    
    def test_4(self):
        tree = treeFromEdges([[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]])
        self.assertEqual(nodeHasApples(tree, '6', [False,False,True,False,True,True,False]), False)
    
    #### graph: {0: [1, 2], 1: [0, 4, 5], 2: [0, 3, 6], 4: [1], 5: [1], 3: [2], 6: [2]}
    def test_5(self):
        self.assertEqual(self.solution.minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],
            [False,False,True,False,True,True,False]), 8)
    
    def test_6(self):
        self.assertEqual(self.solution.minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],
            [False,False,True,False,False,True,False]), 6)
    
    def test_7(self):
        self.assertEqual(self.solution.minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],
            [False,True,True,False,False,False,False]), 4)
    
    def test_8(self):
        self.assertEqual(self.solution.minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],
            [False,False,False,False,False,False,False]), 0)
    
    ##### graph: {0: [1, 6], 1: [0, 2], 2: [1, 3, 4], 3: [2, 5], 4: [2], 5: [3], 6: [0]}
    def test_9(self):
        self.assertEqual(self.solution.minTime(7, [[0,1],[1,2],[2,3],[2,4],[3,5],[0,6]],
            [True,False,False,False,True,False,False]), 6)
    
    ##### graph: {0: [1, 2], 1: [0, 3], 2: [0], 3: [1, 4], 4: [3, 5], 5: [4]}
    def test10(self):
        self.assertEqual(self.solution.minTime(6, [[0,1],[0,2],[1,3],[3,4],[4,5]],
            [False,True,False,False,True,True]), 8)
    
    ##### graph: {0: [2, 3], 2: [0, 1], 3: [0], 1: [2]}
    def test_11(self):
        self.assertEqual(self.solution.minTime(3, [[0,2],[0,3],[1,2]],
            [False,True,False,False]), 4)

if __name__ == '__main__':
    unittest.main()