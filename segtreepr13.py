#jksfhksrgl
m,n=map(int,(input()).split())
l=list(map(int,(input()).split()))
k=[]
for i in range(0,n):
    x,y=map(int,(input()).split())
    s=0
    m=l[x-1]
    for j in range(x-1,y):
        if(l[j]<m):
            m=l[j]
    print(m)
