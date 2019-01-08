#even
n,c=input().split()
n=int(n)
c=int(c)
for i in range(n+1,c):
    if(i%2==0):
        print(i)
