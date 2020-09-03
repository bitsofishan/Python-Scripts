"""Question - Write a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before"""

def reverse_it(data):
    
    for i in range(0,int(len(data)/2)):
        
        data[i],data[-(i+1)]=data[-(i+1)],data[i]
    return data
    

data=[5,6,7,8,9,12,3,4,66,2,34,12]
reverse_array=reverse_it(data)
print(reverse_array)
