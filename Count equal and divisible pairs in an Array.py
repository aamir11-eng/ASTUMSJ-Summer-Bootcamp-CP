class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        y=len(nums)
        count=0
        for i in range(y):
            for j in range(i+1,y):
                if nums[i]==nums[j] and (i*j)%k==0:
                    count+=1
        return count 
