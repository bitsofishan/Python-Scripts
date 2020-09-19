#Recursive Binary Search

def recursive_binary_search(data,target,low,high):
    data=sorted(data)
    
    if low>high:
        return False
    else:
        mid=(high+low)//2
        if data[mid]==target:
            return True
        elif target>data[mid]:
            return recursive_binary_search(data,target,mid+1,high)
        else:
            return recursive_binary_search(data,target,low,mid-1)
a=[1,2,6,3,8,44,23,67,23,1]
print(recursive_binary_search(a,2,0,len(a)-1))
