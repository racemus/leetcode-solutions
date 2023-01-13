from typing import Optional, List, Dict, Set
from collections import defaultdict

def graphFromEdges(edges: List[List[int]]) -> Dict[str, Set[str]]:
    '''
    It creates an two-ways undirected graph in dict with nodes as keys and sets of
    connected nodes as values
    '''
    nodes = {}

    for edge in edges:
        nodes.setdefault(str(edge[0]), {str(edge[1])}).add(str(edge[1]))
        nodes.setdefault(str(edge[1]), {str(edge[0])}).add(str(edge[0]))
        
    return nodes

def treeFromEdges(edges: List[List[int]]) -> Dict[str, Set[str]]:
    '''
    It creates tree in dict with parent nodes as keys and sets of children nodes as
    values
    '''
    nodes = {}

    for edge in edges:
        nodes.setdefault(str(edge[0]), {str(edge[1])}).add(str(edge[1]))

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

def countSubTrees(n: int, edges: List[List[int]], labels: str) -> List[int]:
    '''

    '''
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


# print(graphFromEdges([[0,2],[0,3],[1,2]]))
# print(graphFromEdges([[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]))
# print(graphFromEdges([[0,1],[0,2],[1,4],[1,5],[2,3],[2,6],[4,7],[4,8],[5,9],[5,10],[7,11],[7,12]]))


# graph = treeFromEdges([[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]])
# print(graph)
# print(countLabeledNodes(tree, '2', 'abaedcd'))

print(countSubTrees(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], 'abaedcd')) # [2,1,1,1,1,1,1]
# print(countSubTrees(4, [[0,1],[1,2],[0,3]], 'bbbb')) # [4,2,1,1]
# print(countSubTrees(5, [[0,1],[0,2],[1,3],[0,4]], 'aabab')) # [3,2,1,1,1]
# print(countSubTrees(5, [[0,2],[0,3],[1,2]], 'aeed')) # [1,1,2,1]