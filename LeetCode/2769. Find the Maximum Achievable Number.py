class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2 * t
    
x = Solution()
print(x.theMaximumAchievableX(4, 1))