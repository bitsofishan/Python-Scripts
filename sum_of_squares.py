"""Question - Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n."""

def sum_of_squares(data):   
    return sum((i*i) for i in range(1,data))

squares_sum=sum_of_squares(2)
print(squares_sum)
