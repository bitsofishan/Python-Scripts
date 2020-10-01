a="abbbaabaccc"
s=dict()
for i in a:
    if i in s:
        s[i]+=1
    else:
        s[i]=1
mx=max(s.values())
for k in s:
    
    if s[k]==mx:
       s[k]=0
       
for k in s:
    if s[k]==max(s.values()):
        print(k)
        break
