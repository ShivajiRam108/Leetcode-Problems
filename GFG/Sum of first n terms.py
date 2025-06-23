class Solution:
    def sumOfSeries(self,n):
        res = 0
        for i in range(1, n+1):
            res += i ** 3
        return res 
x = Solution()
print(x.sumOfSeries(5))

# (Or)
class Solution:
    def sumofSeries(self, n):
        return (n * (n + 1) // 2) ** 2
x = Solution()
print(x.sumofSeries(5))