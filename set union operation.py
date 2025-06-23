en=int(input())
enNum=[int(i) for i in input().split()]
fr=int(input())
frNum=[int(i) for i in input().split()]
x=set(enNum)
y=set(frNum)
m=x.union(y)
print(len(m))
