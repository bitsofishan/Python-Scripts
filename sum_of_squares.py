"""Question - Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n."""

def sum_of_squares(data):
    total=0
    for i in range(1,data):
        total=total+(i*i)
        
    return total


squares_sum=sum_of_squares(100)
print(squares_sum)
