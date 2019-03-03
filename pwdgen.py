#hsjghs
a,b=input().split()
d=min(len(a),len(b))
s=""
for i in range(d):
    s+=a[i]
    s+=b[i]
k=b if len(b)>len(a) else a
c=1
for i in range(d,len(k)):
    if k==b:
        s+=str(c)
        s+=k[i]
    if k==a:
        s+=k[i]
        s+=str(c)
    c+=1
print(s)
