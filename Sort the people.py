class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        my_dict=list(zip(names,heights))
        d=sorted(my_dict,key=lambda item:item[1], reverse=True)
        ans=[]
        for i,j in d:
            ans.append(i)
        return ans
