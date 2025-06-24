l = eval(input("Enter list of strings: "))
largeIdx = 0
largeLen = 0

for i in range(len(l)):
    length = len(l[i])
    if length > largeLen:
        largeLen = length
        largeIdx = i

print("Longest String:", l[largeIdx])
#i didn't code this
    