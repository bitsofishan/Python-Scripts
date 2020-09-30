def palindrome_permute(a):
    a=a.lower()
    s=dict()
    count=0
    for i in a:
     if i!=" ":
      if i in s:
        s[i]+=1
      else:
        s[i]=1
    for i in s:
        if s[i]%2!=0:
            count+=1
    print(s)
    if count==1:
        return "pallindrome permutation Allowed"
    else:
        return "pallindrome permutation Not Allowed"

if __name__ == "__main__":
    print(palindrome_permute("tact   coa"))
