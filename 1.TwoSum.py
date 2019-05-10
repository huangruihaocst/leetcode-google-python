class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, v in enumerate(nums):
            d[target - v] = i
        
        for i, v in enumerate(nums):
            if v in d and d[v] != i:
                return [i, d[v]]