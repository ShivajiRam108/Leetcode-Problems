class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        res = []
        for i in range(0, len(nums), 2):
            res += nums[i] * [nums[i+1]]
        return res 
x = Solution()
print(x.decompressRLElist([1,2,3,4]))

# (Or)
class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        res = []
        for i in range(0, len(nums), 2):
            frevm = nums[i]
            val = nums[i+1]
            res.extend([val] * frevm)
        return res 
x = Solution()
print(x.decompressRLElist([1,1,2,3]))
