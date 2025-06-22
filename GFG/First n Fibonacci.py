class Solution:
    #Function to return list containing first n fibonacci numbers.
    def fibonacciNumbers(self,n):
        a, b = 0, 1
        res = []
        x = [0]
        for i in range(0, n-1):
            a, b = b, a+b 
            res.append(a)
        return (x + res)
x = Solution()
print(x.fibonacciNumbers(5))