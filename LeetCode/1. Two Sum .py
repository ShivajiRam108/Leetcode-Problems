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

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
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
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [-1,-1]
x= Solution()
print(x.twoSum([2,7,11,15], 9))  # Output: [0, 1]
print(x.twoSum([3,2,4], 6))       # Output: [1, 2]
print(x.twoSum([3,3], 6))          # Output: [0, 1]

        