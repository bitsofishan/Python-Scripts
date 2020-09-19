#Iterative Binary Search
def iterative_bin_search(data,target):
    data=sorted(data)
    low=0
    high=len(data)-1
    
    while low<high:
     mid=(high+low)//2
     if data[mid]==target:
        return True
     elif target>data[mid]:
         low=mid+1
     else:
         high=mid-1
    return False
a=[1,2,6,3,8,44,23,67,23,1]
print(iterative_bin_search(a,2))
