from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    ''' It is recursive method to compare binary trees '''
    if not p and not q:
        return True
    if not p or not q:
        return False
    return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

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