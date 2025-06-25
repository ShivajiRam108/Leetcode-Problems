class Solution:
    def factorial (self, n):
        res = 1
        for i in range(1, n+1):
            res *= i 
        return res 
x = Solution()
print(x.factorial(5))