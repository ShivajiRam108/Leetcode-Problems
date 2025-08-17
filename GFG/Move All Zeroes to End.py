class Solution:
	def pushZerosToEnd(self, arr):
		left = 0 
		for right in range(len(arr)):
			if arr[right] != 0:
				arr[left] , arr[right] = arr[right], arr[left]
				left += 1 
		return arr
x = Solution()
print(x.pushZerosToEnd([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]   
print(x.pushZerosToEnd([0, 0, 1, 2, 3]))  # Output: [1, 2, 3, 0, 0]
print(x.pushZerosToEnd([1, 2, 3, 4, 5]))  # Output: [1, 2, 3, 4, 5]
print(x.pushZerosToEnd([0, 0, 0, 0, 0]))  # Output: [0, 0, 0, 0, 0]
print(x.pushZerosToEnd([1, 0, 2, 0, 3]))  # Output: [1, 2, 3, 0, 0]