from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root: Optional[TreeNode]) -> list[int]:
    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        if node:
            result.append(node.val)
            stack.append(node.right)
            stack.append(node.left if node.left else None)
        else:
            result.append(None)

    return result

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    ''' It is iterative method to compare binary trees '''
    return preorderTraversal(p) == preorderTraversal(q)

p1 = TreeNode(1)
p2 = TreeNode(2)
p3 = TreeNode(3)
p1.left = p2
p2.right = p3

q1 = TreeNode(1)
q2 = TreeNode(2)
q3 = TreeNode(3)
q1.left = q2
q2.right = q3

p4 = TreeNode(1)
p5 = TreeNode(2)
p4.left = p5

q4 = TreeNode(1)
q5 = TreeNode(2)
q4.right = q5

p6 = TreeNode(1)
p7 = TreeNode(2)
p8 = TreeNode(1)
p6.left = p7
p6.right = p8

q6 = TreeNode(1)
q7 = TreeNode(1)
q8 = TreeNode(2)
q6.left = q7
q6.right = q8

print(isSameTree(p1, q1))
print(isSameTree(p4, q4))
print(isSameTree(p6, q6))