class Solution:
     def reverseString(self, s: str) -> str:
        res = ''
        for i in s:
            res = i + res 
        return res
     
        # (or) 
        return s[::-1]
x = Solution()
print(x.reverseString("Hello world"))