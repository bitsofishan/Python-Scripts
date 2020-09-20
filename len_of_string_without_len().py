def len_iterative(strng):
    count=0
    for element in strng:
        count=count+1
        
    return count

def len_recursive(strng):
    if strng==" ":
      return 0
    
    return 1+ len_recursive(strng[1:])


if __name__== "__main__":
    a="Ish"
    print("Iterative:",len_iterative(a))
    print("Recursive:",len_recursive(a))     
