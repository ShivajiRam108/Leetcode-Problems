class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res = res ^ nums[i]
        return res

# # Create an instance of Solution
# x = Solution()

# # Call the method with the input list and print the result
# print(x.singleNumber([1,2,1]))
