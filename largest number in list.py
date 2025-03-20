a = [10, 24, 76, 23, 12]

# Assuming first element is largest.
largest = a[0]

# Iterate through list and find largest
for i in a:
    if i > largest:
      
          # If current element is greater than largest
        # update it
        largest = i
second_largest=a[0]
for i in a:
    if i<largest and i>second_largest:
        #agar number largest se chota hai aur baaki sabme me bada hai
        #toh wo second largest hai
        second_largest=i
        print(second_largest)
        #and it fucking works too!!
