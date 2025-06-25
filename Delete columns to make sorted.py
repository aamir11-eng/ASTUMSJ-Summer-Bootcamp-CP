class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        l=0
        for i in range(len(strs[0])):
            for j in range(1,len(strs)):
                if strs[j][i]<strs[j-1][i]:
                    l+=1
                    break
        return l
