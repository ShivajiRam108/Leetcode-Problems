class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right ) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] != nums[mid + 1]:
                right = mid 
            else:
                left = mid + 2
        return nums[left]
x = Solution()
print(x.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))  # 2
print(x.singleNonDuplicate([3,3,7,7,10,11,11]))  # 10


# (Or)

class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        res = 0 
        for i in nums:
            if nums.count(i) == 1:
                res += i 
        return res 
x = Solution()
print(x.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))  # 2
print(x.singleNonDuplicate([3,3,7,7,10,11,11]))  # 10