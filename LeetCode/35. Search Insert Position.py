class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] <= target:
                return i 
        return len(nums)
    
        # (Or)
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right )//2
            if nums[mid] == target:
                return mid 
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left
    
    
        
        
           
            
               
            
           