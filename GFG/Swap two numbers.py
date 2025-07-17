class Solution:
    def get(self, a: int, b: int) -> tuple[int, int]:
        a = a + b 
        b  = a - b 
        a = a - b 
        return a , b 
x = Solution()
print(x.get(1, 2))  # Output: (2, 1)