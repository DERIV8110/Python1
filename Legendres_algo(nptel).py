# Make loop/s to check all combinations of a, in (4**a)*(8*b + 7) --> such that
#  we get all the numbers which we cannot represent as sum of three squares (trying to find the general case)
#Then show return(False) -->for those values after calculating the expression and if it = n.
#If return(True) -->then the number can be represented as sum of three squares.
m = int(input("enter m: "))
max_a = 10  
max_b = 20   
forbidden = []
def threesquares(m):
       for a in range(max_a + 1):
           for b in range(max_b + 1):
               forbidden.append((4 ** a) * (8 * b + 7))
       if m in forbidden:
            return False
       else:
            return True


       


