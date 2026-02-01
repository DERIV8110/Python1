x = int(input("Enter m: "))
y = int(input("Enter n: "))
all_factors = []
i = 1
while i<=x and i<=y:
       if x%i==0 and y%i==0:
              all_factors.append(i)
              i+=1
       else:
              i+=1

all_factors.sort()
print(all_factors)
print(all_factors[len(all_factors)-1])