#1323
s = input()
count = 0
for c in s :
  if c.isspace() != True:
    count = count + 1
print(count)
