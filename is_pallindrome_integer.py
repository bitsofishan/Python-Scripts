def is_pallindrome(s):
   if type(s)==int: 
    reverse=0
    org=s
    while s!=0:
        b=s%10
        print("b",b)
        reverse=reverse*10+b
        print("rev",reverse)
        s=s//10
        print("s",s)
    if reverse==org:
        return "Pallindrome"
    else:
        return "Not pallindrome"
   else:
     return "Input Not integer"
        
if __name__ == "__main__":
    print(is_pallindrome(12321))
