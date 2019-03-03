#ipoijisjgj;gr
p=int(input())
m=list(map(int,(input()).split()))
s=0
for i in range(0,p-2):
    for j in range(i+1,p-1):
        for k in range(j+1,p):
            if(i<j<k):
                if(m[i]+m[j]==m[k]):
                    s=s+1
print(s)
