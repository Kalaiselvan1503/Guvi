#kjsd
n=int(input())
tot=1
while(n>0):
    dig=n%10
    tot=dig*tot
    n=n//10
print(tot)
