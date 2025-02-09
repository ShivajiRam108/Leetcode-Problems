class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
         # (or)
        l, zeros = 0, 0
        for r, n in enumerate(nums):
            zeros += n == 0
            if zeros > 0:
                zeros -= nums[l] == 0
                l += 1
        return r - l +1

        # (Or)
        return max((len(list(g)) for k, g in groupby(nums) if k == 1), default = 0)
       
        # (Or)Taking user input
        l, zeros = 0, 0
        max_length = 0  # To store the maximum sequence length

        for r, n in enumerate(nums):
            zeros += n == 0

            if zeros > 0:
                zeros -= nums[l] == 0
                l += 1

            max_length = max(max_length, r - l + 1)

        return max_length


# Taking user input
nums = list(map(int, input("Enter space-separated binary numbers (0s and 1s): ").split()))

solution = Solution()
result = solution.findMaxConsecutiveOnes(nums)

print("Maximum Consecutive Ones:", result)

