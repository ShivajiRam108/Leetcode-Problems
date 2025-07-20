class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1
        while left <= right:
            if nums[left] == target:
                return left 
            if nums[right] == target:
                return right 
            left += 1 
            right -= 1
        return -1 
x = Solution()
print(x.search([4,5,6,7,0,1,2],0))
print(x.search([4,5,6,7,0,1,2],3))