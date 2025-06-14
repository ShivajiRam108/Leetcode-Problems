class Solution:
    def maxSubArraySum(self, arr):
        # Kadane's Algorithm
        # this algorithm finds the maximum sum of a contiguous subarray in an array.
        
        max_sum = float("-inf")
        cur_sum = 0
        for i in arr:
            cur_sum += i
            if cur_sum > max_sum:
                max_sum = cur_sum 
            if cur_sum < 0:
                cur_sum = 0
        return max_sum 
    
# Time Complexity: O(n)
# Space Complexity: O(1)