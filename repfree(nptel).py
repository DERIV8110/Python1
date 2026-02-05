def repfree(s):
       repeat_count = 0
       for i in range(0,len(s),1):
              if s.count(s[i])>1:
                     repeat_count+=1
              else:
                     pass
       if repeat_count>0:
              return False
       else:
              return True
