# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        res = 0
        
        def visit(node):
            if not node:
                return
            
            nonlocal res
            if L <= node.val <= R:
                res += node.val
            if node.val > L:
                visit(node.left)
            if node.val < R:
                visit(node.right)
            
        visit(root)
        return res

