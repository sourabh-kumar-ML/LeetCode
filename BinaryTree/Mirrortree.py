# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root :
            return True
        
        if not root.right or not root.left:
            if not root.right and not root.left:
                return True
            return False
        return self.compareTree(root.right,root.left)
    
    def compareTree(self,x,y):
        if not x and not y:
            return True
        if not x or not y:
            return False
        if x.val != y.val:
            return False
        return (self.compareTree(x.left,y.right) and self.compareTree(x.right,y.left))
