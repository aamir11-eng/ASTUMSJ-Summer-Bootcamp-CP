class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1=sorted(nums1)
        nums2=sorted(nums2)
        m=[]
        x=0
        y=0
        while x<len(nums1) and y<len(nums2):
            if nums1[x]<nums2[y]:
                x+=1
            elif nums1[x]>nums2[y]:
                y+=1
            else:
                m.append(nums1[x])
                x+=1
                y+=1
        return m
