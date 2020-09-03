"""Question - Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators."""

def is_even(n):
  
    return "Even" if n%2==0 else "Odd"
    
 
  
ans=is_even(111)
print(ans)
