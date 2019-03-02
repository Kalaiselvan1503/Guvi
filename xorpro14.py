#skdlakl;i9rw3ke
m,n=map(int,(input()).split())
a=list(map(int,(input()).split()))
k=[]
for i in range(0,n):
    x,y=map(int,(input()).split())
    s=0
    for j in range(x-1,y):
            s=s^a[j]
    print(s)
