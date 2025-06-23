from collections import defaultdict
a,b=map(int,input().split())
dict={}
lisA=[]
lisB=[]
for i in range(a):
    grA=input()
    lisA.append(grA)
for i in range(b):
    grB=input()
    lisB.append(grB)
d=defaultdict()
for b in lisB:
    if b in lisA:
        d[b]=[i for i,j in enumerate (lisA,start=1) if j==b]
        print(' '.join(map(str,d[b])))
    else:
        print(-1)
