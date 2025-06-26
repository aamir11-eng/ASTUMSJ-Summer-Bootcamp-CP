class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        a=sorted(nums)
        paired=[(a[i],a[i+1]) for i in range(0,len(a),2)]
        count=0
        for i in paired:
            count+=min(i)
        return count
