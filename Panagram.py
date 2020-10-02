def is_panagram(a):
    a=a.lower()
    alpha="abcdefghijklmnopqrstuvwxys "
    for i in alpha:
        if not i in a:
            return "Not Panagram"
    return "Panagram"
print(is_panagram("The quick brown fox jumps over the lazy do"))
