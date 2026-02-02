#Consider the following function mys:
def mys(m):
    if m == 1:
        return(1)
    else:
        return(m*mys(m-1))

#Which of the following is correct?
# The function always terminates with mys(n) = factorial of n
# The function always terminates with mys(n) = 1+2+...+n
# The function terminates for non-negative n with mys(n) = factorial of n
# The function terminates for positive n with mys(n) = factorial of n