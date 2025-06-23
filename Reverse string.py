class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n=len(s)-1
        m=0
        while m<n:
           s[m],s[n]=s[n],s[m]
           m+=1
           n-=1
