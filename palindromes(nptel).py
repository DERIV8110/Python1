n = int(input())
x = input()

def median(x):
    if n % 2 == 0:
        return n//2
    elif n % 2 != 0:
        return (n - 1)//2
    else:
        return None

palin = []
final_palin = []

if n % 2 == 0:
       median_left = int(median(x))
       median_right = int(median(x))+1

       while median_left > 0 and median_right < n - 1:
           if x[median_left] == x[median_right]:
               palin.append(x[median_left])
               palin.append(x[median_right])
               median_left -= 1
               median_right += 1
           else:
               median_left -= 1
               median_right += 1    
       for k in range(len(palin)-1, 0, -2):
               final_palin.append(palin[k])
       for l in range(0, len(palin), 2):
               final_palin.append(palin[l])
        
       result = "".join(final_palin)
       print(len(final_palin))
       print(result)         

elif n % 2 != 0:
       median_left = int(median(x))-1
       median_right = int(median(x))+1
       palin.append(x[median(x)])
       while median_left >= 0 and median_right <= n - 1:
           if x[median_left] == x[median_right]:
               palin.append(x[median_left])
               palin.append(x[median_right])
               median_left -= 1
               median_right += 1
           else:
               median_left -= 1
               median_right += 1

       middle = palin[0]
       pairs = palin[1:]

       left = []
       right = []

       for i in range(0, len(pairs), 2):
              left.append(pairs[i])
              right.append(pairs[i+1])

       left.reverse()

       final_palin = left + [middle] + right
       result = "".join(final_palin)
       print(len(final_palin))
       print(result)