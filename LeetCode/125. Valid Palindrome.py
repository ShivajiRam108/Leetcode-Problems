class Solution:
    def isPalindrome(self, s: str) -> bool:
        # using two pointers
        new_string = ''.join(
            i.lower()
            for i in s
            if i.isalnum()
        )
        left = 0
        right = len(new_string) - 1
        while left < right:
            if new_string[left] != new_string[right]:
                return False
            left += 1
            right -= 1
        return True 
    
#  Another approach 
        a = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        return a == a[::-1]
    
# Both cases time and space complexity are the same.
# Time Complexity: O(n)
# Space Complexity: O(n)
