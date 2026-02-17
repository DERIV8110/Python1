# RECURSIVE FUNCTION TO ADD ELEMENTS OF A LIST
def mystery(l = [22,14,19,65,82,55],v = 1):
  if len(l) == 0:
    return (v)
  else:
    return (mystery(l[:-1],l[-1]+v))

print(mystery(l = [22,14,19,65,82,55],v = 1))