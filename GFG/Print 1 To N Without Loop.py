class Solution:
    def printNos(self, n):
        if n > 1:
            self.printNos(n-1)
        print(n, end=" ")
x = Solution()
print(x.printNos(10))
