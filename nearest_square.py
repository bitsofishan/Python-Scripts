def near_root(a):
 sq=0
 i=1
 while sq<a:
    sq=i*i
    
    i+=1
 return i-2
print(near_root(24))   

# Using Binary Search
def near_root_binary(a):
    low=0
    high=a
    while low<=high:
        mid=(low+high)//2
        mid_sq=mid*mid
        if a>mid_sq:
            low=mid+1
        elif a<mid_sq:
            high=mid-1
    return low-1
print(near_root_binary(300))     
