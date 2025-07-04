class Solution:
	def reverseDigits(self, n):
		res = ''
		for i in str(n):
			res = i + res 
		return int(res)
	
x = Solution()
print(x.reverseDigits(10))
print(x.reverseDigits(122))
print(x.reverseDigits(200))
