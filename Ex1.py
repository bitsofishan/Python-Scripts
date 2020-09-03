"""Question - Write a short Python function, is_multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise"""

def is_multiple(n,m):
  if n>m:
    if n%m==0:
        return True
    else:
        return False
  else:
      return False
  
ans=is_multiple(100,11)
print(ans)
