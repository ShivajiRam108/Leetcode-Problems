class Solution:
	def arraySum(self, arr):
		res = 0
		for i in arr:
			res += i 
		return res 
x = Solution()
print(x.arraySum([1,2,3,4]))