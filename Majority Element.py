class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict={}
        for i in nums:
            dict[i]=dict.get(i,0)+1
        for i in dict:
            if dict[i]>len(nums)/2:
                return i
