class Solution:
    def isPalindrome(self, n):
        res = str(n)
        x = ''
        for i in res:
            x = i + x 
        return n == int(x)
x = Solution()
print(x.isPalindrome(555))  # True
print(x.isPalindrome(123))  # False
print(x.isPalindrome(1221))  # True