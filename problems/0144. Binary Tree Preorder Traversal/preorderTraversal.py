from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#  Ex: root = [1, 2,None, 3,4]
#         1
#        /
#       2
#      / \
#     3   4
#
#     node     node.left   node.right  stack    ans
#   –––––––––  –––––––––   –––––––––   ––––––  ––––––
#                                       [1]     []
#       1          2         None       [2]     [1]
#       2          3          4         [4,3]   [1,2]
#       3        None        None       [4]     [1,2,3]
#       4        None        None       [4]     [1,2,3,4]

def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    '''
    It is not recursive simple pre-order traversal solution
    '''
    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        if node:
            result.append(node.val)
            stack.append(node.right)
            stack.append(node.left)

    return result

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.right = n2
n2.left = n3

n4 = None

n5 = TreeNode(1)

n6 = TreeNode(1)
n7 = TreeNode(2)
n8 = TreeNode(3)
n9 = TreeNode(4)
n10 = TreeNode(5)
n11 = TreeNode(6)
n12 = TreeNode(7)
n6.left = n7
n6.right = n8
n7.left = n9
n7.right = n10
n8.left = n11
n8.right = n12

print(preorderTraversal(n1)) # [1, 2, 3]
print(preorderTraversal(n4)) # []
print(preorderTraversal(n5)) # [1]
print(preorderTraversal(n6)) # [1, 2, 4, 5, 3, 6, 7]