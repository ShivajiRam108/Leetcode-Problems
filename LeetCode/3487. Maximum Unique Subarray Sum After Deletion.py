class Solution:
    def maxSum(self, nums: list[int]) -> int:
        res = []
        for i in nums:
            if i not in res and i >= 0:
                res.append(i)
        if not res:
            return max(nums)
        return sum(res)
    
x = Solution()
print(x.maxSum([1,2,3,4,5])) # 15
print(x.maxSum([1,1,0,1,1])) # 1
print(x.maxSum([1,2,-1,-2,1,0,-1])) # 3