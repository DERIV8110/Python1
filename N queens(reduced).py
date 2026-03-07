import pprint
import json
    #  0  1  2  3
c = [ [0, 0, 0, 0], # 0
      [0, 0, 0, 0], # 1
      [0, 0, 0, 0], # 2
      [0, 0, 0, 0]] # 3
                   
# constructing different function for different diagonals:

d0 = [[0,3]]
d1 = [[0,2],[1,3]]
d2 = [[0,1],[1,2],[2,3]]
d3 = [[0,0],[1,1],[2,2],[3,3]]
d4 = [[1,0],[2,1],[3,2]]
d5 = [[2,0],[3,1]]
d6 = [[3,0]]

d00 = [[0,0]]
d11 = [[0,1],[1,0]]
d22 = [[0,2],[1,1],[2,0]]
d33 = [[0,3],[1,2],[2,1],[3,0]]
d44 = [[1,3],[2,2],[3,1]]
d55 = [[2,3],[3,2]]
d66 = [[3,3]]


pos = json.loads(input("enter list [i,j] for queen1: "))

if pos is None:
        print("Place atleast 1 queen at [i,j]")
        pass
else:
        for i in range(0,len(c)):
              for j in range(0,len(c)):
                     if i != pos[0] and j != pos[1]:
                            pass
                     elif i == pos[0] and j == pos[1]:
                            c[pos[0]][pos[1]] = 1
        for k in range(0,len(c)):
              for l in range(0,len(c)):
                     c[pos[0]][l] = 1
              #c[l][l] = 1      # incorrect function of diagonal FIX IT!!
                     c[l][pos[1]] = 1
        if pos in d0:
               for clone in range(0,1):
                      c[clone][clone+3] = 1
        
        if pos in d1:
                    for clone in range(0,2):
                           c[clone][clone+2] = 1
        
        if pos in d2:
                    for clone in range(0,3):
                           c[clone][clone+1] = 1
        
        if pos in d3:
                    for clone in range(0,4):
                           c[clone][clone] = 1
        
        if pos in d4:
                    for clone in range(0,3):
                           c[clone+1][clone] = 1
        
        if pos in d5:
                    for clone in range(0,2):
                           c[clone+2][clone] = 1
        
        if pos in d6:
                    for clone in range(0,1):
                           c[clone+3][clone] = 1
        
        
        if pos in d00:
                    for clone in range(0,1):
                           c[clone][clone] = 1
        
        if pos in d11:
                    for clone in range(0,2):
                           c[clone][abs(clone-1)] = 1
        
        if pos in d22:
                    for clone in range(0,3):
                           c[clone][abs(clone-2)] = 1
        
        if pos in d33:
                    for clone in range(0,4):
                           c[clone][abs(clone-3)] = 1
        
        if pos in d44:
                    for clone in range(0,3):
                           c[clone+1][abs(clone-3)] = 1
        
        if pos in d55:
                    for clone in range(0,2):
                           c[clone+2][abs(clone-3)] = 1
        
        if pos in d66:
               for clone in range(0,1):
                      c[clone+3][clone+3] = 1

pprint.pprint(c, width = 40)       
# checking for empty spaces (unattacked spaces) to put new queen:

pos2 = json.loads(input("enter list [i,j] for queen2: "))

if c[pos2[0]][pos2[1]] == 1:
        print("cannot place!")
        
else:
        for i in range(0,len(c)):
                     for j in range(0,len(c)):
                                   if i != pos2[0] and j != pos2[1]:
                                          pass
                                   elif i == pos2[0] and j == pos2[1]:
                                          c[pos2[0]][pos2[1]] = 1
        for k in range(0,len(c)):
                     for l in range(0,len(c)):
                                   c[pos2[0]][l] = 1
                                   #c[l][l] = 1      # incorrect function of diagonal FIX IT!!
                                   c[l][pos2[1]] = 1
                        #if c[pos2[0]][pos2[1]] == 1:
                        #        print("cannot place!")
                        #        
                        #elif c[pos2[0]][pos2[1]] == 0:
        
        if pos2 in d0:
            for clone in range(0,1):
                   c[clone][clone+3] = 1
        if pos2 in d1:
                    for clone in range(0,2):
                           c[clone][clone+2] = 1
        
        if pos2 in d2:
                    for clone in range(0,3):
                           c[clone][clone+1] = 1
        
        if pos2 in d3:
                    for clone in range(0,4):
                           c[clone][clone] = 1
        
        if pos2 in d4:
                    for clone in range(0,3):
                           c[clone+1][clone] = 1
        
        if pos2 in d5:
                    for clone in range(0,2):
                           c[clone+2][clone] = 1
        
        if pos2 in d6:
                    for clone in range(0,1):
                           c[clone+3][clone] = 1
        
        
        if pos2 in d00:
                    for clone in range(0,1):
                           c[clone][clone] = 1
        
        if pos2 in d11:
                    for clone in range(0,2):
                           c[clone][abs(clone-1)] = 1
        
        if pos2 in d22:
                    for clone in range(0,3):
                           c[clone][abs(clone-2)] = 1
        
        if pos2 in d33:
                    for clone in range(0,4):
                           c[clone][abs(clone-3)] = 1
        
        if pos2 in d44:
                    for clone in range(0,3):
                           c[clone+1][abs(clone-3)] = 1
        
        if pos2 in d55:
                    for clone in range(0,2):
                           c[clone+2][abs(clone-3)] = 1
                           print(clone+2,abs(clone-3))
        
        if pos2 in d66:
               for clone in range(0,1):
                      c[clone+3][clone+3] = 1

