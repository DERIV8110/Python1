# What does f(27182818) return, for the following function definition?


def f(x):
  d=0
  while x > 1:
    (x,d) = (x/2,d+1)
  return(d)