def fixed_point(a):
    for i in range(len(a)):
        if i==a[i]:
            return "Fixed Point is "+str(a[i])
    return "No Fixed Point"
print(fixed_point([-10,-5,0,4,7]))

# Linear Time complexity
#Trying binary search

def fixed_point_bin_search(a):
 low=0
 high=len(a)-1
 
 while low<=high:
  mid=(low+high)//2
  if mid==a[mid]:
   return True
  
  elif mid<a[mid]:
        low=mid+1
  else:
        high=mid-1
 return False
print(fixed_point_bin_search([1,2,2,3,7]))
