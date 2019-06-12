# Solution 1: Beat 8%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        d = dict()
        
        def cal_max(node):
            if not node:
                d[node] = float('-inf')
                return
            cal_max(node.left)
            cal_max(node.right)
            m = max(d[node.left], d[node.right])
            if m != float('-inf'):
                d[node] = node.val + m
            else:
                d[node] = node.val
        
        cal_max(root)
        
        current = 0
        def dfs(node):
            nonlocal current
            if not node:
                return
            if current + node.val + d[node.left] < limit:
                node.left = None
            else:
                current += node.val
                dfs(node.left)
                current -= node.val
            if current + node.val + d[node.right] < limit:
                node.right = None
            else:
                current += node.val
                dfs(node.right)
                current -= node.val
        if d[root] < limit:
            return None
        dfs(root)
        return root
            

# Solution 2: Beat 75%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
#         if not root.left and not root.right:
#             return root if root.val >= limit else None
#         if root.left:
#             root.left = self.sufficientSubset(root.left, limit - root.val)
#         if root.right:
#             root.right = self.sufficientSubset(root.right, limit - root.val)
#         return root if root.left or root.right else None
