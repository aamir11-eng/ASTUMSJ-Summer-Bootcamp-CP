class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row=["qwertyuiop","asdfghjkl","zxcvbnm"]
        l=[]
        for i in words:
            for j in row:
                c=i.lower()
                result=all(char in j for char in c)
                if result:
                    l.append(i)
        return(l)
