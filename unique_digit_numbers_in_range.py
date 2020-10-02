def find_prime_range(n,m):
    count=0
    for i in range(n,m+1,1):
        num=i
        flag=1
        dic={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,0:0}
        while num>0:
            rem=int(num%10)
          
            dic[rem]+=1
            num=num//10
           
        for s in dic:
            
            if dic[s]>1:
                flag=0
        if flag==1:
            count+=1
    return count

print(find_prime_range(90,100))
