class Solution:
    def printArray(self, arr):
        for i in arr:
            print(i, end=" ")
x = Solution()
print(x.printArray([1, 2, 3, 4, 5]))  # Output: 1 2 3 4 


# (Or)
class Solution:
    def printArray(self, arr):
        res = ''
        for i in arr:
            res += str(i) + ' '
        return res.strip()
x = Solution()
print(x.printArray([1, 2, 3, 4, 5]))  # Output: 1 2 3 4 5