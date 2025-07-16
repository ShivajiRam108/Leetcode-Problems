class Solution:
    def maximumLength(self, n: list[int]) -> int:
        even = 0
        odd = 0
        for i in n:
            if i % 2 == 0:
                even += 1 
            else:
                odd += 1
        count_even = 0 
        count_odd = 0
        for i in n:
            if i % 2 == 0:
                count_even = max(count_even , count_odd + 1)
            else:
                count_odd = max(count_odd  , count_even + 1)
        return max(odd, even , count_even, count_odd)
x = Solution()
print(x.maximumLength([1, 2, 3, 4, 5]))
print(x.maximumLength([1,2,1,1,2,1,2]))
print(x.maximumLength([1, 2,3,4]))