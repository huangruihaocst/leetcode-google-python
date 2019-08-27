# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        visit = [root]
        max_level = None
        max_sum = float('-inf')
        curr_level = 1
        while visit:
            new = list()
            curr = 0
            for v in visit:
                curr += v.val
                if v.left:
                    new.append(v.left)
                if v.right:
                    new.append(v.right)
            if curr > max_sum:
                max_sum = curr
                max_level = curr_level
            visit = new
            curr_level += 1
        return max_level
                
