class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        res = []
        for i in nums:
            res.append(i ** 2)
        res.sort()
        return res

    # (Or)

    #  using two pointer:-
        left = 0
        right = len(nums) - 1
        res = []
        while left <= right :
            if abs(nums[left]) > abs(nums[right]):
                res.append(nums[left] ** 2)
                left += 1
            else:
                res.append(nums[right] ** 2)
                right -= 1
        res.reverse()
        return res
x = Solution()
print(x.sortedSquares([-4,-1,0,3,10]))