pprint.pprint(c, width = 40)
pos3 = json.loads(input("enter list [i,j] for queen3: "))
#for anakin in range(0,len(c)):
#        for vader in range(0,len(c)):
#                if c[pos3[0]][pos3[1]] == 1:
#                        print("cannot place!")
#                        break
#                elif c[pos3[0]][pos3[1]] == 0:
if c[pos3[0]][pos3[1]] == 1:
        print("cannot place!")
else:
       for i in c:
           for j in i:
                  if i != pos3[0] and j != pos3[1]:
                         c[pos2[0]][pos2[1]] = 1
                  elif i == pos3[0] and j == pos3[1]:
                         pass
       for k in range(0,len(c)):
           for l in range(0,len(c)):
                         c[pos3[0]][l] = 1
                         #c[l][l] = 1      # incorrect function of diagonal FIX IT!!
                         c[l][pos3[1]] = 1
       if pos3 in d0:
           for clone in range(0,1):
                  c[clone][clone+3] = 1
       if pos3 in d1:
                   for clone in range(0,2):
                          c[clone][clone+2] = 1

       if pos3 in d2:
                   for clone in range(0,3):
                          c[clone][clone+1] = 1

       if pos3 in d3:
                   for clone in range(0,4):
                          c[clone][clone] = 1

       if pos3 in d4:
                   for clone in range(0,3):
                          c[clone+1][clone] = 1

       if pos3 in d5:
                   for clone in range(0,2):
                          c[clone+2][clone] = 1

       if pos3 in d6:
                   for clone in range(0,1):
                          c[clone+3][clone] = 1


       if pos3 in d00:
                   for clone in range(0,1):
                          c[clone][clone] = 1

       if pos3 in d11:
                   for clone in range(0,2):
                          c[clone][abs(clone-1)] = 1

       if pos3 in d22:
                   for clone in range(0,3):
                          c[clone][abs(clone-2)] = 1

       if pos3 in d33:
                   for clone in range(0,4):
                          c[clone][abs(clone-3)] = 1

       if pos3 in d44:
                   for clone in range(0,3):
                          c[clone+1][abs(clone-3)] = 1

       if pos3 in d55:
                   for clone in range(0,2):
                          c[clone+2][abs(clone-3)] = 1

       if pos3 in d66:
              for clone in range(0,1):
                     c[clone+3][clone+3] = 1
pprint.pprint(c, width = 40)
pos4 = json.loads(input("enter list [i,j] for queen4: "))
#for anakin in range(0,len(c)):
#        for vader in range(0,len(c)):
#                if c[pos4[0]][pos4[1]] == 1:
#                        print("cannot place!")
#                        break
#                elif c[pos4[0]][pos4[1]] == 0:
if c[pos4[0]][pos4[1]] == 1:
        print("cannot place!")
else:
       for i in c:
           for j in i:
                  if i != pos4[0] and j != pos4[1]:
                         c[pos2[0]][pos2[1]] = 1
                  elif i == pos4[0] and j == pos4[1]:
                         pass
       for k in range(0,len(c)):
           for l in range(0,len(c)):
                         c[pos4[0]][l] = 1
                         #c[l][l] = 1      # incorrect function of diagonal FIX IT!!
                         c[l][pos4[1]] = 1
       if pos4 in d0:
           for clone in range(0,1):
                  c[clone][clone+3] = 1
       if pos4 in d1:
                   for clone in range(0,2):
                          c[clone][clone+2] = 1

       if pos4 in d2:
                   for clone in range(0,3):
                          c[clone][clone+1] = 1

       if pos4 in d3:
                   for clone in range(0,4):
                          c[clone][clone] = 1

       if pos4 in d4:
                   for clone in range(0,3):
                          c[clone+1][clone] = 1

       if pos4 in d5:
                   for clone in range(0,2):
                          c[clone+2][clone] = 1

       if pos4 in d6:
                   for clone in range(0,1):
                          c[clone+3][clone] = 1


       if pos4 in d00:
                   for clone in range(0,1):
                          c[clone][clone] = 1

       if pos4 in d11:
                   for clone in range(0,2):
                          c[clone][abs(clone-1)] = 1

       if pos4 in d22:
                   for clone in range(0,3):
                          c[clone][abs(clone-2)] = 1

       if pos4 in d33:
                   for clone in range(0,4):
                          c[clone][abs(clone-3)] = 1

       if pos4 in d44:
                   for clone in range(0,3):
                          c[clone+1][abs(clone-3)] = 1

       if pos4 in d55:
                   for clone in range(0,2):
                          c[clone+2][abs(clone-3)] = 1

       if pos4 in d66:
              for clone in range(0,1):
                     c[clone+3][clone+3] = 1
pprint.pprint(c, width = 40)
