class Solution:
    def reverseDegree(self, s: str) -> int:
        res , idx = 0, 1
        for i in s:
            res += (123 - ord(i)) * idx 
            idx += 1 
        return res
x = Solution()
print(x.reverseDegree('abc'))
print(x.reverseDegree("zaza"))

# (Or) 

class Solution:
    def reverseDegree(self, s: str) -> int:
        count = 0 
        for i in range(len(s)):
            count += (i + 1) * (123 - ord(s[i]))
        return count 
x = Solution()
print(x.reverseDegree('abc'))
print(x.reverseDegree("zaza")) 