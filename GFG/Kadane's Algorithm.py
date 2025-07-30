class Solution:
    def maxSubarraySum(self, arr):
        max_sum = float('inf')
        cur_sum = 0 
        for i in arr:
            cur_sum += i 
            if(cur_sum > max_sum):
                max_sum = cur_sum
            if(cur_sum < 0):
                cur_sum = 0 
        return cur_sum
x = Solution()
print(x.maxSubarraySum([2, 3, -8, 7, -1, 2, 3])) # 11
print(x.maxSubarraySum([-2, -4])) # 0
print(x.maxSubarraySum([5, 4, 1, 7, 8]))  # 25

    
# Time Complexity: O(n)
# Space Complexity: O(1)

