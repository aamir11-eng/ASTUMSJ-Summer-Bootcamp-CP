class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        l={}
        m=sorted(score,reverse=True)
        for i,j in enumerate(m):
            if i==0:
               l[j]="Gold Medal"
            elif i==1:
                l[j]="Silver Medal"
            elif i==2:
                l[j]="Bronze Medal"
            else:
                l[j]=str(i+1)
        ans=[]
        for i in score:
            ans.append(l[i])
        return ans
