class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1
        while left <= right:
            if nums[left] == target:
                return left
            if nums[right ]  == target:
                return right
            left += 1
            right -= 1 
        return -1