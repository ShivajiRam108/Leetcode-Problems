class Solution:
	def countOddEven(self, arr):
		even = 0
		odd = 0
		for i in arr:
			if i % 2 == 0:
				even += 1
			else:
				odd += 1
		return odd , even 
x = Solution()
print(x.countOddEven([1, 2, 3, 4, 5]))