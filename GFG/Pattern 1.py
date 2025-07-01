class Solution:
    def printSquare(self, N):
        for i in range(N):
            for j in range(N):
                print("* ", end="")
            print()
x = Solution()
print(x.printSquare(5))