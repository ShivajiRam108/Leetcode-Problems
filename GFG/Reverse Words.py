class Solution:
    def reverseWords(self, s):
        res = s.split()
        res = reversed(res)
        return ' '.join(res)
x = Solution()
print(x.reverseWords(" i like this program very much "))

#  (Or)

class Solution:
    def reverseWords(self, s):
        res = s.split()
        x = ''
        for i in res:
            x = i + " " + x 
        return x.strip()
x = Solution()
print(x.reverseWords(" i like this program very much "))