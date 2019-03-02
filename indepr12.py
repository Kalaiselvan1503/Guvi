#$U*U#UJjkjljeadf
m,n=map(int,(input()).split())
l=list(map(int,(input()).split()))
for i in range(0,n):
    x,y=map(int,(input()).split())
    s=0
    for j in range(x-1,y):
        s=s+l[j]
    print(s)
