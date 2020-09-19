#Find first uppercase letter in the given string

def is_upper_iterative(strng):
    for i in range(len(strng)):
        if strng[i].isupper():
            return True
    return False

def is_upper_recursive(strng,i=0):
    if strng[i].isupper():
        return True
    if i==len(strng)-1:
        return False
    return is_upper_recursive(strng,i+1)

a1="Ishan jain"
a2="ishan jain"
a3="ishan Jain"

print(is_upper_iterative(a1))
print(is_upper_iterative(a2))
print(is_upper_iterative(a3))

print(is_upper_recursive(a1,0))
print(is_upper_recursive(a2,0))
print(is_upper_recursive(a3,0))
