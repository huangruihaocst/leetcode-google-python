# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    @staticmethod
    def get_length(head: ListNode) -> int:
        node = head
        cnt = 0
        while node is not None:
            node = node.next
            cnt += 1
        return cnt
    
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        n = Solution.get_length(head)
        stack = list()
        res = [0] * n
        node = head
        index = 0
        for i in range(n):
            while stack and node.val > stack[-1][1]:
                res[stack.pop()[0]] = node.val
            stack.append((index, node.val))
            index += 1
            node = node.next
        return res


# Solution 2: No need of find length first.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
    
#     def nextLargerNodes(self, head: ListNode) -> List[int]:
#         stack = list()
#         res = list()
#         node = head
#         while node:
#             while stack and node.val > stack[-1][1]:
#                 res[stack.pop()[0]] = node.val
#             stack.append((len(res), node.val))
#             res.append(0)
#             node = node.next
#         return res
