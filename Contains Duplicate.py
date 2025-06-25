class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict=set(nums)
        if len(dict)==len(nums):
            return False
        else:
            return True
