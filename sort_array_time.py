#1234
f=int(input())
d=list(map(int,input().split()))
s=sorted(d)
for i in range(0,len(s)):
    if i==0:
        print(s[i],end="")
    else:
        print("",s[i],end="")
