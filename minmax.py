"""Question - Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution."""

def minmax(data):
  
    largest=data[0]
    smallest=data[1]
    
    for i in range(len(data)):
        if data[i]>largest:
            largest=data[i]
        elif data[i]<smallest:
            smallest=data[i]
        
    return largest,smallest
 
data=[34,67,1,54,23,12,4,76,4]
large,small=minmax(data)
print(large,small)
