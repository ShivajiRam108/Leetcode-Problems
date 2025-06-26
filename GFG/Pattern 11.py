class Solution:
    def printTriangle(self, N):
        for i in range(1, N+ 1):
            for j in range(i):
                if (i + j ) % 2 == 0:
                    print("0 ", end="")
                else:
                    print("1 ", end="")
            print()
x = Solution()
print(x.printTriangle(5))