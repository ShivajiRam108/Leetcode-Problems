class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        res = 0
        total = []
        for i in nums:
            res += i 
            total.append(res)
        return total 
x = Solution()
print(x.runningSum([1,2,3,4]))
print(x.runningSum([1,1,1,1,1]))
print(x.runningSum([3,1,2,10,1]))   

# (Or)

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
        return nums
x = Solution()
print(x.runningSum([1,2,3,4]))
print(x.runningSum([1,1,1,1,1]))
print(x.runningSum([3,1,2,10,1]))  