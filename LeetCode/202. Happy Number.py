class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum(int(d) ** 2 for d in str(n))
            if n == 1:
                return True
        return False
x = Solution()
print(x.isHappy(13))

'''
Happy Number Definition: A happy number is a number that eventually reaches 1 when repeatedly replacing it
by the sum of the squares of its digits. For instance, 19 is a happy number because
1^2 + 9^2 = 82, 8^2 + 2^2 = 68, 6^2 + 8^2 = 100, and 1^2 + 0^2 + 0^2 = 1.
'''