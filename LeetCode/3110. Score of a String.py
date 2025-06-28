class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        for i in range(len(s)- 1):
            total += abs(ord(s[i]) - ord(s[i+1]))
        return total 
x = Solution()
print(x.scoreOfString("zaz"))
print(x.scoreOfString("hello"))