# Solution 1: w/ memory/cache. Beat 98%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.cache = {0: list(), 1: [TreeNode(0)]}
    
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N in self.cache:
            return self.cache[N]
        res = list()
        for i in range(1, N - 1):
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(N - 1 - i)
            for nl in left:
                for nr in right:
                    root = TreeNode(0)
                    root.left = nl
                    root.right = nr
                    res.append(root)
        self.cache[N] = res
        return res


# Solution 2: w/o memory/cache. Beat 40%.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def allPossibleFBT(self, N: int) -> List[TreeNode]:
#         if N % 2 == 0:
#             return list()
#         if N == 1:
#             return [TreeNode(0)]
#         res = list()
#         for i in range(1, N - 1):
#             left = self.allPossibleFBT(i)
#             right = self.allPossibleFBT(N - 1 - i)
#             for nl in left:
#                 for nr in right:
#                     root = TreeNode(0)
#                     root.left = nl
#                     root.right = nr
#                     res.append(root)
#         return res
