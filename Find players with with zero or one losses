class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans=[[],[]]
        dict={}
        for i,j in matches:
            win=i
            los=j
            dict[win]=dict.get(win,0)
            dict[los]=dict.get(los,0)+1
        for i in sorted(dict.keys()):
            if dict[i]==0:
                ans[0].append(i)
            elif dict[i]==1:
                ans[1].append(i)
        return ans
