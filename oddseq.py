#oaehhaseg
k,s=map(int,input().split())
d=list(map(int,input().split()))
e=[]
for i in range(0,len(d)):
	if d[i]%2==1:
		e.append(d[i])
print(e[s-1])
