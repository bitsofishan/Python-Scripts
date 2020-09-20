#5*3 = 5+5+5 = 15
def product_iter(a,b):
    count=0
    for i in range(0,b):
        count=count+a
    return count

def product_recursive(a,b):
    if a==0 or b==0:
        return 0
    
    return a+product_recursive(a,b-1)

if __name__ == "__main__":
    print("Iterative:",product_iter(5, 3))
    print("Recursive:",product_recursive(500, 2000 ))
