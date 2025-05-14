class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        
        res = []
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hashmap and i != hashmap[comp]:
                return [i, hashmap[comp]]
        
        return res