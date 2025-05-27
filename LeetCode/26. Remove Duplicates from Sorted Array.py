class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        j = 1 
        for i in range(1 , len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j

# Example usage:
x = Solution()
print(x.removeDuplicates([1, 1, 2]))  # Output: [1,,2,_]
