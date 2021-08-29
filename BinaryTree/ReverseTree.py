# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS Solution
        """if not root:
            return root
        if not root.left and not root.right :
            return root
        
        queue = [root]
        
        while queue:
            new_queue = []
            for node in queue:
                if node:
                    node.left,node.right = node.right,node.left
                    new_queue.append(node.left)
                    new_queue.append(node.right)
            queue = new_queue
        return root"""
        
        #  Recursive Solution
        
        if not root :
            return root
        root.left,root.right = root.right,root.left
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        
        return root
