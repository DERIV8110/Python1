#For what value of n would g(375,n) return 4?
def g(m,n):
    res = 0
    while m >= n:
        (res,m) = (res+1,m/n)
    return(res)