#drfdf
n,a,d=map(int,input().split())
c=0
i=a
l=[]
while i>=a:
    l.append(i)
    c=c+1
    i=i+d
    if c==n:
        break
print(sum(l))
