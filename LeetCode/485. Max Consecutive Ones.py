# class Solution:
#     def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
#          # (or)
#         l, zeros = 0, 0
#         for r, n in enumerate(nums):
#             zeros += n == 0
#             if zeros > 0:
#                 zeros -= nums[l] == 0
#                 l += 1
#         return r - l +1

        # (Or)
class Solution:
    def findMaxConsecutiveOnes(self, n: list[int]) -> int:
        count = 0 
        max_count = 0 
        for i in n:
            if i == 1:
                count += 1 
                max_count = max(max_count, count)
            else:
                count = 0
        return max(max_count , count)
x = Solution()
print(x.findMaxConsecutiveOnes([1,1,0,1,1,1]))  # Output: 3
print(x.findMaxConsecutiveOnes([1,0,1,1,0,1,1,0,1]))  # Output: 2
print(x.findMaxConsecutiveOnes([0,0,0,0,0]))  # Output: 0


