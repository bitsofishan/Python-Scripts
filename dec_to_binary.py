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

def dec_to_binary(num):
    s=Stack()
    while num>0:
        rem=num%2
        s.insert(rem)
        num=num//2
    bin_num=""
    while not s.is_empty():
        bin_num+=str(s.pop())
    return bin_num

print(dec_to_binary(242))
