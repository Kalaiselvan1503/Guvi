#$%^*(*_})(
s1,s2=map(int,input().split())
for i in range(1):
    temp=s1|s2
    s1,s2=temp&s2,temp&s1
print(s1,s2)
