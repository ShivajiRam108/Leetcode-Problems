class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #  best case
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        
        res = []
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hashmap and i != hashmap[comp]:
                return [i, hashmap[comp]]
        
        return res
    
    # another best case is two pointers but it is given the wrong indexes
        left = 0 
        right = len(nums) - 1
        while left <= right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                return [left, right]
            elif current_sum > target:
                right -= 1
            else:
                left += 1
        return [-1, -1]
    #  brute_force approch 

        