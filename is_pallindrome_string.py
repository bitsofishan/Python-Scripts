 def is_pallindrome(s):
        s=s.lower()
        if s==s[::-1]:
            return "Pallindrome"
        else:
            return "Not pallindrome"
print(is_pallindrome("abaa"))
