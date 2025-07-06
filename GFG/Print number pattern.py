class Solution:
    def  printPat(self, n):
        res = []
        for i in range(n,0,-1):
            for j in range(n,0,-1):
                res.extend([j]* i)
            res.append(-1)
        return res 
x = Solution()
print(x.printPat(3))
print(x.printPat(2))
print(x.printPat(1))