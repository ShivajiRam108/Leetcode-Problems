class Solution:
    def thirdLargest(self,arr):
        arr.sort()
        l = len(arr)
        if l < 3:
            return -1 
        elif l == 3:
            return arr[0]
        else:
            return arr[-3]
x = Solution()
print(x.thirdLargest([2, 4, 1, 3, 5]))  # Output: 3
print(x.thirdLargest([1, 2]))  # Output: -1
print(x.thirdLargest([1, 2, 3]))  # Output: 1

