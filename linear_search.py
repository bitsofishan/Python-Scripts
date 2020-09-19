#Linear Search
def linear_search(data,target):
    for i in range(len(data)):
        if target==data[i]:
            return True
    return False
a=[1,2,6,3,8,44,23,67,23,1]
print(linear_search(a,5))
