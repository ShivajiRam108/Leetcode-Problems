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