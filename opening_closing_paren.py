class Stack():
    def __init__(self):
        self.stack=[]
    def insert(self,value):
        self.stack.append(value)
    def pop(self):
       return self.stack.pop()
    def total(self):
       return sum(self.stack)
    def get_stack(self):
        return self.stack
    def is_empty(self):
        return self.stack==[]
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
    def view(self):
        return self.stack[::-1]

def is_match(p1,p2):
    if p1=="(" and p2==")":
     return True
    elif p1=="{" and p2=="}":
     return True 
    elif p1=="[" and p2=="]":
     return True
    else:
        return False

def is_paren_balanced(strng):
    s=Stack()
    is_balanced=True
    index=0
    while index<len(strng) and is_balanced:
        paren=strng[index]
        if paren in"({[":
            s.insert(paren)
        else:
            if s.is_empty():
                is_balanced=False
            else:
                top=s.pop()
                if not is_match(top,paren):
                    is_balanced=False
        index+=1 
    if s.is_empty() and is_balanced:
        return True
    else:
        return False
                 
print(is_paren_balanced("(]"))      
