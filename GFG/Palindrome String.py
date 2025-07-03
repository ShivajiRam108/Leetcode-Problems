class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s[::-1] == s 
x = Solution()
print(x.isPalindrome("madam"))

# (Or) using two pointers

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0 
        right = len(s) -1
        while left <= right:
            if s[left] != s[right]:
                return False 
            left += 1
            right -= 1
        return True
x  = Solution()
print(x.isPalindrome("abba"))