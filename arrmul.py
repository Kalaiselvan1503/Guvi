#DETFTUFUYGIUH:OI
k=int(input())
a=list(map(int,input().split()))
l1=[]
for i in range(k):
    c=1
    for j in range(i,k):
        c=c*a[j]
    l1.append(c)
for s in range(k):
    c=1
    for p in range(i+1):
        c=c*a[p]
    l1.append(c)
print(max(l1))
