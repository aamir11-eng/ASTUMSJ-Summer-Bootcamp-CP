class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans1=[]
        for i in arr2:
            for j in range(len(arr1)):
                if i==arr1[j]:
                    ans1.append(arr1[j])
        ans2=[]
        for i in arr1:
            if i not in ans1:
                ans2.append(i) 
        ans2.sort()
        return ans1+ans2
