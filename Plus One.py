class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l=''.join(str(i) for i in digits) 
        n=int(l)+1
        s=str(n)
        lis=[]
        for i in s:
           i=int(i)
           lis.append(i)
        return lis
