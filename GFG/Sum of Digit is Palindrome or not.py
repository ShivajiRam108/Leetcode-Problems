class Solution:
    def isDigitSumPalindrome(self, n):
        res = 0 
        for i in str(n):
            res = int(i) + res 
        x = ''
        for i in str(res):
            x = i + x 
        if str(res) == x:
            return True
        else:
            return False  
x = Solution()
print(x.isDigitSumPalindrome(56))
print(x.isDigitSumPalindrome(96))