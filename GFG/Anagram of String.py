def remAnagram(s1,s2):
    a = list(s1)
    b = list(s2)
    i = 0 
    while i < len(a):
        res = a[i]
        if res in b:
            a.pop(i)
            b.remove(res)
        else:
            i += 1
    return len(a) + len(b)
print(remAnagram("bcadeh", "hea"))  # 3
print(remAnagram("cddgk", "gcd"))  # 2