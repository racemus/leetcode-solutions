from typing import Optional, List, Dict, Set
from collections import defaultdict

# def treeFromEdges(edges: List[List[int]]) -> Dict[str, Set[str]]:
#     '''
#     It creates tree in dict with parent nodes as keys and sets of children nodes as
#     values
#     N.B. I had to make not a tree, but two-ways undirected graph.
#     '''
#     nodes = {}
#     for edge in edges:
#         if str(edge[0]) not in nodes:
#             nodes[str(edge[0])] = {str(edge[1])}
#         else:
#             nodes[str(edge[0])].add(str(edge[1]))
#     return nodes

# def nodeHasApples(tree: Dict[str, Set[str]], node: str, hasApple: List[bool],
#     results: List[bool]=None) -> bool:
#     '''
#     It checks are there any apples in provided node and lower in tree.
#     '''
#     if results == None:
#         results = []
#     results.append(hasApple[int(node)])
#     if node in tree:
#         for next_node in tree[node]:
#             nodeHasApples(tree, next_node, hasApple, results)
#     return any(results)

##### better check with graph function
# def minTime(n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
#     '''
#     It creates tree from edges with treeFromEdges() and checks its nodes using pre-order
#     traversal with nodeHasApples()
#     '''
#     if sum(hasApple) == 0:
#         return 0
#     tree = treeFromEdges(edges)
#     print(tree)
#     stack = ['0']
#     result = -2
#     path = set()

#     while stack:
#         # print('stack:', stack)
#         node = stack.pop(0)

#         if nodeHasApples(tree, node, hasApple):
#             print('node:', node, 'nodeHasApples:', nodeHasApples(tree, node, hasApple))
#             result += 2
#             # print(result)
#             # path.append(node)
#             if node in tree:
#                 stack.extend(sorted(tree[node]))
#             # for subnode in tree[node]:
#             #     if subnode
#             # if node in 
#             # print(stack)

#     return result

def minTime(n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
    '''
    It backs to handle functions, but works with edges. It still have LTE on leetcode.com
    on "very big" test case. It solved it in terminal, but I don't know the answers was
    right or not. Anyway it needs to rework with graph fuction instead of tree and maybe
    combine with previous one.
    '''
    # if sum(hasApple) == 0:
    #     return 0
    counter = 0
    # checked = [0]

    ends = [edge[1] for edge in edges]
    ends.append(0)
    # print(ends)

    for i in range(len(edges)):
        if edges[i][0] not in ends:
            edges[i] = [edges[i][1],edges[i][0]]
    # print(edges)
    tree = treeFromEdges(edges)
    # print(tree)
    for edge in edges:
        # print('edge #1:', edge, 'cheking node:', edge[1], 'counter', counter)
        # print('nodeHasApples:', nodeHasApples(tree, str(edge[1]), hasApple))
        # if edge[0] in checked:
        if nodeHasApples(tree, str(edge[1]), hasApple):
            counter += 2
            # checked.append(edge[0]) if edge[0] not in checked else checked
            # checked.append(edge[1]) if edge[1] not in checked else checked
        # print('edge #2:', edge, 'counter', counter)
    return counter

# print(treeFromEdges([[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]))
# print(treeFromEdges([[0,1],[0,2],[1,4],[1,5],[2,3],[2,6],[4,7],[4,8],[5,9],[5,10],[7,11],[7,12]]))

# print(nodeHasApples(tree, '6', [False,False,True,False,True,True,False]))

print(minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,True,True,False])) # 8
print(minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,False,True,False])) # 6
print(minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,True,True,False,False,False,False])) # 4
print(minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,False,False,False,False,False])) # 0
print(minTime(7, [[0,1],[1,2],[2,3],[2,4],[3,5],[0,6]], [True,False,False,False,True,False,False])) # 6
print(minTime(6, [[0,1],[0,2],[1,3],[3,4],[4,5]], [False,True,False,False,True,True])) # 8
print(minTime(3, [[0,2],[0,3],[1,2]], [False,True,False,False])) # 4