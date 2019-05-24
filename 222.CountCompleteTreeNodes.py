# Solution 1: Binary Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    @staticmethod
    def exist(root: TreeNode, height: int, num: int) -> bool:
        r = num - 2 ** height
        b = bin(r)[2:].zfill(height)
        current = root
        for digit in b:
            if digit == '0':
                if current.left:
                    current = current.left
                else:
                    return False
            else:
                if current.right:
                    current = current.right
                else:
                    return False
        return True
    
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        current = root
        height = 0
        while current.left:
            current = current.left
            height += 1
        
        left = 2 ** height
        right = 2 * left - 1
        while right - left > 1:
            mid = (left + right) // 2
            if self.exist(root, height, mid):
                left = mid
            else:
                right = mid
        if left == right:
            return left
        return left if not self.exist(root, height, right) else right


# Solution 2: Recursive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def height(self, root: TreeNode) -> int:
#         if not root:
#             return -1
#         else:
#             return 1 + self.height(root.left)
    
#     def countNodes(self, root: TreeNode) -> int:
#         if not root:
#             return 0

#         h = self.height(root)
#         rh = self.height(root.right)
#         if rh == h - 1:
#             return 2 ** h + self.countNodes(root.right)
#         else:
#             return 2 ** (h - 1) + self.countNodes(root.left)
