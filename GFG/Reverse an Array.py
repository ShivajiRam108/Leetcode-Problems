#  using two pointers to reverse an array
class Solution:
    def reverseArray(self, arr):
        left = 0 
        right = len(arr) - 1
        while left <= right:
            arr[left] , arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr 
x = Solution()
print(x.reverseArray([1, 2, 3, 4, 5]))

#  (Or)

#  using slicing to reverse an array
class Solution:
    def reverseArray(self, arr):
        return arr[::-1]
x = Solution()
print(x.reverseArray([1, 2, 3, 4, 5]))

# (Or)

#  using built-in function to reverse an array
class Solution:
    def reverseArray(self, arr):
        return list(reversed(arr))  
    
x = Solution()
print(x.reverseArray([1, 2, 3, 4, 5]))

# (Or)
#  using bubble sort to reverse an array
class Solution:
    def reverseArray(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr)- i-1):
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
x = Solution()
print(x.reverseArray([1, 2, 3, 4, 5]))