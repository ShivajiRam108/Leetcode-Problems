class Solution:
    def printTriangle(self, N):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if i >= j :
                    print(j, end = " ")
            print()
        
x = Solution()
x.printTriangle(5)
# Output
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
