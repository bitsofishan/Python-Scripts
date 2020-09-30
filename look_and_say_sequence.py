def generate_seq(n):
    s=[]
    i=0
    while i < len(n):
        count=1
        while i+1<len(n) and n[i]==n[i+1]:
            i+=1
            count=count+1
            
        s.append(str(count) + n[i])
        i+=1
    return "".join(s)

n=4
s="1"
print(s)
for i in range(n-1):
    s=generate_seq(s)
    print(s)
