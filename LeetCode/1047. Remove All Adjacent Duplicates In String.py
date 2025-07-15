# using stack to remove adjacent duplicates in a string
# LeetCode 1047: Remove All Adjacent Duplicates In String

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if (len(stack) != 0 and stack[-1] == i):
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)
x = Solution()
print(x.removeDuplicates("abbaca"))  # Output: "ca"


#  (Or)

# using two pointers to remove adjacent duplicates in a string
class Solution:
    def removeDuplicates(self, s: str) -> str:
        if not s:
            return 0 
        res = []
        for i in s:
            if res and res[-1] == i:
                res.pop()
            else:
                res.append(i)
        return ''.join(res)
x = Solution()
print(x.removeDuplicates("abbaca"))  # Output: "ca"

#  (Or)
# using brute force to remove adjacent duplicates in a string
class Solution:
    def removeDuplicates(self, s: str) -> str:
        while True:
            new_s = ''
            i = 0
            while i < len(s):
                if i < len(s) - 1 and s[i] == s[i + 1]:
                    i += 2  # Skip the next character
                else:
                    new_s += s[i]
                    i += 1
            if new_s == s:  # No more duplicates found
                break
            s = new_s
        return s
x = Solution()
print(x.removeDuplicates("abbaca"))  # Output: "ca"
print(x.removeDuplicates("azxxzy"))  # Output: "ay"
