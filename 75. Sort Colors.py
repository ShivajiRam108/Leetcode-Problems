class Solution:
    # def sortColors(self, nums: list[int]) -> None:
    def sortColors(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        p0,cur,p2 = 0 , 0, len(nums)-1
        while cur <= p2:
            if nums(cur ) == 0:
                nums[p0], nums[cur] = nums[cur], nums[p0]
                p0+=1
                cur+=1
            elif nums(cur) == 2:
                nums[cur], nums[p2] = nums[p2], nums[cur]
                p2-=1
            else:
                cur+=1
        return nums


#  taking input form user.
def sortColors(nums):
    p0, cur, p2 = 0, 0, len(nums) - 1
    while cur <= p2:
        if nums[cur] == 0:
            nums[p0], nums[cur] = nums[cur], nums[p0]
            p0, cur = p0 + 1, cur + 1
        elif nums[cur] == 2:
            nums[cur], nums[p2] = nums[p2], nums[cur]
            p2 -= 1
        else:
            cur += 1
    return nums

# Taking input
nums = list(map(int, input("Enter space-separated numbers : ").split()))

# Sorting the colors
sorted_nums = sortColors(nums)

# Output the result
print("Sorted colors:", sorted_nums)
