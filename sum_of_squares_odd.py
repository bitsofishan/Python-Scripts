"""Question - Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n"""

def sum_of_squares_odd(data):
    
    return sum((i*i) for i in range(1,data) if i%2!=0)
        
    


squares_sum=sum_of_squares_odd(5)
print(squares_sum)
