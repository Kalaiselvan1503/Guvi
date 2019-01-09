#1234
h=int(input())
n=list(map(int,input().split()))
s=sorted(h)
for i in range(0,len(s)):
    if i==0:
        print(s[i],end="")
    else:
        print("",s[i],end="")
