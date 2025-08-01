class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(N):
                if i <= j:
                    print("* ", end="")
            print()
x = Solution()
print(x.printTriangle(5))