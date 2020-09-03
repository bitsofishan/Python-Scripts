"""Question - Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd."""

def is_product_odd(data):
    count=0
    lst=[]
    for i in data:
        for j in data:
            if (i*j)%2!=0:
                
                if (i,j) and (j,i) not in lst:
                    lst.append((i,j))
                    count+=1
        
    return lst,count
    

data=[5,6,7,8,9,12,3,4,66,2,34,12]
dist_array,num=is_product_odd(data)
print(dist_array,"\n\n Total unique pairs are:",num)
        
