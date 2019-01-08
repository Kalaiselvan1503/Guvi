#1234
l,u=input().split()
l=int(l)
u=int(u)
m=[]
for num in range(l, u):
   order = len(str(num))
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
   if num == sum:
       m.append(num)
       
for k in range(0,len(m)-1):
  print(m[k],end=" ")
print(m[len(m)-1])
