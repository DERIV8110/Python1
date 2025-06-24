n = int(input("Enter n: "))

if (n > 20):
    print("n should be less than or equal to 20")
else :
    a = 0
    b = 1
    c = a + b
    for i in range(3, n + 1):
        a = b
        b = c
        c = a + b

    print(n, "term of Fibonacci series =", c)

    #i didn't code this