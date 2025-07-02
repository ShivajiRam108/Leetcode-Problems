class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        res = []
        for i in nums:
            res.append(i)
        return res + res

x = Solution()
print(x.getConcatenation([1,2,3]))

#  (Or)

class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        res = []
        for i in nums:
            res.append(i)
        for i in nums:
            res.append(i)
        return res 
x = Solution()
print(x.getConcatenation([1,2]))
