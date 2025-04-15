str1=input("enter a string: ")
if len(str1)==12:
    if (str1[:3]+str1[4:7]+str1[8:12]).isdigit():
        print("entered number is legal.")
else:
    print("enter legal number with dashes at proper places!")