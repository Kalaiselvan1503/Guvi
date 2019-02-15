#jgdk
a,b,c=map(int,input().split())
d=a+b
e=a+c
f=b+c
if(d>c and e>b and f>a):
	print("yes")
else:
	print("no")
