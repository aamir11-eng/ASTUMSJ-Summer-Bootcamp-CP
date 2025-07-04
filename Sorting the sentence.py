class Solution:
    def sortSentence(self, s: str) -> str:
        l=s.split()
        n=sorted(l,key=lambda x:x[-1])
        ans=""
        for i in n:
            ans+=i[:-1]+" "
        return ans[:-1]
