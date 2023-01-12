# First try. SOME TESTS NOT WORKING!

from typing import Optional, List, Dict, Set

def treeFromEdges(edges: List[List[int]]) -> Dict[str, Set[str]]:
    '''
    It creates tree in dict with parent nodes as keys and sets of children nodes as
    values
    N.B. I had to make not a tree, but two-ways undirected graph.
    '''
    nodes = {}
    for edge in edges:
        if str(edge[0]) not in nodes:
            nodes[str(edge[0])] = {str(edge[1])}
        else:
            nodes[str(edge[0])].add(str(edge[1]))
    return nodes

def nodeHasApples(tree: Dict[str, Set[str]], node: str, hasApple: List[bool],
    results: List[bool]=[]) -> bool:
    '''
    It checks are there any apples in provided node and lower in tree.
    '''
    results.append(hasApple[int(node)])
    if node in tree:
        for next_node in tree[node]:
            nodeHasApples(tree, next_node, hasApple, results)
    return any(results)

def minTime(n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
    '''
    It creates tree from edges with treeFromEdges() and checks its nodes using pre-order
    traversal with nodeHasApples()
    '''
    if sum(hasApple) == 0:
        return 0
    tree = treeFromEdges(edges)
    print(tree)
    stack = ['0']
    result = -2
    path = set()

    while stack:
        # print('stack:', stack)
        node = stack.pop(0)

        if nodeHasApples(tree, node, hasApple, []):
            print('node:', node, 'nodeHasApples:', nodeHasApples(tree, node, hasApple, []))
            result += 2
            # print(result)
            # path.append(node)
            if node in tree:
                stack.extend(sorted(tree[node]))
            # for subnode in tree[node]:
            #     if subnode
            # if node in 
            # print(stack)

    return result

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