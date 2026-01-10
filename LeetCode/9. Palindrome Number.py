class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = str(x)
        left = 0 
        right = len(n) - 1
        while left < right:
            if(n[left] != n[right]):
                return False
            left += 1
            right -= 1
        return True 

# Example usage:
solution = Solution()
print(solution.isPalindrome(121))  # Output: True
print(solution.isPalindrome(-121)) # Output: False
print(solution.isPalindrome(10))   # Output: False