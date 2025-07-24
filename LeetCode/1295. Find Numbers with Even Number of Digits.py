class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        left = 0 
        right = len(nums) - 1
        count = 0 
        while left <= right:
            if len(str(nums[left])) % 2 == 0:
                count += 1
            if left != right and len(str(nums[right])) % 2 == 0:
                count += 1 
            left += 1
            right -= 1
        return count 
x = Solution()
print(x.findNumbers([12,345,2,6,7896]))

#  (Or)

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0 
        for i in nums:
            if len(str(i)) % 2 == 0:
                count += 1
        return count 
x = Solution()
print(x.findNumbers([12,345,2,6,7896]))
print(x.findNumbers([555,901,482,1771]))