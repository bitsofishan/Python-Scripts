def task_assignment(a,b):
 
 if len(a)%b==0:
    c=[]
    a=sorted(a)
    for i in range(len(a)//2):
        c.append((a[i],a[~i]))
    return c
 else:
        return "Cant Assign tasks"
print(task_assignment([6,3,2,7,5,5,8,4],4))
