#hoshdaf
x=[int(i) for i in input().split()]
y=[int(j) for j in input().split()]
c=x[0]*60+x[1]
d=y[0]*60+y[1]
k=abs(c-d)
print(str(k//60)+" "+str(k%60))
