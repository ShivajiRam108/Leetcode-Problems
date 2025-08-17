class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
        return k  # Return the new length of the array
        return nums[:k] # Return the modified array up to the new length
x = Solution()
print(x.removeDuplicates([1, 1, 1, 2, 2, 3]))  # Output: 5
print(x.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))  # Output: 7
print(x.removeDuplicates([1, 2, 3, 4, 5]))  # Output: 5
print(x.removeDuplicates([1, 1, 2]))  # Output: 3
print(x.removeDuplicates([1, 1, 1, 1, 2, 2, 3, 3]))  # Output: 6                         