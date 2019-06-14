# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        dd = defaultdict(list)
        
        def dfs(node: TreeNode) -> int:
            nonlocal dd
            if not node:
                return 0
            if node.left == node.right == None:
                dd[0].append(node.val)
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            dd[1 + max(left, right)].append(node.val)
            return 1 + max(left, right)
        
        dfs(root)
        res = list()
        for k in sorted(dd.keys()):
            res.append(dd[k])
        return res

