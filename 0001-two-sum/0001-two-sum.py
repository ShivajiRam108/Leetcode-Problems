class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         #  (Or)
        #  using hashmap
        hashMap = {}
        for i, j in enumerate(nums):
            res = target - j
            if res in hashMap:
                return [hashMap[res], i]
            hashMap[j] = i
        return [-1,-1]

        # using two pointers 
        # Note: in this case array must be sorted
        # left = 0
        # right = len(nums) - 1
        # while left  <= right:
        #     current_sum = nums[left] + nums[right]
        #     if current_sum == target:
        #         return [left, right]
        #     elif current_sum > target:
        #         right -= 1 
        #     else:
        #         left += 1
        # return [-1,-1]
       
        # (Or)
        #  using brute_force 
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return [-1,-1]