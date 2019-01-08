#43536tdsf
n=int(input())
k=list(map(int,input().split()))
s=sorted(k)
for i in range(0,len(s)):
    if i==0:
        print(s[i],end="")
    else:
        print("",s[i],end="")
