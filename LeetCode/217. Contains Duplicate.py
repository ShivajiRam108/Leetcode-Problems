class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return True if len(set(nums)) < len(nums) else False

        # (Or)
        
        nums.sort()
        res = len(nums)
        for i in range(1, res):
            if nums[i] == nums[i - 1]:
                return True
        return False