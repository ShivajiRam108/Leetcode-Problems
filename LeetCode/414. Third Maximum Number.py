class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums = set(nums) # Remove duplicates
        if len(nums) < 3:
            return max(nums)
        else:
            nums.remove(max(nums)) # Remove the largest element
            nums.remove(max(nums)) # Remove the two largest elements
            return max(nums)
x = Solution()
print(x.thirdMax([1, 2]))  # Output: 2  
print(x.thirdMax([2, 2, 3, 1]))  # Output: 1
print(x.thirdMax([1, 2, 3]))  # Output: 1   
print(x.thirdMax([5, 4, 3, 2, 1]))  # Output: 3
print(x.thirdMax([1, 2, 2, 3, 4]))  # Output: 2