def consonants_iter_count(strng):
    count=0
    strng=strng.lower()
    for i in strng:
        if i not in ("a","e","i","o","u") and i.isalpha():
            count=count+1
    return count

def consonants_recursive_count(strng):
     if strng=="":
         return 0
     if strng[0].lower() not in ("a","e","i","o","u") and strng[0].lower().isalpha():
         return 1+consonants_recursive_count(strng[1:])
     else:
         return consonants_recursive_count(strng[1:])

if __name__ == "__main__":
  a="Ishan Jain"
  print("Iterative:",consonants_iter_count(a))
  print("Recursive:",consonants_recursive_count(a)) 
