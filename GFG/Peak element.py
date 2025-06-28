class Solution:   
    def peakElement(self,arr):
        left = 0 
        right = len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] > arr[mid + 1]:
                right = mid 
            else:
                left = mid + 1
        return left 
x = Solution()
print(x.peakElement([1, 2, 4, 5, 7, 8, 3]))




