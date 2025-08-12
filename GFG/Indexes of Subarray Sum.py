class Solution:
    def subarraySum(self, arr, target):
        left = 0 
        cur_sum = 0 
        for right in range(len(arr)):
            cur_sum += arr[right]
            while cur_sum > target and left <= right:
                cur_sum -= arr[left]
                left += 1
            if cur_sum == target:
                return [left+1, right+1]
        return [-1]
x = Solution()
print(x.subarraySum([1, 2, 3, 7, 5], 12))  # Output: [2, 4]
print(x.subarraySum([1, 2, 3, 4, 5], 15))  # Output: [1, 5] 
print(x.subarraySum([1, 2, 3, 4, 5], 10))  # Output: [2, 5]
print(x.subarraySum([1, 2, 3, 4, 5], 11))  # Output: [-1]