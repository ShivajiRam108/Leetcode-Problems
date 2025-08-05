class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0 
        for i in nums:
            res ^= i 
        return res 
x = Solution()
print(x.singleNumber([2,2,1]))  # 1 
print(x.singleNumber([4,1,2,1,2]))  # 4 


# (Or)

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0 
        for i in nums:
            if nums.count(i) == 1:
                res += i 
        return res 
x = Solution()
print(x.singleNumber([2,2,1]))  # 1 
print(x.singleNumber([4,1,2,1,2]))  # 4 