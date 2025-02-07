class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        res = 0
        for i in range(len(nums)):
            if nums[i] !=0:
                nums[i], nums[res] = nums[res], nums[i]
                res+=1
        return nums
    


#  you want to take input write this code.
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        res = 0
        for i in range(len(nums)):
            if nums[i] !=0:
                nums[i], nums[res] = nums[res], nums[i]
                res+=1
nums = list(map(int, input("Enter numbers separated by space: ").split()))

# Calling the function
sol = Solution()
sol.moveZeroes(nums)

# Printing the result
print("Output:", nums)