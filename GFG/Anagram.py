class Solution:
    def areAnagrams(self, s1, s2):
       return (sorted(s1) == sorted(s2))
    

x  = Solution()
print(x.areAnagrams("geeks", "kseeg"))

#  (Or)

class Solution:
    def areAnagrams(self, s1, s2):
        a = {}
        b = {}
        for i in s1:
            a[i] = a.get(i,0) + 1
        for j in s2:
            b[j] = b.get(j, 0) +1
        return a == b
x  = Solution()
print(x.areAnagrams("geeks", "kseeg"))