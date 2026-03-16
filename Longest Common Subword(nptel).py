#def LCW(u,v):    # u[0....m-1], v[0...n-1]
#
#       for r in range(len(u)+1):
#              LCW[r][len(v)+1] = 0  # r for row
#       for c in range(len(v)+1):
#              LCW[len(u)+1][c] = 0  # c for column
#       
#       maxLCW = 0
#       for c in range(len(v)+1,-1,-1):
#              for r in range(len(u)+1,-1,-1):
#                     if u[r] == v[c]:
#                            LCW[r][c] = 1+LCW[r+1][c+1]
#                     else:
#                            LCW[r][c] = 0
#                     if LCW[r][c] > maxLCW:
#                            maxLCW = LCW[r][c]
#       return(maxLCW)
def LCW(u, v):   # u[0....m-1], v[0...n-1]
    m = len(u)
    n = len(v)
    
    # Create (m+1) x (n+1) table initialized to 0
    table = [[0] * (n + 1) for _ in range(m + 1)]
    
    maxLCW = 0
    for c in range(n - 1, -1, -1):
        for r in range(m - 1, -1, -1):
            if u[r] == v[c]:
                table[r][c] = 1 + table[r+1][c+1]
            else:
                table[r][c] = 0
            if table[r][c] > maxLCW:
                maxLCW = table[r][c]
    return maxLCW

print(LCW("titan", "tertiary"))  # Output: 3  →  "ect"
