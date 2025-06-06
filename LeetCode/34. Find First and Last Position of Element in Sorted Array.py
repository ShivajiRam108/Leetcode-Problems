class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def fristNum(nums, target):
            left , right = 0 , len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    if mid == 0 or nums[mid - 1] != target:
                        return mid 
                    else:
                        right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return - 1
        def secondNum(nums, target):
            left , right = 0 , len(nums) - 1
            while left <= right:
                mid = left + (right - left ) // 2
                if nums[mid] == target:
                    if mid == len(nums ) - 1 or nums[mid + 1] != target:
                        return mid 
                    else:
                        right = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return - 1
        frist = fristNum(nums, target)
        last = secondNum(nums, target)
        return [frist, last]
x = Solution()
print(x.searchRange([5,7,7,8,8,10], target = 8))
print(x.searchRange([5,7,7,8,8,10], target = 6))

# (Or)
        # frist , last = -1, -1
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         if frist == -1:
        #             frist = i
        #         last = i
        # return [frist, last]