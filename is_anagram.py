def is_anagram(a,b):
        a=a.lower()
        b=b.lower()
        a1=[]
        b1=[]
        for i in range(len(a)):
            if a[i]!="":
                continue
            elif b[i]!="":
                continue
            else:
                a1.append(a[i])
                b1.append(b[i])
        if sorted(a1)==sorted(b1):
        
            return "Anagram"
        else:
            return "Not Anagram"
print(is_anagram("fairytales","railsafety"))

# This approach although is easy, is not time efficient


def is_anagram(a,b):
    a=a.replace(" ","").lower()
    b=b.replace(" ","").lower()
    dic=dict()
    if len(a)!=len(b):
        return "Not Anagram"
    else:
        for i in a:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in b:
            if i in dic:
                dic[i]-=1
            else:
                dic[i]=1
        for i in dic:
            if dic[i]!=0:
                return "Not Anagram"
        return "Anagram"
    
print(is_anagram("fairy tales"," rail             safety "))
