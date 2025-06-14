class Solution:
    def missingNum(self, arr):
        n = len(arr) + 1
        total_sum = n * (n+1) // 2
        arr_sum = sum(arr)
        return total_sum - arr_sum 
    
#another approach
class Solution:
    def missingNum(self, arr):
        max_num = max(arr)
        min_num = min(arr)
        for i in range(min_num, max_num+1):
            if i not in arr:
                return i 
            
# Time Complexity: O(n)
# Space Complexity: O(1)