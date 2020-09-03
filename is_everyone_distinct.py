"""Question - Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct)"""

def is_everyone_distinct(data):
    
    for i in range(len(data)):
        for j in range(len(data)):
            if (data[i]==data[j] and i!=j):
                return "Not Distinct"
            
    return "Distinct"
    
    

data=[5,6,7,8,9,12,3,90,66,2,34,13]
ans=is_everyone_distinct(data)
print(ans)
