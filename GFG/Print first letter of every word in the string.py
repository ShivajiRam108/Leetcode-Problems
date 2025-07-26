class Solution:
	def firstAlphabet(self, S):
		res = S.split()
		x = ''
		for i in res:
			x += i[0]
		return x 
x  = Solution()
print(x.firstAlphabet("geeks for geeks"))  # gfg
print(x.firstAlphabet("bad is good"))  # big