class Solution:
    @staticmethod
    def swap(nums: List[int], i: int, j: int) -> int:
        nums[i], nums[j] = nums[j], nums[i]
    
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            while nums[i] > 0 and nums[i] <= len(nums) and i + 1 != nums[i] and nums[i] != nums[nums[i] - 1]:
                Solution.swap(nums, i, nums[i] - 1)
            i += 1
        i = 0
        while i < len(nums) and i + 1 == nums[i]:
            i += 1
        return i + 1

