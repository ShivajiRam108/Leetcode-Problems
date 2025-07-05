class Solution:
    def lastIndex(self, s: str) -> int:
        for i in range(len(s)-1,-1,-1):
            if s[i] == '1':
                return i 
        return -1
x = Solution()
print(x.lastIndex('00001'))
print(x.lastIndex('0'))