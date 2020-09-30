def excel_num_encode(s):
    num=0
    count=len(s)-1
    for i in s: 
        num+=26**count * (ord(i)-ord("A")+1)
        count-=1
    return num
    
print(excel_num_encode("ZZ")) 
