
a = [1, 2, 3, 6, 9]
b = [2, 4, 6, 8]
c = []

for i in range(0,len(a)):
       if a[i] not in b and a[i] not in c:
                     c.append(a[i])
       else:
                     pass

print(c)